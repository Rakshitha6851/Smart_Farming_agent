"""
Smart Farming AI Agent - Main Chatbot Logic
IBM Granite + RAG + Weather + Soil + Mandi
"""

from datetime import datetime
import logging
import re

from weather import get_weather
from mandi_api import get_mandi_price, list_available_crops
from translator import translate_to_english
from soil import soil_recommendation, get_soil_health_tips
from rag_retriever import get_farming_advice

from ibm_watsonx_ai.foundation_models import ModelInference
from config import IBM_CREDENTIALS, IBM_MODEL_ID


# ==========================================
# LOGGING
# ==========================================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ==========================================
# SEASON DETECTION
# ==========================================

def get_current_season():
    month = datetime.now().month

    if month in [6, 7, 8, 9]:
        return "kharif (monsoon season)"
    elif month in [10, 11, 12, 1]:
        return "rabi (winter season)"
    else:
        return "summer season"


# ==========================================
# IBM WATSONX MODEL
# ==========================================

logger.info(f"Loading IBM Model: {IBM_MODEL_ID}")

try:
    model = ModelInference(
        model_id=IBM_MODEL_ID,
        credentials=IBM_CREDENTIALS,
        project_id=IBM_CREDENTIALS["project_id"]
    )
    logger.info("IBM Granite initialized successfully")

except Exception as e:
    logger.error(f"IBM Granite Error: {e}")

    try:
        model = ModelInference(
            model_id="meta-llama/llama-3-3-70b-instruct",
            credentials=IBM_CREDENTIALS,
            project_id=IBM_CREDENTIALS["project_id"]
        )
        logger.info("Fallback Llama model initialized")

    except Exception as e:
        logger.error(f"Fallback model failed: {e}")
        model = None


# ==========================================
# MAIN CHATBOT FUNCTION
# ==========================================

def ask_ai(question):

    try:
        original_question = question
        question = translate_to_english(question)

        logger.info(f"{original_question} -> {question}")

        q = question.lower()

        # =====================================
        # WEATHER
        # =====================================

        if any(word in q for word in [
            "weather",
            "temperature",
            "forecast",
            "will it rain",
            "rain today",
            "rain tomorrow"
        ]):

            city = None

            if " in " in q:
                city = q.split(" in ")[-1].strip("?.!, ")
            else:
                last = question.split()[-1].strip("?.!,")
                if last.isalpha() and len(last) > 2:
                    city = last

            return get_weather(city)

        # =====================================
        # MANDI PRICE
        # =====================================

        if any(word in q for word in ["price", "mandi", "market"]):

            words = question.split()

            for word in words:
                crop = word.strip("?.!,").lower()

                if crop in [
                    "price",
                    "market",
                    "mandi",
                    "what",
                    "is",
                    "the",
                    "of"
                ]:
                    continue

                result = get_mandi_price(crop)

                if "Commodity:" in str(result):
                    return result

            return (
                "No mandi data found.\n\n"
                f"Available crops: {list_available_crops()}"
            )

        # =====================================
        # SOIL
        # =====================================

        if "soil" in q:

            soil_types = [
                "black",
                "red",
                "sandy",
                "clay",
                "alluvial",
                "loamy"
            ]

            for soil_type in soil_types:
                if soil_type in q:
                    return soil_recommendation(soil_type)

            return get_soil_health_tips("general")

        # =====================================
        # RAG / KNOWLEDGE BASE
        # =====================================

        rag_context = get_farming_advice(question)

        # Sanitize retrieved context to avoid embedded Q/A examples
        # that can cause the model to continue example datasets.
        if rag_context:
            # remove lines that look like Q: / A: / Question: / Answer:
            rag_context = re.sub(r"(?im)^\s*(q:|a:|question:|answer:)\s.*$", "", rag_context)
            # collapse multiple blank lines
            rag_context = re.sub(r"\n{2,}", "\n\n", rag_context).strip()

        # If KB already has answer, return directly
        if rag_context:

            keywords = [
                "PEST CONTROL GUIDE",
                "FERTILIZER RECOMMENDATIONS",
                "IRRIGATION GUIDELINES",
                "CROP RECOMMENDATIONS",
                "RELEVANT KNOWLEDGE BASE"
            ]

            if any(k in rag_context for k in keywords):
                return rag_context

        # =====================================
        # AI RESPONSE
        # =====================================

        if model:

            season_info = get_current_season()

            prompt = f"""
You are Smart Farming AI Assistant.

CURRENT SEASON:
{season_info}

RULES:
1. Use only provided information.
2. If supporting knowledge exists, use it.
3. Do not invent facts.
4. Give concise answers.
5. Focus on Indian farming.
6. If the supporting knowledge contains example Q/A pairs or dataset entries, DO NOT continue or create new Q/A examples—answer only the user's Question below.
7. Ignore any 'Question:' or 'Answer:' labels inside the supporting knowledge; those are examples only.

Supporting Knowledge:
{rag_context if rag_context else "No supporting knowledge found."}

Question:
{question}

Answer:
"""

            response = model.generate_text(
                prompt=prompt,
                params={
                    "max_new_tokens": 300,
                    "temperature": 0.2
                }
            )

            if isinstance(response, dict):
                if "results" in response:
                    answer = response["results"][0].get(
                        "generated_text",
                        ""
                    )
                else:
                    answer = str(response)

            elif isinstance(response, list):
                answer = "\n".join(str(x) for x in response)

            else:
                answer = str(response)

            answer = (
                answer.replace("# Response:", "")
                .replace("**", "")
                .strip()
            )

            return answer

        # =====================================
        # FALLBACK
        # =====================================

        if rag_context:
            return rag_context

        return (
            "Unable to generate answer. "
            "Please try another farming question."
        )

    except Exception as e:
        logger.error(f"Chatbot Error: {e}")
        return f"Error: {str(e)}"


# ==========================================
# FEATURES LIST
# ==========================================

def get_available_features():

    return """
🌾 Smart Farming AI Agent

Weather Information
Example: Weather in Bangalore

Mandi Prices
Example: Tomato price

Soil Recommendations
Example: Best crops for black soil

Fertilizer Guidance
Example: Fertilizer for paddy

Pest Control
Example: Control aphids in tomato

Irrigation Advice
Example: Water requirement for rice

Crop Recommendations
Example: Best crop for kharif season

AI Farming Guidance
Example: How to increase crop yield
"""