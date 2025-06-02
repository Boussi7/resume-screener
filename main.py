from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from utils.pdf_parser import extract_text_from_pdf
from model.embedder import get_embedding
from model.scorer import get_similarity_score

app = FastAPI()

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_resume(
    request: Request,
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Save uploaded resume
    resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    with open(resume_path, "wb") as f:
        f.write(await resume.read())

    # Extract text from resume
    resume_text = extract_text_from_pdf(resume_path)

    # Score using SBERT
    resume_emb = get_embedding(resume_text)
    job_emb = get_embedding(job_description)
    score = get_similarity_score(resume_emb, job_emb)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "score": round(score, 4),
        "filename": resume.filename
    })