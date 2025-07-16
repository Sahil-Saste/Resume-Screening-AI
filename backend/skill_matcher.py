import re

def extract_skills(text, skill_set):
    found_skills = []
    text_lower = text.lower()

    for skill in skill_set:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return list(set(found_skills))

def calculate_match_score(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    score = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0
    return score, matched, missing 