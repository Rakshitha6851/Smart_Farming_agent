"""
Comprehensive Agricultural Knowledge Base for Smart Farming Agent
Contains curated agricultural data for Indian farming conditions
"""

# Pest Control Measures
PEST_CONTROL = {
    "aphids": {
        "crops_affected": ["cotton", "groundnut", "pulses", "vegetables"],
        "symptoms": "Small insects clustering on leaves, yellowing, sticky residue",
        "organic_control": [
            "Spray neem oil (3% solution) every 10-15 days",
            "Use insecticidal soap",
            "Release ladybugs (natural predators)",
            "Spray water to dislodge insects"
        ],
        "chemical_control": [
            "Imidacloprid 17.8% SL",
            "Dimethoate 30% EC",
            "Acephate 75% SP"
        ],
        "prevention": [
            "Use resistant varieties",
            "Maintain field hygiene",
            "Avoid excess nitrogen fertilizer",
            "Remove infected plants early"
        ]
    },
    "whiteflies": {
        "crops_affected": ["cotton", "okra", "eggplant", "tomato"],
        "symptoms": "White insects on leaf undersides, yellowing leaves, sticky substance",
        "organic_control": [
            "Yellow sticky traps",
            "Spray neem oil regularly",
            "Use reflective mulch to confuse insects",
            "Parasitic wasps (Encarsia formosa)"
        ],
        "chemical_control": [
            "Thiamethoxam 25% WG",
            "Imidacloprid 17.8% SL"
        ],
        "prevention": [
            "Remove infected plants",
            "Crop rotation",
            "Use seed treatment"
        ]
    },
    "armyworms": {
        "crops_affected": ["maize", "sorghum", "rice", "groundnut"],
        "symptoms": "Leaf damage, bore holes in crops, presence of dark-colored caterpillars",
        "organic_control": [
            "Hand-picking affected leaves",
            "Spray Bacillus thuringiensis (Bt) every 7 days",
            "Use pheromone traps",
            "Encourage natural parasites"
        ],
        "chemical_control": [
            "Chlorpyrifos 20% EC",
            "Cypermethrin 10% EC",
            "Spinosad 45% SC"
        ],
        "prevention": [
            "Deep plowing in off-season",
            "Crop rotation",
            "Intercropping with marigold/sunflower"
        ]
    },
    "bollworms": {
        "crops_affected": ["cotton"],
        "symptoms": "Holes in bolls, caterpillars inside cotton bolls, reduced yield",
        "organic_control": [
            "Bt cotton varieties",
            "Hand-picking affected bolls",
            "Neem spray (3%) at flower initiation",
            "Pheromone traps"
        ],
        "chemical_control": [
            "Emamectin benzoate 5% SG",
            "Flubendiamide 20% WDG"
        ],
        "prevention": [
            "Use Bt hybrid seeds",
            "Proper sanitation",
            "Timely picking"
        ]
    },
    "leaf_spot": {
        "crops_affected": ["rice", "wheat", "pulses", "vegetables"],
        "symptoms": "Brown/dark spots on leaves, premature leaf fall",
        "organic_control": [
            "Spray Bordeaux mixture (1%) every 15 days",
            "Use resistant varieties",
            "Remove infected leaves",
            "Improve air circulation"
        ],
        "chemical_control": [
            "Mancozeb 75% WP",
            "Carbendazim 50% WP"
        ],
        "prevention": [
            "Avoid overhead irrigation",
            "Proper crop spacing",
            "Crop rotation"
        ]
    }
}

