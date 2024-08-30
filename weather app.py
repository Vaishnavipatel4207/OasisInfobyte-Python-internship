import requests

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print("Error: Could not retrieve weather data.")

def main():
    api_key = "3faa7cb5e309f03ec069068051adb03b"  # OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ")
    
    weather_data = get_weather_data(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
