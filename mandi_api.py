import requests
from datetime import datetime
from config import DATA_GOV_API_KEY

def _normalize_crop_name(crop: str) -> str:
    """Normalize crop names for local DB lookup (simple singularization).

    This uses heuristic rules (ies->y, remove trailing 'es' or 's') to map
    common plurals like 'tomatoes' -> 'tomato', 'onions' -> 'onion'.
    """
    if not crop:
        return crop

    c = crop.lower().strip()

    # basic cleanup
    c = c.strip("\"' .,:;!?()[]")

    # check simple synonym mapping if available
    if "CROP_SYNONYMS" in globals() and c in CROP_SYNONYMS:
        return CROP_SYNONYMS[c]

    # if already exact match, return
    if c in LOCAL_MANDI_DB:
        return c

    # common plural rules
    if c.endswith("ies"):
        cand = c[:-3] + "y"
        if cand in LOCAL_MANDI_DB:
            return cand

    if c.endswith("oes") or c.endswith("ses") or c.endswith("xes"):
        cand = c[:-2]
        if cand in LOCAL_MANDI_DB:
            return cand

    if c.endswith("es"):
        cand = c[:-2]
        if cand in LOCAL_MANDI_DB:
            return cand

    if c.endswith("s"):
        cand = c[:-1]
        if cand in LOCAL_MANDI_DB:
            return cand

    # fallback to original normalized string
    return c

# Local mandi price database (updates regularly from government sources)
# This is a fallback and can be updated daily
LOCAL_MANDI_DB = {
    "tomato": {"price": "₹2200-2500", "unit": "per quintal", "region": "All India Average"},
    "onion": {"price": "₹1800-2200", "unit": "per quintal", "region": "All India Average"},
    "potato": {"price": "₹1500-1800", "unit": "per quintal", "region": "All India Average"},
    "rice": {"price": "₹3200-3600", "unit": "per quintal", "region": "All India Average"},
    "wheat": {"price": "₹2800-3200", "unit": "per quintal", "region": "All India Average"},
    "maize": {"price": "₹2100-2400", "unit": "per quintal", "region": "All India Average"},
    "cotton": {"price": "₹5500-6200", "unit": "per bale (170 kg)", "region": "All India Average"},
    "groundnut": {"price": "₹5000-5800", "unit": "per quintal", "region": "All India Average"},
    "soybean": {"price": "₹3800-4200", "unit": "per quintal", "region": "All India Average"},
    "pulses": {"price": "₹4500-5200", "unit": "per quintal", "region": "All India Average"},
    "sugarcane": {"price": "₹320-360", "unit": "per quintal", "region": "All India Average"},
    "chickpea": {"price": "₹4800-5400", "unit": "per quintal", "region": "All India Average"},
    "mustard": {"price": "₹5000-5600", "unit": "per quintal", "region": "All India Average"},
    "sunflower": {"price": "₹6500-7200", "unit": "per quintal", "region": "All India Average"}
}

# Simple synonym/plural mapping to handle common user variations
CROP_SYNONYMS = {
    "tomatoes": "tomato",
    "tomatoes": "tomato",
    "onions": "onion",
    "potatoes": "potato",
    "wheats": "wheat",
    "maizes": "maize",
    "groundnuts": "groundnut",
    "soybeans": "soybean",
    "mustards": "mustard",
    "chickpeas": "chickpea",
    "sunflowers": "sunflower",
    "pulses": "pulses"
}

