import requests

API_KEY = 'f8048b0e63072be71064f31ae14f688c'
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
        temperature = (temperature * 9/5) + 32
        print(f"Temperature: {temperature}°F")
    else:
        print("City not found!")
        #hello

if __name__ == "__main__":
    main()
