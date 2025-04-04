
# 🌦️ Flask Weather API by Adarsh Dubey

A lightweight Flask REST API that provides real-time weather data using OpenWeatherMap and OpenStreetMap (Nominatim). This project allows you to retrieve current weather information by either location name or geographic coordinates.

---

## 🌐 Live Preview

➡️ Visit: [adarsh-dubey.netlify.app](https://adarsh-dubey.netlify.app)  
For more APIs and projects by Adarsh Dubey.

---

## ✨ Features

- 🔍 Get weather by location name
- 📍 Get weather by latitude & longitude
- 🛰️ Uses OpenStreetMap Nominatim for geocoding
- ☁️ Real-time weather data from OpenWeatherMap
- 🌡️ Includes temperature, humidity, wind, clouds, rain/snow, visibility, and more
- 🔐 API key secured using dotenv
- ⚙️ Built with Flask

---

## 🧰 Tech Stack

- Python 3.x  
- Flask  
- Requests  
- python-dotenv  
- OpenWeatherMap API  
- OpenStreetMap Nominatim API  

---

## 📥 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-flask-api.git
cd weather-flask-api
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root directory and add your OpenWeatherMap API key:

```
WEATHER_API_KEY=your_api_key_here
```

### 5. Run the Flask App

```bash
python app.py
```

Runs on: `http://127.0.0.1:5000/`

---

## 📡 API Endpoints

### 🔹 Home Route

```http
GET /
```

Returns a welcome message.

---

### 🔹 Get Weather by Location

```http
GET /get_data_by_location/<location>
```

Fetches weather data using the city/location name.

---

### 🔹 Get Weather by Coordinates

```http
GET /get_data_by_cordinate/<lat>/<lon>
```

Fetches weather data using latitude and longitude.

---

## 📄 License

MIT License. Feel free to use and modify.

---

## 👨‍💻 Author

**Adarsh Dubey**  
📧 [adarshdubey0002@gmail.com](mailto:adarshdubey0002@gmail.com)  
🌐 [adarsh-dubey.netlify.app](https://adarsh-dubey.netlify.app)
