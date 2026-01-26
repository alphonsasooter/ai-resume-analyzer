def analyze_resume(text: str) -> dict:
    text = text.lower()

    skills_map = {
        "python": "Python",
        "fastapi": "FastAPI",
        "mysql": "MySQL",
        "flutter": "Flutter",
        "docker": "Docker",
        "aws": "AWS"
    }

    skills = [value for key, value in skills_map.items() if key in text]

    return {
        "summary": "Resume analyzed successfully",
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