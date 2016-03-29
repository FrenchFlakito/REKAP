import requests

def get_stock_history():
    url = "http://marketdata.websol.barchart.com/getHistory.json?key=4b3c254703f6e53f6028a8d430ec0ee2&symbol=IBM&type=daily&startDate=20160321000000"
    try:
        hist_request = requests.get(url)
        json_history = hist_request.json()
    except:
        json_history["message"] = "Error in API access"
    print "json_history", json_history
    return json_history

def stock_display():
    history = get_stock_history()
    message = ""
    message = message + "\nIBM :\n"
    for i in history["results"]:
        message = message + i["timestamp"][0:9] + " closing value : " + str(i["close"]) + "\n"
    message = message + "-------------\n"
    print message
    return message

stock_display()
