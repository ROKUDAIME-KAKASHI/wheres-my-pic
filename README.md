# Where’s My Pic? 🔍🖼️

A **semantic image search engine** built using **CLIP, FAISS, and Flask**.  
Search your local images using **natural language queries**.

---

## 🚀 Features
- Text-to-image search using CLIP
- Fast similarity search with FAISS
- Simple Flask web interface
- Works offline on local images

---

## 📁 How to Run

```bash
pip install -r requirements.txt
python index_images.py   # build FAISS index
python app.py            # start server
