def analyze_resume(text: str):
    text = text.lower()

    skills = []
    if "python" in text:
        skills.append("Python")
    if "fastapi" in text:
        skills.append("FastAPI")
    if "mysql" in text:
        skills.append("MySQL")
    if "flutter" in text:
        skills.append("Flutter")

    return {
        "summary": "Backend developer resume analyzed successfully",
        "skills_found": skills,
        "strengths": [
            "API development",
            "Backend logic",
            "Database knowledge"
        ],
        "weaknesses": [
            "Cloud deployment",
            "Automated testing"
        ],
        "suggestions": [
            "Learn Docker",
            "Add unit tests",
            "Deploy on cloud"
        ],
        "score": min(60 + len(skills) * 10, 100)
    }