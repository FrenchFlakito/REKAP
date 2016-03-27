def get_forecast(place):
    # With a "place" as an imput, we get the data of the forecast
    # The method needs to return a tuple or a list. Or several

def meteo_message(forecast):
    # from the data (format TBD) we print a readable message
    print()

def main():
    # For now we ask an input to a human user
    myplace = input("Where do you want the weather forecast for ?\n")
    forecast = get_forecast(myplace)
    meteo_message(forecast)

main()
