import tkinter as tk
import math
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Mortgage Calculator")
# window.geometry("600x400")
# Window size can be also set up as below two lines - more complicated?
window_size = tk.Frame(master=window, width=600, height=400)
window_size.pack()

# Load and place an image for a background of your app
load_picture = Image.open("C:/Users/nazar/Desktop/Life scenarios Python Apps/Mortgage calculator/mortg_calc.jpg")
render = ImageTk.PhotoImage(load_picture)
label_picture = tk.Label(window, image=render)
label_picture.place(x=0, y=0)


def calculations():
    I4.delete(0, tk.END)
    I5.delete(0, tk.END)
    principal = int(I1.get())
    # print("Principal amount: " + principal)
    interest_rate = (float(I2.get())) / (100 * 12)
    # print("Interest(APR): " + interest_rate)
    years = int(I3.get())
    # print("Years: " + years)
    number_of_payments = years * 12
    monthly_instalment = principal * (interest_rate / (1 - math.pow((1 + interest_rate), (-number_of_payments))))
    total_amount = monthly_instalment * years * 12
    I4.insert(0, round(monthly_instalment, 2))
    I5.insert(0, round(total_amount, 2))


def clear():
    I1.delete(0, tk.END)
    I2.delete(0, tk.END)
    I3.delete(0, tk.END)
    I4.delete(0, tk.END)
    I5.delete(0, tk.END)


# Placed entry fields descriptions
tk.Label(window, text="Principal", font="Helvetica 9 bold").place(x=0, y=20)
tk.Label(window, text="Interest(APR)", font="Helvetica 9 bold").place(x=0, y=50)
tk.Label(window, text="Years", font="Helvetica 9 bold").place(x=0, y=80)
tk.Label(window, font="Helvetica 12 bold", text="Monthly Instalment").place(x=0, y=140)
tk.Label(window, font="Helvetica 12 bold", text="Total Amount Paid").place(x=0, y=170)
tk.Label(window, font="Helvetica 6", text="Fixed for 1 Y = 1.41% APR").place(x=0, y=220)
tk.Label(window, font="Helvetica 6", text="Fixed for 3 Y = 1.41% APR").place(x=0, y=235)
tk.Label(window, font="Helvetica 6", text="Fixed for 5 Y = 1.51% APR").place(x=0, y=250)
tk.Label(window, font="Helvetica 6", text="Fixed for 10 Y = 1.93% APR").place(x=0, y=265)
tk.Label(window, font="Helvetica 6", text="Fixed for 15 Y = 2.57% APR").place(x=0, y=280)

# Entry widget for user input
I1 = tk.Entry(window, bd=4)
I1.place(x=100, y=20)
I2 = tk.Entry(window, bd=4)
I2.place(x=100, y=50)
I3 = tk.Entry(window, bd=4)
I3.place(x=100, y=80)
I4 = tk.Entry(window, bd=8)
I4.place(x=170, y=140)
I5 = tk.Entry(window, bd=8)
I5.place(x=170, y=170)

# Add buttons for user inputs
B1 = tk.Button(window, text="Calculate", font="bold", bg="#89bf56", fg="black", command=calculations)
B2 = tk.Button(window, text="Clear", font="bold", bg="#b4b1e8", fg="black", command=clear)
B3 = tk.Button(window, text="Quit", font="bold", bg="#a6545e", fg="white", command=window.destroy)

# Place and a size of each button
B1.pack()
B1.place(x=20, y=330, height=60, width=100)
B2.pack()
B2.place(x=140, y=330, height=60, width=100)
B3.pack()
B3.place(x=260, y=330, height=60, width=100)

window.mainloop()
