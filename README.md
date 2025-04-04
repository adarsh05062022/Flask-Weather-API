Weather API - Flask Application 🌦️
Overview
This is a Flask API that provides weather information based on location or latitude/longitude coordinates. The weather data is fetched using the OpenWeatherMap API.

🚀 Developed by: Adarsh Dubey

Features
✅ Fetch weather data by city name.
✅ Fetch weather data using latitude and longitude.
✅ Provides temperature, humidity, pressure, wind speed, and more.
✅ Uses .env for API key security.

Setup and Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/yourusername/weather-api.git
cd weather-api
2️⃣ Create a Virtual Environment (Optional)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Create a .env File for API Key
Create a .env file in the project root and add:

ini
Copy
Edit
WEATHER_API_KEY=your_openweathermap_api_key
Replace your_openweathermap_api_key with your actual API key from OpenWeatherMap.

Running the Flask App
sh
Copy
Edit
python app.py
The API will start at http://127.0.0.1:5000/

API Endpoints
🌍 1. Get Weather by Location Name
Endpoint:

pgsql
Copy
Edit
GET /get_data_by_location/<location>
📌 Example:

sh
Copy
Edit
http://127.0.0.1:5000/get_data_by_location/Delhi
📌 Response:

json
Copy
Edit
{
    "latitude": "28.6274",
    "longitude": "77.1717",
    "location": "Connaught Place",
    "country": "IN",
    "temperature": 31.0,
    "feels_like": 30.5,
    "humidity": 50,
    "pressure": 1012,
    "weather": "clear sky",
    "wind_speed": 2.5,
    "sunrise": 1743727073,
    "sunset": 1743772224
}
📍 2. Get Weather by Latitude & Longitude
Endpoint:

php-template
Copy
Edit
GET /get_data_by_cordinate/<lat>/<lon>
📌 Example:

sh
Copy
Edit
http://127.0.0.1:5000/get_data_by_cordinate/28.6274/77.1717
📌 Response: (Same as above)

Tech Stack
Python 🐍

Flask 🔥

Requests 🌐

OpenWeatherMap API ☁️

🛠️ Future Improvements
📌 Add hourly & weekly weather forecast

📌 Include air quality index (AQI)

📌 Improve error handling & logging

💡 Contributing
Feel free to contribute to this project by submitting a pull request! 🚀

📜 License
This project is open-source and available under the MIT License.

🚀 For more projects & APIs, visit: adarsh-dubey.netlify.app 🎯
