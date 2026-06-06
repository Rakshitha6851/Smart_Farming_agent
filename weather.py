import requests
from config import WEATHER_API_KEY, WEATHER_API_TIMEOUT

def get_weather(city):
    """Get current weather for the specified city."""
    if not city or not isinstance(city, str):
        return "Please specify a city for weather information."

    city = city.strip()
    if not city:
        return "Please specify a city for weather information."

    try:

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=WEATHER_API_TIMEOUT)
        response.raise_for_status()

        data = response.json()

        if "main" not in data or "weather" not in data:
            return "Weather data not available."

        temperature = data["main"].get("temp")
        humidity = data["main"].get("humidity")
        weather_desc = data["weather"][0].get("description", "N/A")

        return (
            f"🌦 Weather in {city}\n\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {weather_desc.capitalize()}\n"
        )

    except requests.exceptions.RequestException as e:
        return f"Weather API error: {str(e)}"
    except Exception as e:
        return f"Weather error: {str(e)}"