import requests
from datetime import datetime
import smtplib
import time
from tkinter import *

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

