from fastapi import FastAPI
from app.routers.analyze import router

app = FastAPI(title="AI Resume Analyzer API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Main app is working"}