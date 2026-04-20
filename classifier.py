from rapidfuzz import fuzz

AI_ML_KEYWORDS = [
    "machine learning",
    "ml engineer",
    "ai engineer",
    "artificial intelligence",
    "data scientist",
    "mlops",
    "deep learning",
    "computer vision",
    "nlp"
]

FULLSTACK_KEYWORDS = [
    "full stack",
    "software engineer (full",
    "full-stack",
    "backend + frontend",
    "react + python",
    "node + react"
]

FRONTEND_KEYWORDS = [
    "frontend",
    "front end",
    "react",
    "angular",
    "vue"
]

BACKEND_KEYWORDS = [
    "backend",
    "django",
    "flask",
    "spring",
    "api"
]

SYSTEM_KEYWORDS = [
    "devops",
    "aws",
    "kubernetes",
    "cloud",
    "platform engineer",
    "site reliability"
]

EXCLUDE = [
    "ux designer",
    "product manager"
]


def score(title, keywords):
    return max(fuzz.partial_ratio(title.lower(), k) for k in keywords)


def classify(title: str):
    t = title.lower()

    # ❌ exclude first
    if any(x in t for x in EXCLUDE):
        return None

    # 🧠 AI/ML (highest priority after fullstack)
    if score(t, AI_ML_KEYWORDS) > 75:
        return "AI/ML"

    # 🚀 FULLSTACK (FIXED: broader detection)
    if (
        "full stack" in t
        or "fullstack" in t
        or score(t, FULLSTACK_KEYWORDS) > 70
        or ("react" in t and "backend" in t)
        or ("frontend" in t and "backend" in t)
    ):
        return "Fullstack"

    # 🎨 Frontend
    if score(t, FRONTEND_KEYWORDS) > 75:
        return "Frontend"

    # ⚙️ Backend
    if score(t, BACKEND_KEYWORDS) > 75:
        return "Backend"

    # ☁️ System
    if score(t, SYSTEM_KEYWORDS) > 75:
        return "System"

    return "Software"