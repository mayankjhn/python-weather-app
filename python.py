import requests

API_KEY = 638fc22172030697cd17f31974799d8c
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        return f"City: {city}\nTemperature: {response['main']['temp']}°C\nWeather: {response['weather'][0]['description']}"
    else:
        return "Invalid city name!"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
