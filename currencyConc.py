from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

import requests
import json

#colors 
cor0 = "#f1faee"  # white
cor1 = "#2a9d8f"  # green
cor2 = "#f4a261"  # orange

window = Tk()
window.geometry('500x500')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height = FALSE, width=FALSE)

#frames
top = Frame(window, width=500, height=100, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'
        

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted

    print(converted_amount, formatted)


#top frame

icon = Image.open('images/currency.png')
icon = icon.resize((60, 60))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text = "CURRENCY CONVERTER", height=5, padx=13, pady=30, anchor=CENTER, font=('inter 16 bold'), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)

#main frame
result = Label(main, text = " ",width=16, height=2, pady=10, relief="solid", anchor=CENTER, font=('inter 15 bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD']

from_label = Label(main, text = "From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('inter 10 bold'), bg=cor0, fg='#7209b7')
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text = "To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('inter 10 bold'), bg=cor0, fg='#7209b7')
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg=cor2, fg=cor0,font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)



window.mainloop()