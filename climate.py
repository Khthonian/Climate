#!/usr/bin/env python3

import argparse
import requests

# API information
api_key = "a8f17a6c042ac852d0eb43031428a411" # OpenWeather API key

# Define a function to give the weather conditions
def giveWeather(location):
    # Input the location with the API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    try:
        # Make API call
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Get weather conditions
        weather = data['weather'][0]['description']

        # Get temperature in celsius
        temperature = data['main']['temp'] - 273.15

        # Return string describing the weather
        return f"The weather in {location} is {weather} with a temperature of {temperature:.1f}°C."
    
    # Handle errors
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return "Error parsing weather data."

def main():
    parse = argparse.ArgumentParser(description="Receive climate information for a location.")
    parse.add_argument("-w", "--weather", metavar="location", help="Get weather information.")

    args = parse.parse_args()

    if args.weather:
        print(giveWeather(args.weather))
    else:
        print("Please use either -w to get weather conditions or pollution.")


if __name__ == "__main__":
    main()
