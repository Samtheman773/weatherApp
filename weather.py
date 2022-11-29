from distutils.command.config import config
from msilib.schema import Icon
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'secrets.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

#tkinter is used for U/I

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        #create a tuple that will return infomration (City, Country, temp_celsius, temp_fahrenheit, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_farenheit = temp_celsius * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        humidity = json['main']['humidity']
        weather_description = json['weather'][0]['description']

        final = (city, country, temp_celsius, temp_farenheit, icon, weather, humidity, weather_description)
        return final;
    
    else:
        return None



def search():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        #global img["icon"] = 'C:/Users/Sam/Desktop/Python/weather-app/weather_icons/{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
        humid_lbl['text'] = 'Humidity Level: {}'.format(weather[6])
        description_label['text'] = weather[7];
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Weather Application")
app.geometry("750x350")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather", width=12, command=search)
search_btn.pack() # The .pack allows the button to be seen

location_label = Label(app, text="", font = ('bold', 20))
location_label.pack()

#image = PhotoImage(file="")
#image = Label(app, image=img)
#image.pack()

temp_lbl = Label(app, text="")
temp_lbl.pack()

weather_lbl = Label(app, text="")
weather_lbl.pack()

humid_lbl = Label(app, text="")
humid_lbl.pack()

description_label = Label(app, text='')
description_label.pack()




app.mainloop()



