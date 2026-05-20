import urllib.request
import json

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

            current = data['current_condition'][0]
            area = data['nearest_area'][0]

            city_name = area['areaName'][0]['value']
            country = area['country'][0]['value']
            temp_c = current['temp_C']
            feels_like = current['FeelsLikeC']
            humidity = current['humidity']
            wind_speed = current['windspeedKmph']
            description = current['weatherDesc'][0]['value']

            print("\n" + "="*40)
            print(f"  Weather in {city_name}, {country}")
            print("="*40)
            print(f"  🌡️  Temperature  : {temp_c}°C")
            print(f"  🤔  Feels Like   : {feels_like}°C")
            print(f"  💧  Humidity     : {humidity}%")
            print(f"  💨  Wind Speed   : {wind_speed} km/h")
            print(f"  ☁️  Condition    : {description}")
            print("="*40 + "\n")

    except Exception as e:
        print(f"\n❌ Could not fetch weather for '{city}'. Check city name.\n")

def main():
    print("\n🌤️  Python Weather App")
    print("----------------------")
    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye! 👋")
            break
        if city:
            get_weather(city)

if __name__ == "__main__":
    main()