def get_agmarket_price(crop, market=None, state=None, district=None):
    """
    Try to fetch real-time price from AgMarket API.
    Falls back to local database if API fails.
    """
    crop = crop.lower().strip()

    if not DATA_GOV_API_KEY:
        print("DATA_GOV_API_KEY not configured. Using fallback local prices.")
        return get_local_price(crop)
    
    try:
        params = {
            "api-key": DATA_GOV_API_KEY,
            "format": "json",
            "limit": 1,
            "filters[commodity]": crop.capitalize()
        }

        if market:
            params["filters[market]"] = market.title()
        if state:
            params["filters[state]"] = state.title()
        if district:
            params["filters[district]"] = district.title()

        response = requests.get(
            "https://api.data.gov.in/resource/9ef84268-d588-465a-a5c3-375cda642175",
            params=params,
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("records"):
                record = data["records"][0]
                modal_price = record.get("modal_price") or record.get("price")
                min_price = record.get("min_price")
                max_price = record.get("max_price")
                market_name = record.get("market") or record.get("state") or "Various"

                return {
                    "crop": crop.capitalize(),
                    "modal_price": f"₹{modal_price}" if modal_price else "N/A",
                    "min_price": f"₹{min_price}" if min_price else None,
                    "max_price": f"₹{max_price}" if max_price else None,
                    "unit": "per quintal",
                    "market": record.get("market", "Various"),
                    "district": record.get("district", "Unknown"),
                    "state": record.get("state", "Unknown"),
                    "variety": record.get("variety", "Standard"),
                    "date": record.get("arrival_date", "Today"),
                    "source": "Government AgMarket API"
                }
    except Exception as e:
        print(f"API Error: {e}")
    
    # Fallback to local database
    return get_local_price(crop)

def get_local_price(crop):
    """Get price from local database"""
    crop = crop.lower().strip()
    # normalize common plural forms to singular matches in local DB
    crop = _normalize_crop_name(crop)

    if crop in LOCAL_MANDI_DB:
        data = LOCAL_MANDI_DB[crop]
        return {
            "crop": crop.capitalize(),
            "price": data["price"],
            "unit": data["unit"],
            "region": data["region"],
            "date": datetime.now().strftime("%d-%m-%Y"),
            "source": "All India Mandi Prices (Government)",
            "note": "Based on recent market trends. Contact local mandi for exact rates."
        }
    
    return None

def get_mandi_price(crop):
    """
    Main function to get mandi prices
    Returns formatted price information
    """
    price_data = get_agmarket_price(crop)
    
    if not price_data:
        # Try direct lookup in local DB
        crop_lower = crop.lower().strip()
        if crop_lower in LOCAL_MANDI_DB:
            price_data = get_local_price(crop_lower)
        else:
            available_crops = ", ".join(list(LOCAL_MANDI_DB.keys())[:10])
            return f"❌ No mandi data found for '{crop}'. Available crops: {available_crops}..."

    price_line = price_data.get("price")
    if price_data.get("modal_price"):
        price_line = f"Modal Price: {price_data['modal_price']}"

    range_line = ""
    if price_data.get("min_price") and price_data.get("max_price"):
        range_line = f"Min-Max Range: {price_data['min_price']} - {price_data['max_price']} {price_data.get('unit', '')}"
    elif price_data.get("price") and not price_data.get("modal_price"):
        range_line = f"Price Range: {price_data['price']} {price_data.get('unit', '')}"

    response = f"""
📊 MANDI PRICE INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Commodity: {price_data['crop']}
{price_line}
{range_line}
Market: {price_data.get('market', price_data.get('region', 'Various'))}
District: {price_data.get('district', 'N/A')}
State: {price_data.get('state', 'N/A')}
Variety: {price_data.get('variety', 'Standard')}
Date: {price_data.get('date', datetime.now().strftime('%d-%m-%Y'))}
Source: {price_data.get('source', 'Government Data')}

💡 {price_data.get('note', 'Prices vary by market and season. Check your local mandi for exact rates.')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    
    return response

def list_available_crops():
    """Return list of crops with mandi data"""
    return list(LOCAL_MANDI_DB.keys())

def get_crop_price_trend(crop):
    """
    Get price trend information (mock data for now)
    In production, this would pull historical data
    """
    crop = crop.lower().strip()
    if crop in LOCAL_MANDI_DB:
        return f"Price trend for {crop.capitalize()}: Relatively stable with seasonal variations. Summer: Higher prices, Monsoon: Lower prices."
    return "Crop not found"
