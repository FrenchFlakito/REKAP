import requests
import json
import datetime
from parameters import access_params


def get_forecast():
    # in the "parameters.json" file, the "location" must be entered as follows : "City, iso_3166_country_code"
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + access_params("location") + "&units=metric&appid=" + access_params("owm_api")
    forecast_request = requests.get(url)
    forecast_json = forecast_request.json()
    return forecast_json


def forecast_message(forecast_json):
    message = ""
    for i in forecast_json["list"]:
        heure = str(i["dt_txt"][11:13])
        if  (heure == "09") | (heure == "15"):
            moment = i["dt_txt"][0:16]
            temperature = str(i["main"]["temp"])
            conditions = i["weather"][0]["main"]
            if heure == "15":
                break_of_day = "\n\n"
            else:
                break_of_day = "\n"
            day_forecast = moment + " => " + temperature + " degrees with "+ conditions + break_of_day
            message = message + day_forecast
    return message

def main():
    myforecast_json = get_forecast()
    message = forecast_message(myforecast_json)
    print message
    return message

main()
