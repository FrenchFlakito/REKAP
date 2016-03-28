import requests
import json
import datetime

def get_forecast():
    # in the "parameters.json" file, the "location" must be entered as follows : "City, iso_3166_country_code"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + access_params("location") + "&units=metric&appid=" + access_params("owm_api")
    forecast_request = requests.get(url)
    forecast_json = forecast_request.json()
    forecast_summary = (forecast_json["main"]["temp"], forecast_json["weather"][0]["main"])
    return forecast_summary

def forecast_message():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")
    message = "The date is " + date + " and it is " + time + ". The temperature right now is " + str(get_forecast()[0]) + " degrees Celsius with a general weather \"" + get_forecast()[1] + "\" today ! Have fun !"
    return message

def access_params(param):
    try:
        myplace = open('parameters.json', 'r')
        myplace = myplace.read()
        myplace = json.loads(myplace)
    except FileNotFoundError as err:
        print(err)
    return myplace[param]

def main():
    current_forecast = forecast_message()
    print current_forecast
    return current_forecast

main()
