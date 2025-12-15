import os
import pickle
import numpy as np
import torch
import open_clip
import faiss
from PIL import Image

IMAGE_DIR = "images"   # ⬅️ ADD IMAGES HERE
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, _, preprocess = open_clip.create_model_and_transforms(
        "ViT-B-32", pretrained="openai"
    )
    return model.to(device), preprocess, device


def image_to_embedding(path, model, preprocess, device):
    img = Image.open(path).convert("RGB")
    img = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        emb = model.encode_image(img)
    emb /= emb.norm(dim=-1, keepdim=True)
    return emb.cpu().numpy()[0]


model, preprocess, device = load_model()

paths = []
vectors = []

for root, _, files in os.walk(IMAGE_DIR):
    for f in files:
        if f.lower().endswith(("jpg", "png", "jpeg", "webp")):
            full = os.path.join(root, f)
            try:
                vec = image_to_embedding(full, model, preprocess, device)
                vectors.append(vec)
                paths.append(full)
            except Exception as e:
                print("Skipped", full, e)

vectors = np.array(vectors).astype("float32")

# --- FAISS INDEX ---
dim = vectors.shape[1]
index = faiss.IndexFlatIP(dim)   # Inner Product = cosine (normalized)
index.add(vectors)

faiss.write_index(index, f"{DATA_DIR}/faiss.index")

with open(f"{DATA_DIR}/image_paths.pkl", "wb") as f:
    pickle.dump(paths, f)

print("Indexed", len(paths), "images")