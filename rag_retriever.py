"""
RAG Engine - Retrieval Augmented Generation for Smart Farming
Integrates Chroma vector database with LangChain for knowledge retrieval
"""

import os
from config import ENABLE_RAG, VECTOR_DB_DIR, EMBEDDING_MODEL
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from knowledge_base import (
    get_pest_control_info,
    get_fertilizer_info,
    get_irrigation_info,
    get_seasonal_crops,
    get_regional_crops,
    get_soil_crops
)

VECTOR_DIR = VECTOR_DB_DIR


def initialize_vector_db():
    """Initialize the vector database connection."""
    if not ENABLE_RAG:
        print("RAG is disabled by configuration.")
        return None

    try:
        embedding = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        if not os.path.isdir(VECTOR_DIR) or not os.listdir(VECTOR_DIR):
            print(f"Vector DB not found or empty at '{VECTOR_DIR}'. Run rag_engine.py first.")
            return None

        vector_db = Chroma(
            persist_directory=VECTOR_DIR,
            embedding_function=embedding
        )
        return vector_db
    except Exception as e:
        print(f"Vector DB initialization error: {e}")
        return None

def retrieve_agricultural_knowledge(query, k=3):
    """
    Retrieve relevant agricultural knowledge from vector database
    
    Args:
        query: User question
        k: Number of results to retrieve
    
    Returns:
        Retrieved documents relevant to query
    """
    try:
        vector_db = initialize_vector_db()
        if vector_db is None:
            return []
        
        # Similarity search in vector database
        results = vector_db.similarity_search(query, k=k)
        return results
    except Exception as e:
        print(f"RAG retrieval error: {e}")
        return []

def format_rag_context(retrieved_docs):
    """Format retrieved documents into readable context"""
    if not retrieved_docs:
        return ""
    
    context = "📚 RELEVANT KNOWLEDGE BASE:\n━━━━━━━━━━━━━━━━━━━━━━\n"
    for i, doc in enumerate(retrieved_docs, 1):
        context += f"\n{i}. {doc.page_content[:200]}...\n"
    
    return context

def get_farming_advice(question):
    """
    Get supporting context using RAG and knowledge base
    Combines vector DB retrieval with domain knowledge
    """
    
    # First, check if question relates to specific farming domains
    q_lower = question.lower()
    
    # Pest Control
    if ("pest" in q_lower or "insect" in q_lower or "disease" in q_lower or "aphids" in q_lower or "whiteflies" in q_lower or "armyworms" in q_lower or "bollworms" in q_lower or "leaf spot" in q_lower):
        
        
        
        
        
        
        
        
        
        for pest in ["aphids", "whiteflies", "armyworms", "bollworms", "leaf_spot"]:
            if pest.replace("_", " ") in q_lower or pest.replace("_", "") in q_lower:
                pest_info = get_pest_control_info(pest)
                if pest_info:
                    return format_pest_control(pest_info)
        return ""
    
    # Fertilizer
    if "fertilizer" in q_lower or "manure" in q_lower or "nutrient" in q_lower:
        crops = ["rice", "wheat", "cotton", "maize", "pulses"]
        for crop in crops:
            if crop in q_lower:
                fert_info = get_fertilizer_info(crop)
                if fert_info:
                    return format_fertilizer_advice(crop, fert_info)
        return ""
    
    # Irrigation
    if "irrigation" in q_lower or "water" in q_lower or "watering" in q_lower:
        crops = ["rice", "wheat", "cotton", "maize", "vegetables"]
        for crop in crops:
            if crop in q_lower:
                irr_info = get_irrigation_info(crop)
                if irr_info:
                    return format_irrigation_advice(crop, irr_info)
        return ""
    
    # Crop Recommendation
    # Broaden detection to capture queries like "which crop gives highest yield in rainy season"
    if "crop" in q_lower and (any(word in q_lower for word in ["recommend", "suggest", "best", "which", "highest", "yield"]) or "season" in q_lower or "rainy" in q_lower):
        if "season" in q_lower or "rainy" in q_lower:
            for season in ["kharif", "rabi", "summer", "rainy"]:
                # treat 'rainy' as alias for 'kharif' where applicable
                check_season = 'kharif' if season == 'rainy' else season
                if season in q_lower or check_season in q_lower:
                    crops = get_seasonal_crops(check_season)
                    if crops:
                        return format_crop_recommendation(check_season, crops)

        if "region" in q_lower or "state" in q_lower:
            for region in ["punjab", "uttar_pradesh", "maharashtra", "madhya_pradesh"]:
                if region.replace("_", " ") in q_lower or region in q_lower:
                    crops = get_regional_crops(region)
                    if crops:
                        return format_regional_recommendation(region, crops)

        # If no specific season/region found but question asks for 'which' or 'highest yield', return general seasonal recommendation
        if any(word in q_lower for word in ["which", "highest", "yield"]):
            crops = get_seasonal_crops("kharif")
            if crops:
                return format_crop_recommendation("kharif", crops)

        return ""
    
    # Try RAG retrieval
    retrieved = retrieve_agricultural_knowledge(question)
    if retrieved:
        return format_rag_context(retrieved)

    # General fallback for crop/season questions when RAG or AI is unavailable
    fallback = get_general_crop_advice(q_lower)
    if fallback:
        return fallback

    return None


