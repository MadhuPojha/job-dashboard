from rapidfuzz import fuzz

AI_ML = [
    "machine learning", "ai engineer", "ml engineer",
    "data scientist", "deep learning", "nlp",
    "artificial intelligence", "computer vision", "mlops"
]

FULLSTACK = [
    "full stack", "fullstack", "react", "node", "django"
]

EXCLUDE = [
    "ux designer", "product manager", "recruiter"
]


def classify(title: str):
    t = title.lower()

    if any(x in t for x in EXCLUDE):
        return None

    ai_score = max(fuzz.partial_ratio(t, k) for k in AI_ML)
    fs_score = max(fuzz.partial_ratio(t, k) for k in FULLSTACK)

    if ai_score > 80:
        return "AI/ML"

    if fs_score > 80:
        return "Fullstack"

    if "frontend" in t:
        return "Frontend"

    if "backend" in t:
        return "Backend"

    if "devops" in t or "aws" in t:
        return "System"

    return "Software"
