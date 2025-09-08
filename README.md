AR-DMS is an AI-powered system that extracts, processes, and analyzes research data from various sources, including PDFs, web articles, and images. The system supports functionalities such as text extraction, summarization, search, and report generation.

##Features
📄 Upload & Extract: Extract text from PDFs, images, and web pages.
🔎 Search & Insights: Retrieve context-aware insights using AI-powered search.
✍ Summarization: Generate concise summaries from large documents.
📊 Report Generation: Compile extracted and processed data into structured reports.
🖼 OCR Support: Convert scanned documents into editable text.

##Tech Stack
 pip install fastapi uvicorn pydantic sqlalchemy asyncpg alembic psycopg2 langchain \
huggingface-hub sentence-transformers pdfplumber pytesseract pdf2image numpy opencv-python \
scipy pandas nltk transformers newspaper3k beautifulsoup4 requests tqdm \
faiss-cpu whoosh lxml python-dotenv

Backend: FastAPI
OCR: pytesseract, pdf2image
NLP & AI: LangChain, Hugging Face Transformers, FAISS
Database: SQLite / PostgreSQL (optional)
in windows powershell(run as adminisrtation)
1.cd AR-DMS
2.python -m venv ardms_env
(Create & Activate Virtual Environment) 
{Activate the environment:
Windows (CMD):
ardms_env\Scripts\activate
powershell
.\ardms_env\Scripts\Activate}
3.uvicorn main:app --reload
4.ctrl+c to exit
check http://127.0.0.1:8000/
http://127.0.0.1:8000/docs#/


conda activate ardms_env
