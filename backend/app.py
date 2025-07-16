from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills, calculate_match_score
from semantic_matcher import calculate_semantic_similarity
import uvicorn

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load skills list once (O*NET only, lowercase for matching)
with open("skills_list.txt", "r", encoding="utf-8") as f:
    all_skills = [line.strip() for line in f.readlines() if line.strip() != ""]

  

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read PDF and extract text
    resume_text = extract_text_from_pdf(await file.read())

    # Extract skills from resume and job description
    resume_skills = extract_skills(resume_text, all_skills)
    jd_skills = extract_skills(job_description, all_skills)

    # Skill match score
    score, matched, missing = calculate_match_score(resume_skills, jd_skills)

    # Semantic similarity
    semantic_score = calculate_semantic_similarity(resume_text, job_description)

    # Combined score
    combined_score = int((score * 0.4) + (semantic_score * 0.6))

    return JSONResponse({
        "skill_match_score": score,
        "semantic_similarity_score": semantic_score,
        "combined_score": combined_score,
        "matched_skills": matched,
        "missing_skills": missing
    })

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 