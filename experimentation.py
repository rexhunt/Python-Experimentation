import urllib.request, json

url="https://api.coinmarketcap.com/v1/ticker/"

#jsonurl = urlopen(url)

#print(jsonurl)

#text = json.loads(jsonurl)

#print(text)


with urllib.request.urlopen(url) as jsonurl:
    data = json.loads(jsonurl.read().decode())
    print(data)
