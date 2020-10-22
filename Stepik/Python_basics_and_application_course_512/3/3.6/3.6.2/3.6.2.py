import requests
city=input("City")
url="http://api.openweathermap.org/data/2.5/weather?"

params={
    "q" : city,
    "appid" : "c79f8edf0acd359113d22c5dce154a91",
    "units" : "metric"
}

res=requests.get(url,params=params)
data=res.json()
template="Temperature in {} is {}"
print(template.format(city,data["main"]["temp"]))
