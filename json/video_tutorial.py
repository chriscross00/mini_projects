import json
from urllib.request import urlopen



if __name__ == "__main__":

    print("hello world\n\n")

    with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
        source = response.read()

    print(source)