# Fertilizer Recommendations
FERTILIZER_RECOMMENDATIONS = {
    "rice": {
        "npk_ratio": "120:60:40",
        "organic": {
            "farmyard_manure": "10-15 tons/hectare before planting",
            "compost": "5-7 tons/hectare",
            "green_manure": "Incorporate legume crop"
        },
        "inorganic": {
            "urea": "120 kg/hectare (split: 40-40-40)",
            "dap": "50 kg/hectare",
            "mop": "40 kg/hectare"
        },
        "timing": ["Before transplanting", "At tilering (40 DAS)", "At panicle initiation (60 DAS)"],
        "deficiency_signs": {
            "nitrogen": "Yellow leaves from bottom",
            "phosphorus": "Purple/reddish discoloration",
            "potassium": "Brown spots on leaf edges"
        }
    },
    "wheat": {
        "npk_ratio": "100:50:50",
        "organic": {
            "farmyard_manure": "8-10 tons/hectare",
            "compost": "5 tons/hectare",
            "crop_residue": "Incorporate previous crop residue"
        },
        "inorganic": {
            "urea": "100 kg/hectare (split: 50-50)",
            "dap": "50 kg/hectare at sowing",
            "mop": "50 kg/hectare"
        },
        "timing": ["At sowing", "30 DAS (Tillering)", "60 DAS (Flag leaf)"],
        "deficiency_signs": {
            "nitrogen": "Pale yellow leaves",
            "phosphorus": "Reduced tillering",
            "potassium": "Drought susceptibility"
        }
    },
    "cotton": {
        "npk_ratio": "150:80:60",
        "organic": {
            "farmyard_manure": "10-12 tons/hectare",
            "oil_cakes": "2-3 tons/hectare (neem/castor)",
            "vermicompost": "3-5 tons/hectare"
        },
        "inorganic": {
            "urea": "150 kg/hectare (3-4 splits)",
            "dap": "80 kg/hectare",
            "mop": "60 kg/hectare"
        },
        "timing": ["Before sowing", "At flowering", "At boll formation"],
        "deficiency_signs": {
            "nitrogen": "Light green foliage",
            "phosphorus": "Poor root development",
            "potassium": "Boll shedding"
        }
    },
    "maize": {
        "npk_ratio": "120:60:40",
        "organic": {
            "farmyard_manure": "10-15 tons/hectare",
            "compost": "5-7 tons/hectare"
        },
        "inorganic": {
            "urea": "120 kg/hectare (split: 50-70)",
            "dap": "60 kg/hectare",
            "mop": "40 kg/hectare"
        },
        "timing": ["At planting (basal)", "At 30 DAS (V4-V5 stage)"],
        "deficiency_signs": {
            "nitrogen": "Early purple discoloration",
            "phosphorus": "Stunted growth",
            "potassium": "Marginal scorch"
        }
    },
    "pulses": {
        "npk_ratio": "25:50:25",
        "organic": {
            "farmyard_manure": "5-7 tons/hectare",
            "compost": "3-5 tons/hectare"
        },
        "inorganic": {
            "dap": "50 kg/hectare",
            "mop": "25 kg/hectare",
            "note": "Low nitrogen due to nitrogen fixation"
        },
        "timing": ["At sowing (full DAP)", "Optional top dressing at flowering"],
        "deficiency_signs": {
            "phosphorus": "Poor root nodule formation",
            "potassium": "Pods not filled properly"
        }
    }
}

