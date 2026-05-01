from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.audio_service import extract_audio
from app.services.whisper_service import transcribe_audio
from app.services.translation_service import translate_text

router = APIRouter()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    audio_path = extract_audio(file_path)
    transcription, language = transcribe_audio(audio_path)
    translated = translate_text(transcription)

    output_file = f"{OUTPUT_DIR}/{file.filename}.txt"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated)

    return {
        "language_detected": language,
        "transcription": transcription,
        "translated": translated,
        "file": output_file
    }