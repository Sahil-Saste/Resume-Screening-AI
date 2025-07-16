# AI Resume Screening Project

A full-stack application for automated resume screening using React (frontend) and Python FastAPI (backend). This tool helps recruiters quickly assess how well a candidate’s resume matches a job description by extracting and comparing skills, and computing a relevance score.

---

## 🚀 Features
- **PDF Resume Upload:** Upload resumes in PDF format for analysis.
- **Job Description Input:** Paste or type the job description for matching.
- **Skill Extraction & Matching:** Extracts skills from both resume and job description using a comprehensive O*NET-based skills list.
- **Semantic Similarity:** Uses advanced NLP to compare resume content with job requirements.
- **Visual Results:** Displays scores and a pie chart of matched vs. missing skills.
- **Modern UI:** Clean, responsive React interface.
- **Modular Backend:** FastAPI backend with clear, extensible endpoints.

---

## 🖥️ Screenshots

> _Add screenshots of the UI and results here!_

- ![Home Page](screenshots/home.png)
- ![Results Example](screenshots/results.png)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <project-folder>
```

### 2. Backend Setup (FastAPI)
1. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the backend server:**
   ```sh
   uvicorn app:app --reload
   ```
   The API will be available at [http://localhost:8000](http://localhost:8000).

### 3. Frontend Setup (React)
1. **Install Node dependencies:**
   ```sh
   cd frontend
   npm install
   ```
2. **Start the React app:**
   ```sh
   npm start
   ```
   The app will run at [http://localhost:3000](http://localhost:3000).

---

## 📝 Usage
1. Open the React app in your browser.
2. Upload a PDF resume and paste a job description.
3. Click "Submit" to analyze.
4. View the skill match score, semantic similarity, combined score, and a pie chart of matched/missing skills.

---

## 🗂️ Key Files & Structure
- `frontend/src/App.js` – Main React component (UI, API calls, chart)
- `app.py` – FastAPI backend (API endpoints)
- `resume_parser.py` – PDF text extraction
- `skill_matcher.py` – Skill extraction and matching logic
- `semantic_matcher.py` – Semantic similarity scoring
- `skills_list.txt` – O*NET-based skills database

---

## 🌟 Extending the Project
- Add fuzzy matching or synonyms for skills
- Section-based weighting (e.g., skills in "Experience" count more)
- More robust error handling and user feedback
- Add authentication or user management
- Deploy backend (Heroku, AWS, Azure) and frontend (Netlify, Vercel)

---

## 📸 Screenshots
> _Add your own screenshots in the `screenshots/` folder and update the links above._

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](LICENSE) 