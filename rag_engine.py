import os
import sys
import signal
from contextlib import contextmanager

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import VECTOR_DB_DIR, EMBEDDING_MODEL

print("Starting RAG setup...")

# =====================================================
# TIMEOUT HANDLER
# =====================================================

class TimeoutException(Exception):
    pass

@contextmanager
def time_limit(seconds):
    """Context manager for timeout handling"""
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    
    # Note: signal only works on Unix. For Windows, we'll use a try-except approach
    if hasattr(signal, 'SIGALRM'):
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(seconds)
    try:
        yield
    finally:
        if hasattr(signal, 'SIGALRM'):
            signal.alarm(0)

# =====================================================
# LOAD DOCUMENTS (with size check)
# =====================================================

documents = []

DATA_FOLDER = "data"

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    print(f"Created {DATA_FOLDER} folder. Add PDFs to this folder.")

pdf_files = [f for f in os.listdir(DATA_FOLDER) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("ℹ️  No PDF files found in 'data' folder.")
    print("Using knowledge base only. Add PDFs to 'data/' to enable RAG.")
    # Continue without PDFs - knowledge base will still work
    documents = []
else:
    for file in pdf_files:
        pdf_path = os.path.join(DATA_FOLDER, file)
        file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        
        # Skip very large PDFs
        if file_size_mb > 50:
            print(f"⚠️  Skipping {file} (too large: {file_size_mb:.1f}MB)")
            continue

        print(f"📄 Loading PDF: {file} ({file_size_mb:.1f}MB)")

        try:
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()
            print(f"   ✓ Loaded {len(pages)} pages")
            documents.extend(pages)

        except Exception as e:
            print(f"   ✗ Failed loading {file}: {e}")
            continue

if not documents:
    print("ℹ️  No documents loaded from PDFs. Using knowledge base only.")
    # Create a minimal document for vector DB
    documents = []
else:
    print(f"Total pages loaded: {len(documents)}")

# =====================================================
# SPLIT DOCUMENTS
# =====================================================

if documents:
    print("Splitting documents into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)
    print(f"Generated {len(docs)} chunks")
else:
    print("Skipping document splitting (no documents)")
    docs = []

# =====================================================
# CLEAN CHUNKS
# =====================================================

clean_texts = []
clean_metadatas = []

for idx, doc in enumerate(docs):
    try:
        text = doc.page_content

        if text is None:
            continue

        # Ensure it's a string
        text = str(text)
        
        # Remove null characters 
        text = text.replace("\x00", " ")
        
        # Remove problematic unicode characters
        text = text.encode('utf-8', 'ignore').decode('utf-8')
        
        # Clean whitespace
        text = ' '.join(text.split())
        
        if len(text) < 5:
            continue

        clean_texts.append(text)

        meta = {}
        if hasattr(doc, "metadata"):
            meta = {k: str(v) for k, v in doc.metadata.items()}
        
        clean_metadatas.append(meta)

    except Exception as e:
        print(f"Skipping chunk {idx}: {e}")

print(f"Valid chunks: {len(clean_texts)}")

# =====================================================
# EMBEDDINGS
# =====================================================

print("Loading embedding model...")

try:
    embedding = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    print("✓ Embedding model loaded successfully")
except Exception as e:
    print(f"✗ Failed to load embedding model: {e}")
    embedding = None

# =====================================================
# PREPARE TEXTS FOR EMBEDDING
# =====================================================

valid_texts = []
valid_metadatas = []

for text, meta in zip(clean_texts, clean_metadatas):
    try:
        # Ensure text is proper string type
        if isinstance(text, str) and len(text.strip()) > 0:
            valid_texts.append(text.strip())
            valid_metadatas.append(meta)
    except Exception as e:
        print(f"Warning: Skipping text due to: {e}")

print(f"Ready to embed {len(valid_texts)} chunks")

# =====================================================
# CREATE VECTOR DATABASE
# =====================================================

VECTOR_DIR = VECTOR_DB_DIR

os.makedirs(VECTOR_DIR, exist_ok=True)

if not valid_texts:
    print("⚠️  No valid texts to embed. Vector DB will be created with sample data.")
    # Add sample farming knowledge as fallback
    valid_texts = [
        "Smart farming techniques include crop rotation, soil testing, weather monitoring, and pest management.",
        "Mandi prices fluctuate based on supply and demand. Check local market rates daily.",
        "Black soil is ideal for cotton, groundnut, and sugarcane. Red soil suits pulses and oil seeds.",
        "Common pests include aphids, whiteflies, and armyworms. Use organic or chemical control measures."
    ]
    valid_metadatas = [{"source": "knowledge_base"} for _ in valid_texts]

print("Creating vector database...")

try:
    if embedding:
        # Ensure all texts are strings and properly formatted
        texts_to_embed = [str(t).strip() for t in valid_texts if t]
        
        if texts_to_embed:
            vector_db = Chroma.from_texts(
                texts=texts_to_embed,
                embedding=embedding,
                metadatas=valid_metadatas[:len(texts_to_embed)],
                persist_directory=VECTOR_DIR
            )
            print("✓ Vector database created successfully!")
        else:
            print("⚠️  No texts available for embedding")
            sys.exit(1)
    else:
        print("✗ Embedding model not available. Skipping vector DB creation.")
        sys.exit(1)

except Exception as e:
    print("✗ Failed creating vector database")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print(f"✓ Stored at: {VECTOR_DIR}")
print("\n✅ RAG setup completed!")