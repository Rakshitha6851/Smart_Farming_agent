"""
Configuration module for Smart Farming Agent
Loads and manages application configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =========================================
# IBM Watsonx Configuration
# =========================================

IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID")
IBM_URL = os.getenv("IBM_URL", os.getenv("IBM_REGION_URL"))

# Fallback credentials for testing (REPLACE WITH YOUR OWN)
if not IBM_API_KEY:
    print("⚠️  WARNING: IBM_API_KEY not found in environment variables!")
    print("   Using test/demo credentials. For production, set IBM_API_KEY in .env file")
    IBM_API_KEY = "So8rv6i0xqMe6QXMjv2DqonioB7vQdq7q4HJbCxg3jDN"

if not IBM_PROJECT_ID:
    print("⚠️  WARNING: IBM_PROJECT_ID not found in environment variables!")
    IBM_PROJECT_ID = "b91263d7-790d-47e0-a35e-0402b1734811"

if not IBM_URL:
    print("⚠️  WARNING: IBM_URL not found in environment variables!")
    IBM_URL = "https://au-syd.ml.cloud.ibm.com"

IBM_CREDENTIALS = {
    "url": IBM_URL,
    "apikey": IBM_API_KEY,
    "project_id": IBM_PROJECT_ID
}

# IBM Model Configuration (Llama as per requirements)
IBM_MODEL_ID = os.getenv("IBM_MODEL_ID", "meta-llama/llama-3-3-70b-instruct")

# Alternative models available:
# "meta-llama/llama-3-3-70b-instruct"  # Llama 3.3 (Recommended)
# "ibm/granite-34b-code-instruct"      # IBM Granite
# "mistralai/mistral-large"             # Mistral

# =========================================
# External API Configuration
# =========================================

# Data.gov API Configuration
DATA_GOV_API_KEY = os.getenv("DATA_GOV_API_KEY", "")

# Weather API Configuration (OpenWeatherMap)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "e113ca2a843002a4b086fc716a8d581f")
WEATHER_API_TIMEOUT = 10  # seconds

# =========================================
# Vector Database Configuration
# =========================================

VECTOR_DB_DIR = os.getenv("VECTOR_DB_DIR", "chroma_db")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")

# Alternative embeddings:
# "sentence-transformers/all-MiniLM-L6-v2"
# "sentence-transformers/all-mpnet-base-v2"

# =========================================
# Flask Configuration
# =========================================

FLASK_ENV = os.getenv("FLASK_ENV", "development")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

# =========================================
# Application Settings
# =========================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MAX_RESPONSE_LENGTH = int(os.getenv("MAX_RESPONSE_LENGTH", "1000"))

# =========================================
# Feature Flags
# =========================================

ENABLE_RAG = os.getenv("ENABLE_RAG", "True").lower() == "true"
ENABLE_WEATHER = os.getenv("ENABLE_WEATHER", "True").lower() == "true"
ENABLE_MANDI = os.getenv("ENABLE_MANDI", "True").lower() == "true"
ENABLE_AI = os.getenv("ENABLE_AI", "True").lower() == "true"

# =========================================
# API Configuration
# =========================================

API_TIMEOUT = 10  # seconds
MAX_RETRIES = 3

# Supported Languages (for translation)
SUPPORTED_LANGUAGES = [
    "en",  # English
    "hi",  # Hindi
    "ta",  # Tamil
    "te",  # Telugu
    "kn",  # Kannada
    "ml",  # Malayalam
    "mr",  # Marathi
    "gu",  # Gujarati
    "bn",  # Bengali
    "pa"   # Punjabi
]

DEFAULT_LANGUAGE = "en"

# =========================================
# Startup Info
# =========================================

print("\n" + "="*60)
print("✅ Smart Farming Agent - Configuration Loaded")
print("="*60)
print(f"IBM Model:        {IBM_MODEL_ID}")
print(f"Embedding Model:  {EMBEDDING_MODEL}")
print(f"Vector DB:        {VECTOR_DB_DIR}")
print(f"Flask Debug:      {FLASK_DEBUG}")
print(f"RAG Enabled:      {ENABLE_RAG}")
print(f"Weather Enabled:  {ENABLE_WEATHER}")
print(f"Mandi Enabled:    {ENABLE_MANDI}")
print(f"AI Enabled:       {ENABLE_AI}")
print("="*60 + "\n")
