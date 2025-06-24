# 📄 Automated Metadata Generation System

## 🎯 Objective

This project builds a user-friendly, Streamlit-based web app for **automated metadata generation** from documents. It extracts key information from various unstructured formats like **PDF**, **DOCX**, and **TXT**, enhancing discoverability, classification, and content analysis.

---

## 💡 Features

- Extracts and processes text from PDF, DOCX, and TXT files
- Identifies top keywords, document length, and preview
- Automatically generates structured metadata
- Option to export metadata as CSV
- Easy-to-use web interface built with Streamlit
- Compatible with Jupyter Notebook for testing and experimentation

---

## 📁 Folder Structure

```bash
autometa/
├── .venv/                     # Python virtual environment (auto-created)
├── streamlit_app.py          # Streamlit web app
├── metadata_generator.ipynb  # Jupyter notebook version
├── README.md                 # This file
├── requirements.txt          # Python packages list (optional)
└── sample_docs/              # Test documents folder
    ├── sample1.pdf           # Academic-style PDF
    ├── sample2.docx          # Proposal-style DOCX
    └── notes.txt             # Diary-style text file
````

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
cd autometa
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Required Libraries

```bash
pip install streamlit python-docx PyMuPDF pandas
```

### 3. (Optional) Enable Jupyter Kernel Support

```bash
pip install notebook ipykernel
python -m ipykernel install --user --name=autometa-kernel --display-name "Python (.venv - autometa)"
```

---

## 🚀 Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

* Upload a PDF, DOCX, or TXT file
* Instantly see structured metadata
* Optionally download the metadata as a CSV

---

## 📓 Jupyter Notebook Usage

1. Open `metadata_generator.ipynb` in VS Code
2. Select kernel: `Python (.venv - autometa)`
3. Run each cell step-by-step
4. Export the final metadata using:

```python
df.to_csv("generated_metadata.csv", index=False)
```

---

## 📂 Sample Documents

Use test files provided in `sample_docs/`:

* `sample1.pdf` — AI in Healthcare
* `sample2.docx` — Green Energy Proposal
* `notes.txt` — Daily productivity notes

---

## 🚫 Limitations

* No OCR or scanned image support (excluded `pytesseract`, `textract`)
* Basic keyword extraction logic
* Currently designed for local usage only

---

## 🔮 Future Work

* Add NLP-based summary and topic detection
* Detect author name, abstract, and section headers
* Deploy to Streamlit Cloud with upload history

---

## 👩‍💻 Author

Muskan Verma
B.Tech, Metallurgical & Materials Engineering
IIT Roorkee

