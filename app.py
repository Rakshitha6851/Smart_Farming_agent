"""
Smart Farming AI Agent - Flask Web Application
Provides web interface for farmers to get agricultural guidance
"""

from flask import Flask, render_template, request, jsonify
from chatbot import ask_ai, get_available_features
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    """Main page - display form and handle questions"""
    answer = ""
    error_message = ""
    
    if request.method == "POST":
        try:
            question = request.form.get("question", "").strip()
            
            if not question:
                error_message = "❌ Please enter a question!"
            elif len(question) < 2:
                error_message = "❌ Question too short. Please provide more details!"
            elif question.lower() in ["hi", "hello", "hey", "namaste"]:
                answer = """👋 Hello Farmer! 🌾

Welcome to Smart Farming AI Agent!

I'm here to help you with:
✅ Weather forecasts
✅ Market prices (Mandi rates)
✅ Soil recommendations
✅ Pest control solutions
✅ Fertilizer guidance
✅ Irrigation schedules
✅ Seasonal crop recommendations

Ask me anything about farming! You can ask in English or your local language."""
            else:
                logger.info(f"Processing question: {question}")
                answer = ask_ai(question)
                if not answer:
                    error_message = "❌ Could not find information about your question. Please try a different question!"
        
        except Exception as e:
            logger.error(f"Error processing question: {e}")
            error_message = f"❌ Error: {str(e)}"
    
    return render_template("index.html", answer=answer, error_message=error_message)

@app.route("/features", methods=["GET"])
def features():
    """Return available features"""
    return jsonify({"features": get_available_features()})

@app.route("/api/ask", methods=["POST"])
def api_ask():
    """API endpoint for getting farming advice"""
    try:
        data = request.get_json()
        question = data.get("question", "").strip()
        
        if not question:
            return jsonify({"error": "Question is required"}), 400
        
        answer = ask_ai(question)
        return jsonify({"question": question, "answer": answer})
    
    except Exception as e:
        logger.error(f"API Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "Smart Farming Agent is running"})

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal error: {error}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )