import requests

BASE_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly'
API_KEY = 'b6907d289e10d714a6e88b30761fae22'

def get_weather():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    response = get_weather_data()
    if response is not None:
        for data in response['list']:
            if data['dt_txt'].startswith(date_str):
                print(f"Temperature on {data['dt_txt']}: {data['main']['temp']} K")
                break
        else:
            print("Weather data not available for the input date.")
    else:
        print("Error fetching weather data.")

def get_wind_speed():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    response = get_weather_data()
    if response is not None:
        for data in response['list']:
            if data['dt_txt'].startswith(date_str):
                print(f"Wind Speed on {data['dt_txt']}: {data['wind']['speed']} m/s")
                break
        else:
            print("Weather data not available for the input date.")
    else:
        print("Error fetching weather data.")

def get_pressure():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    response = get_weather_data()
    if response is not None:
        for data in response['list']:
            if data['dt_txt'].startswith(date_str):
                print(f"Pressure on {data['dt_txt']}: {data['main']['pressure']} hPa")
                break
        else:
            print("Weather data not available for the input date.")
    else:
        print("Error fetching weather data.")

def get_weather_data():
    params = {
        'q': 'London,us',  # London location (Note: 'us' is a dummy value, not used in the API)
        'appid': API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def main():
    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            get_weather()
        elif choice == '2':
            get_wind_speed()
        elif choice == '3':
            get_pressure()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
