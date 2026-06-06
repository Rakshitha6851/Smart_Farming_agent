from knowledge_base import get_soil_crops

SOIL_INFORMATION = {
    "black": {
        "scientific_name": "Vertisols/Regosols",
        "region": "Central India (Deccan Plateau)",
        "characteristics": [
            "Deep and fertile soil (1-2 meters)",
            "High moisture retention capacity",
            "Rich in clay and iron compounds",
            "Good nutrient-holding capacity",
            "Cracks when dry, difficult to work when wet"
        ],
        "ph_range": "6.0-8.0",
        "water_holding": "High",
        "fertility": "High",
        "suitable_crops": ["cotton", "soybean", "sunflower", "groundnut", "chickpea", "wheat"],
        "fertilizer_needs": "Moderate nitrogen with balanced NPK",
        "challenges": "Waterlogging risk during monsoon, needs good drainage"
    },
    "red": {
        "scientific_name": "Laterite/Lateritic",
        "region": "South India and Eastern Ghats",
        "characteristics": [
            "Acidic in nature due to leaching",
            "Low in nitrogen and phosphorus",
            "Well-drained, light textured",
            "Low water retention",
            "Rich in iron and aluminum oxides"
        ],
        "ph_range": "4.5-6.0",
        "water_holding": "Low",
        "fertility": "Low to Medium",
        "suitable_crops": ["groundnut", "millet", "pulses", "vegetables", "fruits", "coconut"],
        "fertilizer_needs": "High organic matter, lime application, balanced NPK",
        "challenges": "Acidic, leaching of nutrients, needs organic matter"
    },
    "alluvial": {
        "scientific_name": "Fluvisols/Entisols",
        "region": "Indo-Gangetic Plains, river valleys",
        "characteristics": [
            "Transported by rivers and deposited",
            "Very fertile and productive",
            "Mixed texture (loamy)",
            "Good water holding capacity",
            "Rich in minerals and organic matter"
        ],
        "ph_range": "7.0-8.0",
        "water_holding": "Medium to High",
        "fertility": "Very High",
        "suitable_crops": ["rice", "wheat", "sugarcane", "vegetables", "pulses"],
        "fertilizer_needs": "Moderate nitrogen, balanced NPK",
        "challenges": "Subject to seasonal flooding, salinity in some areas"
    },
    "sandy": {
        "scientific_name": "Psamments/Desert Soils",
        "region": "Rajasthan, coastal areas, arid zones",
        "characteristics": [
            "Well-drained, coarse textured",
            "Low water retention",
            "Low organic matter",
            "Low nutrient content",
            "Prone to erosion and dust storms"
        ],
        "ph_range": "6.5-8.0",
        "water_holding": "Very Low",
        "fertility": "Low",
        "suitable_crops": ["groundnut", "pulses", "watermelon", "coconut", "millets"],
        "fertilizer_needs": "High organic matter, mulching essential, regular irrigation",
        "challenges": "High evaporation, low water holding, requires frequent irrigation"
    },
    "clay": {
        "scientific_name": "Vertisols",
        "region": "Parts of Central and South India",
        "characteristics": [
            "Heavy textured, high clay content",
            "Excellent water retention",
            "Poor drainage and aeration",
            "High fertility but difficult to work",
            "Forms hard cakes when dry"
        ],
        "ph_range": "7.0-8.5",
        "water_holding": "Very High",
        "fertility": "High",
        "suitable_crops": ["rice", "wheat", "cotton", "maize"],
        "fertilizer_needs": "Balanced NPK, needs good organic matter",
        "challenges": "Poor drainage, waterlogging, difficult workability"
    },
    "loamy": {
        "scientific_name": "Mollisols/Alfisols",
        "region": "Various regions across India",
        "characteristics": [
            "Ideal soil texture (balanced sand-silt-clay)",
            "Good water retention and drainage",
            "High organic matter potential",
            "Excellent for most crops",
            "Easy to work with"
        ],
        "ph_range": "6.0-7.5",
        "water_holding": "Medium",
        "fertility": "High",
        "suitable_crops": ["All crops", "vegetables", "cereals", "pulses", "oilseeds"],
        "fertilizer_needs": "Moderate NPK, responds well to organic matter",
        "challenges": "Subject to erosion, needs conservation"
    }
}

def soil_recommendation(soil):
    """Get detailed soil recommendations"""
    soil = soil.lower().strip().replace(" ", "")
    
    if soil in SOIL_INFORMATION:
        info = SOIL_INFORMATION[soil]
        crops = info.get("suitable_crops", [])
        
        response = f"""
🌱 SOIL INFORMATION: {soil.upper()} SOIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scientific Name: {info['scientific_name']}
Region: {info['region']}

📊 Properties:
• pH Range: {info['ph_range']}
• Water Holding Capacity: {info['water_holding']}
• Fertility Level: {info['fertility']}

🌾 Characteristics:
"""
        for char in info['characteristics']:
            response += f"  • {char}\n"
        
        response += f"""
✅ Suitable Crops:
{', '.join(crops)}

🧪 Fertilizer Needs:
{info['fertilizer_needs']}

⚠️ Challenges:
{info['challenges']}

💡 Recommendation:
For {soil} soil, prioritize:
1. {crops[0] if crops else 'Consult local agronomist'}
2. Soil testing before fertilizer application
3. {info['fertilizer_needs'].lower()}
"""
        return response
    
    # If soil type not found, suggest similar
    available = list(SOIL_INFORMATION.keys())
    return f"Soil type '{soil}' not recognized. Available: {', '.join(available)}"

def get_soil_health_tips(soil_type):
    """Get tips to improve soil health"""
    soil_type = soil_type.lower().strip()
    
    general_tips = [
        "Add organic matter (compost/manure) annually",
        "Perform soil testing every 2 years",
        "Practice crop rotation",
        "Avoid monocropping",
        "Use green manuring",
        "Minimize chemical pesticides",
        "Maintain proper pH level",
        "Ensure good drainage"
    ]
    
    if soil_type == "sandy":
        return [
            "Add 5-10 tons compost/manure per hectare",
            "Use mulching extensively",
            "Increase organic matter content",
            "Install drip irrigation system",
            "Grow cover crops to prevent erosion"
        ]
    elif soil_type in ["clay", "black"]:
        tips = [
            "Improve drainage with raised beds",
            "Add sand/organic matter to reduce waterlogging",
            "Use vermiculture",
            "Plant deep-rooted crops for aeration",
            "Avoid working soil when wet"
        ]
    elif soil_type == "red":
        tips = [
            "Add lime to reduce acidity",
            "Increase organic matter significantly",
            "Use balanced fertilizers",
            "Avoid excessive nitrogen",
            "Practice mulching"
        ]
    else:
        tips = general_tips

    return "🧑‍🌾 SOIL HEALTH TIPS:\n" + "\n".join(f"• {tip}" for tip in tips)
