import requests
from tkinter import *

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return response

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    temperature.config(text=f"Temp: {weather['main']['temp']}°C")
    description.config(text=f"Weather: {weather['weather'][0]['description']}")

root = Tk()
root.title("Weather App")

city_entry = Entry(root)
city_entry.pack()

search_button = Button(root, text="Get Weather", command=show_weather)
search_button.pack()

temperature = Label(root)
temperature.pack()

description = Label(root)
description.pack()

root.mainloop()
