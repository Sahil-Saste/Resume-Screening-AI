# 🧠 AI Resume Screening App

A smart, AI-powered resume screening system built with **Python**, **NLP**, and **Streamlit**.

This project analyzes a candidate's resume against a job description using:
- ✅ Keyword-based skill matching (regex enhanced)
- 🧠 Semantic similarity with **Sentence-BERT**
- 📊 Visual feedback (pie charts, match %)
- 🤝 Combined Relevance Score

---

## 🚀 Features

- Upload resume in **PDF**
- Paste job description
- See:
  - Skill Match Score ✅
  - Semantic Similarity Score 🧠
  - Combined Relevance Score 🤝
  - Missing Skills in bullet format
- Pie chart for visual feedback 📊

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🌐
- Sentence-BERT (`sentence-transformers`)
- PyMuPDF (PDF parsing)
- Plotly (charts)

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/yourusername/Resume-Screening-AI.git
cd Resume-Screening-AI
python -m venv venv
venv\Scripts\activate       # on Windows
pip install -r requirements.txt
streamlit run streamlit_app.py
