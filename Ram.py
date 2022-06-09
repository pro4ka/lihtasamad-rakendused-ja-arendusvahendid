import requests, json
import psutil

mem = psutil.virtual_memory()
print(mem)
warning_text = "hoiatusteate taituvus % peab olema seadistatav"


def warning():
    if mem.percent > 20:
        print(warning_text)


warning()

with open('info.txt', 'w') as f:
    f.writelines(warning_text)

apikey = "010cb4edccd749722ca7065d57f08363"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name: ")
complete_url = base_url + "appid=" + apikey + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
print(x)