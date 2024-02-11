# Climate

This Python tool is a simple command-line weather app, to allow a user to input a location and receive the weather conditions and temperature. Relevant parts of the data are then saved to a `txt` file in a more readable format for the user. The `txt` file also has unique and dynamic naming using the given location and the ID from the JSON data.

## Usage

### Check Weather Conditions

```bash
climate -w {location}
```

## Obtaining the Data

The tool uses the OpenWeather API to collect the data in JSON format. The query given to the API requires the location, given by the user in the command line, and the user's API key, which is stored in the dedicated `.env` file.

> **Important**: The `.env` file is important as it prevents malicious actors abusing revealed API keys.

The data is retrieved from the OpenWeather servers using the requests library. A simple sentence describing the temperature and weather conditions in the location is output to the console, while a more in-depth `txt` file is generated using the formatted data and saved to a unique location.

## Understanding the Data and the Documentation

My experience using the OpenWeather API was painless. Getting access to the API is as simple as setting up an account, unlike Twitter, which requires you to complete an application (I didn't bother to go past the first stage of this). As far as I understand, OpenAI is not difficult either and actually comes with it's own API library to aid the user.

The [documentation](https://openweathermap.org/current) for the OpenWeather API is really good, explains each part of the data quite simply, however the nature of the data might lend to this ease of understanding.

