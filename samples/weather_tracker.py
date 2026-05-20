import os
import json
import urllib.request
from datetime import datetime

class WeatherTracker:
    def __init__(self, city: str = "Cebu"):
        """Initializes the tracker with a target city."""
        self.city = city
        self.base_url = f"https://api.open-meteo.com/v1/forecast?latitude=10.3157&longitude=123.8854&current_weather=true"

    def fetch_current_weather(self) -> dict:
        """Fetches live weather data using standard python libraries."""
        print(f"📡 Fetching current weather data for {self.city}...")
        try:
            with urllib.request.urlopen(self.base_url, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    return data.get("current_weather", {})
                else:
                    print(f"⚠️ Server returned status code: {response.status}")
                    return {}
        except Exception as e:
            print(f"❌ Network error occurred: {e}")
            return {}

    def log_weather_to_file(self, weather_data: dict, filename: str = "weather_log.txt") -> bool:
        """Parses the weather details and saves them cleanly to a text file."""
        if not weather_data:
            print("⚠️ No data available to log.")
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp = weather_data.get("temperature", "N/A")
        windspeed = weather_data.get("windspeed", "N/A")

        log_entry = (
            f"--- Log Entry: {timestamp} ---\n"
            f"City: {self.city}\n"
            f"Temperature: {temp}°C\n"
            f"Wind Speed: {windspeed} km/h\n"
            f"{'='*30}\n"
        )

        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(log_entry)
            print(f"💾 Weather entry successfully saved to {filename}!")
            return True
        except IOError as e:
            print(f"❌ Failed to write to file: {e}")
            return False

if __name__ == "__main__":
    tracker = WeatherTracker()
    current_weather = tracker.fetch_current_weather()
    tracker.log_weather_to_file(current_weather)