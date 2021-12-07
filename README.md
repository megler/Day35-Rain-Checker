# Pomodoro

Using Twilio and OpenWeatherMap, send a text if rain is expected in next 11
hours. Can be automated on an online server like PythonAnywhere to send daily.


## Usage
When run, the app will query OpenWeatherMap for any chance of rain in next 11 hours.
If rain is forecast, a text will be sent via Twilio. Otherwise, you'll receive a
text saying no rain in forecast.

API variables and Longitude/Latitude are set in a .env file. See [python-env docs](https://pypi.org/project/python-dotenv/) for more info.

## License
[MIT](https://choosealicense.com/licenses/mit/)