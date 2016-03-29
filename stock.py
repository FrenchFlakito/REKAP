import requests

def get_stock_history(stock):
    params = {"symbol": stock, "type": "daily", "startDate":"20160321000000"}
    url = "http://marketdata.websol.barchart.com/getHistory.json?key=4b3c254703f6e53f6028a8d430ec0ee2"
    try:
        # with requests.get we get a Response object
        r = requests.get(url, params)
        print "retrieving from", r.url
        json_hist = r.json()
    except:
        json_hist["message"] = "Error in API access"
    return json_hist

def stock_display(stock):
    message = ""
    history = get_stock_history(stock)
    for i in history["results"]:
        message = message + i["timestamp"][0:10] + " closing value : " + str(i["close"]) + "\n"
    message = "\n" + stock + " :\n" + message + "-------------\n"
    return message

print stock_display("TSLA")
