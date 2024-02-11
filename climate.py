import argparse
import os

import pycountry
import requests
from dotenv import load_dotenv

# API information
load_dotenv()
api_key = os.getenv("api_key")  # OpenWeather API key


# Define a function to convert the timezone response
def formatTimezone(data):
    timezoneOffset = data["timezone"]
    timezoneOffsetHrs = timezoneOffset // 3600
    timezoneOffsetMins = (timezoneOffset % 3600) // 60

    if timezoneOffsetHrs >= 0:
        return f"+{timezoneOffsetHrs:02d}:{timezoneOffsetMins:02d}"
    else:
        return f"+{timezoneOffsetHrs:03d}:{timezoneOffsetMins:02d}"


# Define a function to convert the country code
def formatCountry(data):
    countryCode = data["sys"]["country"]

    try:
        return pycountry.countries.get(alpha_2=countryCode).name
    except AttributeError:
        return countryCode


# Define a function to save the data characteristics
def saveWeather(location, data):
    # Format relevant variables to a readable format
    weatherText = "Weather information for {}\n".format(location)
    weatherText += "-----------------------------\n"
    weatherText += f"Weather: {data['weather'][0]['description']}\n"
    weatherText += f"Temperature: {data['main']['temp'] - 273.15:.1f}°C\n"
    weatherText += f"Humidity: {data['main']['humidity']}%\n"
    weatherText += f"Pressure: {data['main']['pressure']} hPa\n"
    weatherText += f"Wind Speed: {data['wind']['speed']} m/s\n"
    weatherText += f"Cloudiness: {data['clouds']['all']}%\n"
    weatherText += f"Timezone: UTC{formatTimezone(data)}\n"
    weatherText += f"Country: {formatCountry(data)}\n"
    weatherText += "-----------------------------\n"

    # Save the file
    fileName = f"data/{location}_{data['id']}.txt"
    with open(fileName, "a+") as file:
        file.write(weatherText)


# Define a function to give the weather conditions
def giveWeather(location):
    # Input the location with the API
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    )

    try:
        # Make API call
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Get weather conditions
        weather = data["weather"][0]["description"]

        # Get temperature in celsius
        temperature = data["main"]["temp"] - 273.15

        saveWeather(location, data)

        # Return string describing the weather
        return f"The weather in {location} is {weather} with a temperature of {temperature:.1f}°C."

    # Handle errors
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return "Error parsing weather data."


def main():
    parse = argparse.ArgumentParser(
        description="Receive climate information for a location."
    )
    parse.add_argument(
        "-w", "--weather", metavar="location", help="Get weather information."
    )

    args = parse.parse_args()

    if args.weather:
        print(giveWeather(args.weather))
    else:
        print("Please use either -w to get weather conditions or pollution.")


if __name__ == "__main__":
    main()
