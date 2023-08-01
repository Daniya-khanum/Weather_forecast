# Weather Forecast Program

This is a simple Python program that interacts with the OpenWeatherMap API to provide hourly weather forecast data for the London location.

## Features

- Get weather forecast for a specific date.
- Retrieve wind speed and pressure information for a given date.

## Requirements

- Python 3.x
- `requests` library (to make HTTP requests)

## Getting Started

1. Clone this repository to your local machine.
2. Install Python 3.x if you haven't already.
3. Install the required `requests` library using `pip install requests`.
4. Replace `'YOUR_API_KEY'` in the `weather_forecast.py` file with your actual API key from OpenWeatherMap.
5. Run the program using `python weather_forecast.py`.
6. Follow the on-screen prompts to get weather data or exit the program.

## Usage

1. Choose an option:
   - 1: Get weather forecast
   - 2: Get wind speed
   - 3: Get pressure
   - 0: Exit

2. If option 1, enter the date (YYYY-MM-DD) for the weather forecast.
3. If option 2 or 3, enter the date (YYYY-MM-DD) to get wind speed or pressure.

## API Key

To use this program, you need an API key from OpenWeatherMap. You can sign up for a free API key at https://openweathermap.org/api.

