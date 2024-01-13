from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.state('zoomed')
def getWeather():
        city = textfield.get()

        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text='ТЕКУЩАЯ ПОГОДА')

        #weather
        api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=7ef7776ee3a63dbdc05d537f458a1d10'

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = round(json_data['main']['temp'])
        temperature_feels = round(json_data['main']['feels_like'])
        pressure = int(json_data['main']['pressure']/1.333)
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,'°'))
        c.config(text=condition + ' | ' + 'ОЩУЩАЕТСЯ' + ' КАК: ' + str(temperature_feels) + '°')

        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)


#search box
Search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root, justify='center', width=17, font=('poppins',25,"bold"), bg='#404040', border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image = PhotoImage(file="Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom box
Frame_image = PhotoImage(file="Copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.place(x=50, y=430)

#time
name = Label(root, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=('Helvetica', 20))
clock.place(x=30, y=130)

#Label
label1 = Label(root, text='ВЕТЕР', font = ('Helvetica',15,'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=450)

label2 = Label(root, text='ВЛАЖНОСТЬ', font = ('Helvetica',15,'bold'), fg='white', bg='#1ab5ef')
label2.place(x=345, y=450)

label3 = Label(root, text='ДАВЛЕНИЕ', font = ('Helvetica',15,'bold'), fg='white', bg='#1ab5ef')
label3.place(x=650, y=450)

t = Label(font=('arial', 70, 'bold'), fg='#ee666d')
t.place(x=400, y=150)
c = Label(font = ('arial', 15, 'bold'))
c.place(x=400, y=250)

w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=120, y=480)
h = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
h.place(x=345, y=480)
p = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
p.place(x=670, y=480)


root.mainloop()