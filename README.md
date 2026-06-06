# Smart Farming AI Agent

## Problem Statement

**Problem Statement No.9 – AI Agent for Smart Farming Advice** 

**The Challenge** – An AI Agent for Smart Farming Advice, powered by RAG (Retrieval-Augmented 
Generation), supports small-scale farmers by delivering real-time, localized agricultural guidance. 
It retrieves trusted data on weather forecasts, soil conditions, crop recommendations, pest control 
measures, and current market prices from agricultural departments, meteorological sources, and agri
tech platforms. 
Farmers can interact in their local language and ask questions like “What crop is best for this season?” 
or “What is today’s mandi rate for tomatoes?” 
The agent ensures timely, data-driven decisions that reduce risk, increase yield, and boost income. 
This AI-driven assistant bridges the knowledge gap and brings smart farming to the grassroots. 

**Technology** – Use of IBM Cloud Lite services / IBM Granite is mandatory. 

---

## Features

* 🌦️ Weather forecasts for agricultural planning
* 🧾 Mandi rate lookup for common crops
* 🌱 Soil health and crop recommendation guidance
* 🐛 Pest control and fertilizer advice
* 💧 Irrigation recommendations
* 🌾 Seasonal crop suggestions
* 📚 Retrieval-Augmented Generation (RAG) for knowledge-based answers
* 🌐 Multilingual support through translation
* 🔧 REST API support for integration

---

## Technology Stack

* IBM watsonx.ai
* IBM Granite / Llama Models
* IBM Cloud Lite
* Python
* Flask
* LangChain
* ChromaDB
* HuggingFace Embeddings
* OpenWeatherMap API
* AgMarket/Data.gov API
* Retrieval-Augmented Generation (RAG)

---

## Architecture Overview

Farmer Query
↓
Translation Module
↓
Intent Detection
↓
Weather / Soil / Crop / Pest / Mandi Modules
↓
RAG Retrieval (ChromaDB)
↓
IBM watsonx.ai (Granite/Llama Model)
↓
Response Generation
↓
Smart Farming Recommendation

---

## IBM Cloud Components Used

### IBM watsonx.ai

Used for foundation model inference and intelligent response generation.

### IBM Granite / Llama Models

Used for natural language understanding, reasoning, and agricultural recommendation generation.

### IBM Cloud Lite

Provides a secure and scalable cloud environment for deploying and managing the Smart Farming AI Agent.

### IBM Model Inference

Enables seamless access to foundation models for processing farmer queries and generating responses.

---

## Quick Start

### 1. Clone the Repository

```bash
git clone <repo-url>
cd smart-farming-agent
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Create a .env File

```env
IBM_API_KEY=your_ibm_api_key
IBM_PROJECT_ID=your_ibm_project_id
IBM_URL=https://your_ibm_url
DATA_GOV_API_KEY=your_data_gov_api_key
WEATHER_API_KEY=your_openweathermap_api_key
VECTOR_DB_DIR=chroma_db
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

## API Endpoints

| Endpoint      | Description                   |
| ------------- | ----------------------------- |
| GET /         | Web Interface                 |
| GET /features | List of available features    |
| POST /api/ask | Ask farming-related questions |
| GET /health   | Health status check           |

### Example API Request

```bash
curl -X POST http://127.0.0.1:5000/api/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is the mandi price for tomatoes?"}'
```

---

## Supported Modules

### chatbot.py

Main assistant logic and response generation.

### translator.py

Handles multilingual query translation.

### weather.py

Provides weather forecast information.

### mandi_api.py

Retrieves mandi prices and crop market data.

### soil.py

Provides soil recommendations and crop suitability guidance.

### rag_retriever.py

Retrieves relevant agricultural information from ChromaDB.

### knowledge_base.py

Stores curated agricultural knowledge related to crops, fertilizers, irrigation, and pest control.

---

## Role of Agentic AI

Agentic AI enables the Smart Farming AI Agent to function as an intelligent agricultural advisor rather than a simple chatbot. It analyzes user queries, determines the required information source, retrieves relevant agricultural knowledge using RAG, and generates context-aware recommendations. By integrating weather data, market prices, soil guidance, crop recommendations, and pest management advice, the system helps farmers make informed decisions and improve productivity.

---

## Novelty and Uniqueness

* Combines weather forecasts, mandi prices, soil analysis, crop recommendations, and pest management in a single platform.
* Uses Retrieval-Augmented Generation (RAG) to improve response accuracy.
* Supports multilingual farmer interactions.
* Provides seasonal and location-aware recommendations.
* Integrates IBM watsonx.ai and Granite/Llama models for intelligent decision support.
* Uses fallback mechanisms for APIs and model services to improve reliability.

---

## Future Scope

* Voice-based farmer assistant in regional languages.
* Mobile application deployment.
* IoT sensor integration for real-time farm monitoring.
* Image-based crop disease detection.
* Smart irrigation automation.
* Yield prediction and analytics.
* Satellite and drone-based crop monitoring.

---

## Notes

* Uses local fallback mandi data when external APIs are unavailable.
* RAG functionality can be enabled or disabled through configuration.
* Configuration details are displayed during startup for debugging purposes.

---

## License

This project is developed for educational purposes and demonstrates the use of IBM watsonx.ai, Granite/Llama Models, LangChain, ChromaDB, and Retrieval-Augmented Generation (RAG) in smart agriculture applications.