# Irrigation Guidelines
IRRIGATION_GUIDELINES = {
    "rice": {
        "water_requirement": "1000-1500 mm per season",
        "irrigation_interval": "Every 7-10 days during growing season",
        "depth": "5-10 cm standing water throughout season",
        "critical_stages": ["Nursery", "Transplanting (first 30 days)", "Flowering"],
        "method": "Flooding or drip in case of water scarcity",
        "conservation_tips": [
            "Use drip irrigation to save 30-40% water",
            "Mulching with straw",
            "Alternate wetting and drying (AWD)"
        ]
    },
    "wheat": {
        "water_requirement": "400-500 mm per season",
        "irrigation_interval": "Every 20-30 days in winter",
        "number_of_irrigations": "3-4 times",
        "critical_stages": ["Crown root initiation (21 DAS)", "Tillering (40-45 DAS)", "Grain filling (70-75 DAS)"],
        "method": "Flood or sprinkler irrigation",
        "conservation_tips": [
            "Deficit irrigation in winter",
            "Mulching reduces water loss",
            "Drip irrigation suitable in dry zones"
        ]
    },
    "cotton": {
        "water_requirement": "600-900 mm per season",
        "irrigation_interval": "10-15 days in summer",
        "critical_stages": ["Flowering", "Boll development", "Boll maturation"],
        "method": "Drip irrigation preferred",
        "conservation_tips": [
            "Drip reduces water by 40-50%",
            "Mulching maintains soil moisture",
            "Avoid irrigation 2 weeks before harvest"
        ]
    },
    "maize": {
        "water_requirement": "500-800 mm per season",
        "irrigation_interval": "8-12 days during growing season",
        "critical_stages": ["V4-V6 (Early growth)", "Tasseling", "Silking"],
        "method": "Sprinkler or drip irrigation",
        "conservation_tips": [
            "Use soil moisture sensors",
            "Mulching reduces evaporation",
            "Drip irrigation saves 25-30% water"
        ]
    },
    "vegetables": {
        "water_requirement": "300-600 mm per season (varies by crop)",
        "irrigation_interval": "Every 3-5 days in summer",
        "method": "Drip irrigation highly recommended",
        "critical_stages": ["Seedling establishment", "Flowering", "Fruiting"],
        "conservation_tips": [
            "Drip irrigation most efficient",
            "Morning irrigation reduces disease",
            "Mulching is essential",
            "Avoid waterlogging"
        ]
    },
    "pulses": {
        "water_requirement": "350-550 mm per season (varies by pulse crop)",
        "irrigation_interval": "Every 10-15 days (as per soil moisture)",
        "method": "Sprinkler or drip (avoid waterlogging)",
        "critical_stages": ["Sowing/seedling establishment", "Flowering", "Pod filling"],
        "conservation_tips": [
            "Mulching to reduce evaporation",
            "Irrigate based on soil moisture rather than fixed schedule",
            "Use improved drainage to prevent root diseases"
        ]
    }
}

# Crop Recommendations by Season
SEASONAL_CROP_RECOMMENDATIONS = {
    "kharif": {  # Monsoon/Summer crops
        "suitable_crops": ["rice", "maize", "cotton", "groundnut", "soybean", "pulses"],
        "season_months": "June-September",
        "rainfall_needed": "800-1200 mm",
        "crops": {
            "rice": "Suitable for high rainfall regions",
            "maize": "Early maize variety recommended",
            "cotton": "Bt cotton preferred",
            "groundnut": "Oil seeds for dry regions",
            "soybean": "Alternate to cotton"
        }
    },
    "rabi": {  # Winter crops
        "suitable_crops": ["wheat", "rice", "pulses", "oilseeds", "vegetables"],
        "season_months": "October-March",
        "rainfall_needed": "400-600 mm (or irrigation)",
        "crops": {
            "wheat": "Major crop in north India",
            "rice": "Winter rice in coastal regions",
            "pulses": "Chickpea, lentil, pea",
            "mustard": "Oil seed crop",
            "vegetables": "Tomato, onion, cabbage, cauliflower"
        }
    },
    "summer": {  # Dry season - limited crops
        "suitable_crops": ["vegetables", "pulses", "oilseeds"],
        "season_months": "March-May",
        "rainfall_needed": "Depends on irrigation",
        "crops": {
            "vegetables": "Tomato, eggplant, beans with irrigation",
            "groundnut": "Summer groundnut with irrigation",
            "maize": "Early maize"
        }
    }
}

