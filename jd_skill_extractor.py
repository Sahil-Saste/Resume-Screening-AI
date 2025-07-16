"""
Simple skill extraction from job descriptions by matching skills as whole words.

Instructions:
Use extract_skills_from_jd(jd_text, skills_set) to extract skills from a job description.
  - jd_text: The job description string.
  - skills_set: a set of canonical skills to filter against (e.g., from O*NET).
"""

import re

def extract_skills_from_jd(jd_text, skills_set):
    jd_text_lower = jd_text.lower()
    found_skills = set()
    for skill in skills_set:
        # Match as whole word (case-insensitive)
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, jd_text_lower):
            found_skills.add(skill)
    return list(found_skills) 