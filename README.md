# Where’s My Pic? 🔍🖼️

A **semantic image search engine** using **CLIP + FAISS + Flask**.

Search your local images using **natural language**.

---

## 🚀 Features
- CLIP-based text–image embeddings
- FAISS for ultra-fast similarity search
- Flask web interface
- Works fully offline
- Scales to thousands of images

---

## 📁 Project Structure
```
where-is-my-pic/
├── app.py
├── cli.py
├── config.py
├── data/
│   ├── images/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   └── embeddings.json
├── requirements.txt
└── README.md
```

---

## 📚 Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the CLI
```bash
python cli.py
```