def get_general_crop_advice(q_lower):
    """Return a generic crop recommendation when no RAG context is found."""
    if "crop" not in q_lower and "yield" not in q_lower and "season" not in q_lower and "rainy" not in q_lower:
        return ""

    # Prefer explicit season keywords; otherwise map rainy/season queries to Kharif.
    if "rabi" in q_lower:
        season = "rabi"
    elif "summer" in q_lower:
        season = "summer"
    elif "rainy" in q_lower or "monsoon" in q_lower or "kharif" in q_lower or "season" in q_lower:
        season = "kharif"
    else:
        season = "kharif"

    crops = get_seasonal_crops(season)
    if crops:
        return format_crop_recommendation(season, crops)

    return ""


def format_pest_control(pest_info):
    """Format pest control information"""
    response = f"""
🐛 PEST CONTROL GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Affected Crops: {', '.join(pest_info['crops_affected'])}
Symptoms: {pest_info['symptoms']}

🌿 ORGANIC CONTROL:
"""
    for method in pest_info['organic_control']:
        response += f"  • {method}\n"
    
    response += f"""
🧪 CHEMICAL CONTROL:
"""
    for chemical in pest_info['chemical_control']:
        response += f"  • {chemical}\n"
    
    response += f"""
🛡️ PREVENTION:
"""
    for prev in pest_info['prevention']:
        response += f"  • {prev}\n"
    
    return response

def format_fertilizer_advice(crop, fert_info):
    """Format fertilizer recommendations"""
    response = f"""
🧪 FERTILIZER RECOMMENDATIONS: {crop.upper()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NPK Ratio: {fert_info['npk_ratio']}

🌾 ORGANIC FERTILIZERS:
"""
    for name, amount in fert_info['organic'].items():
        response += f"  • {name.replace('_', ' ').title()}: {amount}\n"
    
    response += f"""
🔬 INORGANIC FERTILIZERS:
"""
    for name, amount in fert_info['inorganic'].items():
        response += f"  • {name.upper()}: {amount}\n"
    
    response += f"""
⏰ APPLICATION TIMING:
"""
    for timing in fert_info['timing']:
        response += f"  • {timing}\n"
    
    response += f"""
⚠️ DEFICIENCY SIGNS:
"""
    for nutrient, sign in fert_info['deficiency_signs'].items():
        response += f"  • {nutrient.title()}: {sign}\n"
    
    return response

def format_irrigation_advice(crop, irr_info):
    """Format irrigation guidelines"""
    response = f"""
💧 IRRIGATION GUIDELINES: {crop.upper()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Water Requirement: {irr_info['water_requirement']}
Irrigation Interval: {irr_info['irrigation_interval']}
"""
    
    if 'depth' in irr_info:
        response += f"Water Depth: {irr_info['depth']}\n"
    
    response += f"""
🎯 CRITICAL GROWTH STAGES:
"""
    for stage in irr_info['critical_stages']:
        response += f"  • {stage}\n"
    
    response += f"""
💧 RECOMMENDED METHOD:
{irr_info['method']}

💡 WATER CONSERVATION TIPS:
"""
    for tip in irr_info['conservation_tips']:
        response += f"  • {tip}\n"
    
    return response

def format_crop_recommendation(season, crops_data):
    """Format seasonal crop recommendations"""
    response = f"""
🌾 CROP RECOMMENDATIONS: {season.upper()} SEASON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Season Duration: {crops_data['season_months']}
Required Rainfall: {crops_data['rainfall_needed']}

✅ Suitable Crops:
"""
    for crop in crops_data['suitable_crops']:
        response += f"  • {crop.capitalize()}\n"
    
    response += f"""
📝 CROP DETAILS:
"""
    for crop, detail in crops_data['crops'].items():
        response += f"  • {crop.capitalize()}: {detail}\n"
    
    return response

def format_regional_recommendation(region, crops_data):
    """Format regional crop recommendations"""
    response = f"""
🌍 CROP RECOMMENDATIONS: {region.replace('_', ' ').upper()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Main Crops: {', '.join(crops_data['crops'])}

🌾 KHARIF (Monsoon) Crops:
{crops_data['kharif']}

🌾 RABI (Winter) Crops:
{crops_data['rabi']}
"""
    return response
