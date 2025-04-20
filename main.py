from fastapi import FastAPI, File, UploadFile
import shutil
from ai_processor import query_huggingface,query_local_ai, summarize_text, extract_key_insights
from rag_processor import extract_text_from_pdf, add_to_knowledge_base, retrieve_relevant_info
from web_scraper import scrape_article
from search_engine import search_documents, add_document
from multi_modal_processor import extract_text_from_image
from ai_processor import summarize_multiple_texts
from ai_processor import query_local_ai, summarize_text, extract_key_insights, summarize_multiple_texts
import os  
from io import BytesIO


app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI-Powered AR-DMS is running!"}

@app.post("/analyze/")
def analyze_text(query: str):
    """Retrieve relevant context and analyze text input using AI model."""
    context = retrieve_relevant_info(query)
    enhanced_query = f"Context: {context} \nQuestion: {query}"
    response = query_huggingface(enhanced_query)
    return {"AI Response": response}

@app.post("/upload-pdf/")
def upload_pdf(file: UploadFile = File(...)):
    """Extracts text from a PDF and adds it to the knowledge base."""
    pdf_path = f"temp_{file.filename}"
    
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    extracted_text = extract_text_from_pdf(pdf_path)
    add_to_knowledge_base(extracted_text)
    
    return {"message": f"PDF '{file.filename}' added to knowledge base.", "Extracted Text": extracted_text}

@app.post("/scrape/")
def scrape_and_store(url: str):
    """Scrape a webpage and store its content in the knowledge base."""
    return scrape_article(url)
@app.post("/summarize/")
def summarize_content(text: str):
    """Summarizes input text to extract key points."""
    summary = summarize_text(text)
    return {"Summary": summary}

@app.post("/extract-insights/")
def extract_insights(text: str):
    """Extracts key insights from the text."""
    insights = extract_key_insights(text)
    return {"Key Insights": insights}
@app.post("/search/")
def search_content(query: str):
    """Search for specific topics in stored documents."""
    results = search_documents(query)
    return {"Search Results": results}

@app.post("/add-document/")
def add_new_document(title: str, content: str):
    """Add a new document to the search index."""
    add_document(title, content)
    return {"message": f"Document '{title}' added to search index."}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """Uploads an image and extracts text using OCR."""
    try:
        image_path = f"temp_{file.filename}"  # ✅ Save temp image file

        # ✅ Save uploaded file temporarily
        with open(image_path, "wb") as buffer:
            buffer.write(await file.read())

        # ✅ Process the image and extract text
        extracted_text = extract_text_from_image(image_path)

        # ✅ Cleanup: Remove temporary file
        os.remove(image_path)

        return {"text": extracted_text.strip() if extracted_text.strip() else "No text found in image."}

    except Exception as e:
        return {"error": f"Image processing failed: {str(e)}"}

