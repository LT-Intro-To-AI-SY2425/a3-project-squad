import requests

API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    # Construct the complete URL
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    
    if weather_data:
        main_weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        print(f"Weather in {city}: {main_weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found!")

if __name__ == "__main__":
    main()
