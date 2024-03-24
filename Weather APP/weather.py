import requests

def get_weather(city):
    api_key = '2c19fbb94f2de02f315fa85377f141ea'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_info = {
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_info, city):
    if weather_info:
        print(f"Weather in {city}:")
        print(f"Description: {weather_info['description'].capitalize()}")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        print("Weather information not available.")

def main():
    city = input("Enter the city name: ")
    weather_info = get_weather(city)
    display_weather(weather_info, city)

if __name__ == "__main__":
    main()