# Crop Recommendations by Soil Type
CROP_BY_SOIL = {
    "black_soil": {
        "region": "Central India",
        "suitable_crops": ["cotton", "soybean", "groundnut", "sunflower", "wheat", "chickpea"],
        "characteristics": "Deep, fertile, moisture-retentive",
        "fertilizer_requirement": "High nitrogen due to good holding capacity"
    },
    "red_soil": {
        "region": "South India, Eastern Ghats",
        "suitable_crops": ["groundnut", "millet", "pulses", "vegetables", "fruits"],
        "characteristics": "Low fertility, well-drained, acidic",
        "fertilizer_requirement": "Higher organic matter and lime application needed"
    },
    "alluvial_soil": {
        "region": "Indo-Gangetic Plains",
        "suitable_crops": ["rice", "wheat", "sugarcane", "vegetables"],
        "characteristics": "Very fertile, good water holding capacity",
        "fertilizer_requirement": "Moderate nitrogen with balanced NPK"
    },
    "sandy_soil": {
        "region": "Rajasthan, coastal areas",
        "suitable_crops": ["groundnut", "watermelon", "coconut", "pulses"],
        "characteristics": "Well-drained, low water holding, low fertility",
        "fertilizer_requirement": "High organic matter, regular irrigation needed"
    },
    "laterite_soil": {
        "region": "Western coastal regions",
        "suitable_crops": ["coconut", "arecanut", "spices", "vegetables"],
        "characteristics": "High iron/aluminum oxide, low fertility",
        "fertilizer_requirement": "High organic matter and balanced nutrients"
    }
}

# Crop Recommendations by Region (Indian States)
CROP_BY_REGION = {
    "punjab": {
        "crops": ["wheat", "rice", "cotton", "vegetables"],
        "kharif": "Rice, cotton, pulses",
        "rabi": "Wheat, mustard, chickpea"
    },
    "uttar_pradesh": {
        "crops": ["wheat", "rice", "sugarcane", "pulses", "vegetables"],
        "kharif": "Rice, maize, cotton",
        "rabi": "Wheat, lentil, chickpea"
    },
    "maharashtra": {
        "crops": ["cotton", "groundnut", "sugarcane", "onion"],
        "kharif": "Cotton, groundnut, soybean",
        "rabi": "Chickpea, wheat, vegetables"
    },
    "madhya_pradesh": {
        "crops": ["cotton", "soybean", "groundnut", "pulses"],
        "kharif": "Cotton, soybean",
        "rabi": "Wheat, chickpea, mustard"
    },
    "karnataka": {
        "crops": ["cotton", "sugarcane", "groundnut", "vegetables"],
        "kharif": "Cotton, maize",
        "rabi": "Groundnut, sunflower, pulses"
    },
    "andhra_pradesh": {
        "crops": ["rice", "groundnut", "sugarcane", "vegetables"],
        "kharif": "Rice, groundnut, maize",
        "rabi": "Rice, groundnut, pulses"
    },
    "tamil_nadu": {
        "crops": ["rice", "sugarcane", "groundnut", "vegetables"],
        "kharif": "Rice, maize",
        "rabi": "Rice, groundnut, pulses"
    }
}

def get_pest_control_info(pest_name):
    """Get detailed pest control information"""
    pest_name = pest_name.lower().replace(" ", "_")
    if pest_name in PEST_CONTROL:
        return PEST_CONTROL[pest_name]
    return None

def get_fertilizer_info(crop_name):
    """Get fertilizer recommendations for a crop"""
    crop_name = crop_name.lower()
    if crop_name in FERTILIZER_RECOMMENDATIONS:
        return FERTILIZER_RECOMMENDATIONS[crop_name]
    return None

def get_irrigation_info(crop_name):
    """Get irrigation guidelines for a crop"""
    crop_name = crop_name.lower()
    if crop_name in IRRIGATION_GUIDELINES:
        return IRRIGATION_GUIDELINES[crop_name]
    return None

def get_seasonal_crops(season):
    """Get crops recommended for a season"""
    season = season.lower()
    if season in SEASONAL_CROP_RECOMMENDATIONS:
        return SEASONAL_CROP_RECOMMENDATIONS[season]
    return None

def get_regional_crops(region):
    """Get crops recommended for a region"""
    region = region.lower().replace(" ", "_")
    if region in CROP_BY_REGION:
        return CROP_BY_REGION[region]
    return None

def get_soil_crops(soil_type):
    """Get crops suitable for soil type"""
    soil_type = soil_type.lower().replace(" ", "_")
    if soil_type in CROP_BY_SOIL:
        return CROP_BY_SOIL[soil_type]
    return None
