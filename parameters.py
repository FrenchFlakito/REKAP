import json

def access_params(param):
    try:
        myplace = open('parameters.json', 'r')
        myplace = myplace.read()
        myplace = json.loads(myplace)
    except FileNotFoundError as err:
        print(err)
    return myplace[param]
