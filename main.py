import requests
from datetime import datetime
import smtplib
from tkinter import *
import random

my_email = "agarwaltushar3710@gmail.com"
my_pass = "ohhn vfpe ozih yccf"

def mail():
    pass

#fetching quotes with API
def get_quote():
    response = requests.get("https://zenquotes.io/api/quotes/random")
    response.raise_for_status()
    data = response.json()
    quote = data[1]["q"]
    author = data[1]["a"]
    complete = f"{quote}\n\n~{author}"
    #print(quote)
    #print(author)
    canvas.itemconfig(quote_text, text=complete)

#choosing fonts
with open("fonts.txt") as file:
    all_fonts = file.readlines()
    choosed_font = random.choice(all_fonts)

print(choosed_font)

#choosing image templte from images dir
window = Tk()
window.title("Monday be like...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="images.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="motivation", width=250, font=(choosed_font, 30), fill="black")
canvas.grid(row=0, column=0)


next_quote = "Next Plz"
button = Button(text =next_quote, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()