import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DATA_FOLDER = os.path.join(BASE_DIR, "data")

VECTOR_INDEX = os.path.join(DATA_FOLDER, "index.faiss")
VECTOR_METADATA = os.path.join(DATA_FOLDER, "metadata.json")

MAX_CONTENT_LENGTH = 50 * 1024 * 1024

SUMMARY_MODEL = "facebook/bart-large-cnn"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)