from sentence_transformers import SentenceTransformer, util

# Load model only once when the file is imported
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_semantic_similarity(resume_text, jd_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    
    similarity_score = util.cos_sim(resume_embedding, jd_embedding).item()
    return round(similarity_score * 100)  # Convert to percent 