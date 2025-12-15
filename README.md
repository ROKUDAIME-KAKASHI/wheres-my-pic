# Where’s My Pic? 🔍🖼️  
### Semantic Image Search using CLIP + FAISS + Flask

**Where’s My Pic?** is a local **semantic image search engine** that allows users to search images using **natural language text queries** instead of filenames or tags.

The system uses **CLIP** for text–image understanding and **FAISS** for ultra-fast similarity search, served through a **Flask web application**.



🚀 Features

- 🔎 Search images using natural language (e.g., *“a dog running on grass”*)
- 🧠 CLIP-based multimodal embeddings (text + image)
- ⚡ FAISS-powered fast vector similarity search
- 🌐 Lightweight Flask web interface
- 📂 Works completely offline
- 📈 Scales to thousands of images



🏗️ System Architecture

Text Query ──▶ CLIP Text Encoder ──▶ FAISS Search
│
Images ──▶ CLIP Image Encoder ──▶ FAISS Index
│
Ranked Images


📁 Project Structure

wheres_my_pic/
├── app.py # Flask web application
├── index_images.py # Script to build FAISS index (run once)
├── requirements.txt # Python dependencies
├── README.md
├── .gitignore
│
├── images/ # Image dataset (ignored in Git)
│ ├── img1.jpg
│ ├── img2.png
│ └── ...
│
├── data/ # FAISS index + metadata (ignored in Git)
│ ├── faiss.index
│ └── image_paths.pkl
│
└── templates/
└── index.html # Web UI



🛠️ Tech Stack

  Python
  PyTorch
  OpenCLIP
  FAISS
  Flask
  HTML / CSS

 ⚙️ Installation

 1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/wheres-my-pic.git
cd wheres-my-pic
2️⃣ Install dependencies
pip install -r requirements.txt
🖼️ Add Images
Place your images inside the images/ folder:
images/
 ├── beach.jpg
 ├── dog.png
 └── sunset.jpeg
Supported formats:

.jpg
.png
.jpeg
.webp

🧠 Build the FAISS Index (Run Once)
bash
Copy code
python index_images.py
This will:

Encode all images using CLIP
Build a FAISS similarity index
Save index + image paths to data/
⚠️ Re-run this script if you add or remove images.

▶️ Run the Application

python app.py
Open your browser at:
http://127.0.0.1:5000

🔍 Example Queries
a dog playing outside
a beach at sunset
people walking on the street
mountains with snow

📈 Performance Notes
FAISS provides sub-millisecond search for thousands of images
CLIP embeddings are normalized for cosine similarity
Image resolution matters: higher resolution images give better semantic understanding

📌 Future Improvements
Image upload search
FAISS HNSW / IVF indexing
Docker deployment
Web hosting / cloud deployment
Mobile-friendly UI

🧾 License
This project is licensed under the MIT License.

👤 Author
Built by ROKUDAIME-KAKASHI
AI / Machine Learning Enthusiast

⭐ If you like this project
Give it a star ⭐ on GitHub!
