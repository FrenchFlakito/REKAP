import requests
import datetime
from parameters import access_params

def get_stock_history(stock):
    # penser a rendre dynamique la date et retriever celle d il y a 3 semaines.
    # now = datetime.datetime.now()
    # start_date = now.strftime("%Y%m%d0000000")
    params = {"key": access_params("barchart_key"), "symbol": stock, "type": "daily", "startDate":"20160321000000"}
    url = "http://marketdata.websol.barchart.com/getHistory.json?"
    try:
        # with requests.get we get a Response object
        r = requests.get(url, params)
        # print "retrieving from", r.url
        json_hist = r.json()
    except:
        json_hist["message"] = "Error in API access"
    return json_hist

def stock_display(stock):
    message = ""
    total = 0
    history = get_stock_history(stock)
    for i in history["results"]:
        message = message + i["timestamp"][0:10] + " closing value : " + str(i["close"]) + "\n"
        total = total + i["close"]
    average = round(total/len(history["results"]), 2)
    message = "\n" + stock + " :\n" + message + "Average :" + str(average) + "\n-------------\n"
    return message

def message_display():
    message = ""
    values = access_params("stock_values")
    for stock in values:
        h = stock_display(stock)
        message = message + h
    return message

print(message_display())
