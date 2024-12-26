from fastapi import FastAPI, UploadFile
from google.cloud import vision
from google.protobuf.json_format import MessageToDict
import config


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Exam Practice App!"}


@app.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()

    # Save the file temporarily
    temp_file = "uploaded_file.pdf" if file.filename.endswith(".pdf") else "uploaded_file.jpg"
    with open(temp_file, "wb") as f:
        f.write(content)

    # Initialize Google Cloud Vision client
    client = vision.ImageAnnotatorClient()

    # Read the file content for OCR
    with open(temp_file, "rb") as image_file:
        image = vision.Image(content=image_file.read())

    response = client.document_text_detection(image=image)
    annotations = response.full_text_annotation

    if annotations:
        extracted_text = annotations.text
    else:
        extracted_text = "No text detected."

    return {"extracted_text": extracted_text}
