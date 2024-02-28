from currency_converter import CurrencyConverter
import tkinter as tk

#This section make programm screen width and height
screen = tk.Tk()
scr_width = 400
scr_height = 600

#This is hader section
heading = "All Currency Converter"
heading_font = "Times 25 bold"
place_x = 30
place_y = 80

#This is body section
body = "Enter Amount Here:"
body2 = "Enter Currency Name:"
body3 = "Enter Currency to convert:"
body3_font = "Times 13 bold"
body_font = "Times 15 bold"
body_place_x = 20
body_place_y = 150
body2_place_x = 20
body2_place_y = 200
body3_place_x = 20
body3_place_y = 250

#This is button section
button_text = "Click"
button_place_x = 200
button_place_y = 400

# Correctly instantiate the CurrencyConverter class
a = CurrencyConverter()

def calculater():
    amount = float(body_entry.get())  # Convert amount to float to handle decimals
    cur1 = body2_entry.get()
    cur2 = body3_entry.get()
    data = a.convert(amount, cur1, cur2)
    l1 = tk.Label(screen, text=data, font="Times 15 bold",).place(x=150, y=500)

screen.geometry(f"{scr_width}x{scr_height}")

head_part = tk.Label(screen, text=heading, font=heading_font).place(x=place_x, y=place_y)
body_part = tk.Label(screen, text=body, font=body_font).place(x=body_place_x, y=body_place_y)
body2_part = tk.Label(screen, text=body2, font=body_font).place(x=body2_place_x, y=body2_place_y)
body3_part = tk.Label(screen, text=body3, font=body3_font).place(x=body3_place_x, y=body3_place_y)

button = tk.Button(screen, text=button_text, command=calculater).place(x=button_place_x, y=button_place_y)

body_entry = tk.Entry(screen)
body2_entry = tk.Entry(screen)
body3_entry = tk.Entry(screen)

body_entry.place(x=245, y=155)
body2_entry.place(x=245, y=200)
body3_entry.place(x=245, y=250)
screen.mainloop()
