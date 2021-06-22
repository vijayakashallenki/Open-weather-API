import requests
#import os
from datetime import datetime

api_key = '050b23126abc246654c48401cb0cb58a'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
r = api_data
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("vijay's open weather report:                                         *Wanna by a me a coffee?")
print("                                                                       LOL I Don't Drink coffee.....                      ")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("==================================================================")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
print("\n")
print("Copyrights:@Vijayakash-Allenki".rjust(75))
f = open("weather.txt","w").close()
f = open('weather.txt','a')

f.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
f.write("Current weather desc  : {}\n".format(weather_desc))
f.write("Current Humidity      : {} % \n".format(hmdt))
f.write("Current wind speed    : {} kmph \n".format(wind_spd))

f.close()
pr_f =  open('weather.txt')
a = pr_f.readlines()
for i in a:
  print(i.strip())
