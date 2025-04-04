from flask import Flask,jsonify
import requests
import os
from dotenv import load_dotenv


app = Flask(__name__)

@app.route('/')
def home():
    return "This is a Flask api for weatherapp by Adarsh Dubey!!! For more Projects and API visit <b><I>adarsh-dubey.netlify.app</></b>"

def get_coordinates(location):
    url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
    headers = {
        "User-Agent": "MyFlaskApp/1.0 your_email@gmail.com"
    }
    response = requests.get(url, headers=headers)

   

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return data["lat"], data["lon"]
    else:
        return None, None  



def make_request(lat,lon):

    load_dotenv()

    api_key = os.getenv("WEATHER_API_KEY")

    print("API KEY IS ",api_key)

    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
     

    print("Respone is",response)


    if response.status_code == 200:
        data = response.json()

        weather_info = {
            "latitude": lat,
            "longitude": lon,
            "location": data.get("name", "Unknown"),
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["description"],
            "weather_id": data["weather"][0]["id"], 
            "wind_speed": data["wind"]["speed"],
            "wind_gust": data["wind"].get("gust", "N/A"),
            "cloudiness": data["clouds"]["all"],
            "visibility": data["visibility"],
            "rain_1h": data.get("rain", {}).get("1h", 0),
            "rain_3h": data.get("rain", {}).get("3h", 0),
            "snow_1h": data.get("snow", {}).get("1h", 0),
            "snow_3h": data.get("snow", {}).get("3h", 0),
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
            "data_calculated_at": data["dt"]
        }


        return weather_info

    else:
        return jsonify({"error": "Weather data not found"}), response.status_code

@app.route("/get_data_by_cordinate/<lat>/<lon>")
def get_data(lat,lon):
    if lat is None or lon is None:
        return jsonify({"error": "Location not found"}), 404
    return make_request(lat,lon)

@app.route('/get_data_by_location/<location>')
def get_data_by_location(location):

    lat,lon = get_coordinates(location)
    if lat is None or lon is None:
        return jsonify({"error": "Location not found"}), 404
    return make_request(lat,lon)


if __name__ == '__main__':
    app.run(debug=True)