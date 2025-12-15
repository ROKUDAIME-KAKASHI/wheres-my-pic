import os
import pickle
import numpy as np
import torch
import open_clip
import faiss
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_folder="images")
DATA_DIR = "data"
IMAGE_DIR = "images"


def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, _, preprocess = open_clip.create_model_and_transforms(
        "ViT-B-32", pretrained="openai"
    )
    return model.to(device), preprocess, device


def text_to_embedding(text):
    tokens = open_clip.tokenize([text]).to(device)
    with torch.no_grad():
        emb = model.encode_text(tokens)
    emb /= emb.norm(dim=-1, keepdim=True)
    return emb.cpu().numpy().astype("float32")


# ---- LOAD EVERYTHING ----
model, preprocess, device = load_model()
index = faiss.read_index(f"{DATA_DIR}/faiss.index")

with open(f"{DATA_DIR}/image_paths.pkl", "rb") as f:
    paths = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index_page():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"]
        q_vec = text_to_embedding(query)
        scores, ids = index.search(q_vec, 10)

        for score, idx in zip(scores[0], ids[0]):
            # convert absolute path → filename
            filename = os.path.basename(paths[idx])

            # Flask static URL
            img_url = url_for("static", filename=filename)

            results.append((img_url, float(score)))

    return render_template("index.html", results=results, query=query)


if __name__ == "__main__":
    app.run(debug=True)
