
from doctest import master
import customtkinter
from tkinter import * 
from PIL import ImageTk, Image
from matplotlib.ft2font import BOLD
import requests
from sympy import false





def search(*args):

    for widget in content.winfo_children():
        widget.destroy()


    print("hello")
    #basic api calls
    baseurl = "http://api.openweathermap.org/data/2.5/weather?"
    apikey = "157486c9301015c404f1aca2830a3c19"
    city = userinput.get()


    url = baseurl + "appid=" +apikey + "&q=" +city
    weatherdata = requests.get(url).json()




    if len(weatherdata) !=13:
        label = customtkinter.CTkLabel(master=content, text="City Not Found", text_font=("Calibri", 30))

        label.grid(row=0, column=0, padx=50)
        content.grid_propagate(False)






    else:


        tempkelvin = weatherdata["main"]["temp"]
        tempcelsius = round(tempkelvin-273.15)
        tempfarenheit = round(1.8*(tempkelvin-273) + 32)

        print(weatherdata)

        xval = 85

        windspeed = "Windspeed: "+ str(weatherdata["wind"]["speed"])
        descriptions = weatherdata["weather"][0]["description"]
        humidity = "Humidity: " + str(weatherdata["main"]["humidity"]) + "%"
  

        content.grid_propagate(False)



        label = customtkinter.CTkLabel(master=content, text=weatherdata["name"], text_font=("Calibri", 55))
        label.grid(row =0, column = 3, padx=10 )


        temperature = str(tempcelsius) + "°C" + " / " + str(tempfarenheit) + "°F" 


        customtkinter.CTkLabel(master=content, text=temperature, text_font=("Calibri", 30)).grid(row =1, column = 3 , sticky=N)
        customtkinter.CTkLabel(master=content, text=windspeed, text_font=("Calibri", 30)).grid(row =2, column = 3 , sticky=N)

        customtkinter.CTkLabel(master=content, text=humidity, text_font=("Calibri", 30)).grid(row =3, column = 3 , sticky=N)

        customtkinter.CTkLabel(master=content, text=descriptions, text_font=("Calibri", 25)).grid(row =4, column = 3 , sticky=N)




    # logo = PhotoImage(Image.open("C:\\Users\\super\\Desktop\\Work\\Programming\\Python\\weather app\\icons\\cold.png"))

    # logocanvas = Canvas(root, width=100, height=100)
    # logocanvas.place(x=30, y=100)

    # logocanvas.create_image(100, 100, image=logo)




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#Basic GUI
main = customtkinter.CTk()
main.geometry("400x550")
main.resizable(False, False)
main.title("Weather")

userinput = customtkinter.CTkEntry(master=main, placeholder_text="Search for a city", width=380)
userinput.place(x=10, y=20)
userinput.bind("<Return>", search)



#frame containing info

content = customtkinter.CTkFrame(master=main,
                            width=350,
                            height=480,
                            corner_radius=10)

content.place(x=20, y=60)






main.mainloop()