# AI Document Intelligence Backend

A modular Transformer-based backend for:

- Text Understanding
- Text Summarization
- Semantic Search
- Document Intelligence
- Entity Extraction
- Document Embeddings

## Technologies

Python
Flask
Hugging Face Transformers
Sentence Transformers
FAISS
spaCy
PyMuPDF
python-docx

## Installation

Create a virtual environment:

python -m venv venv

Activate:

Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Install spaCy model:

python -m spacy download en_core_web_sm

## Run

python app.py

Server:

http://127.0.0.1:5000

## API

GET /api/health

POST /api/understand

POST /api/summarize

POST /api/search

POST /api/documents/upload

## Example Understanding Request

POST /api/understand

{
    "text": "Apple announced a new product in California."
}

## Example Summarization Request

POST /api/summarize

{
    "text": "Your long document text..."
}

## Example Semantic Search

POST /api/search

{
    "query": "machine learning applications",
    "top_k": 5
}

## Document Upload

POST /api/documents/upload

Use multipart/form-data.

Field:

file

Supported formats:

PDF
DOCX
TXT