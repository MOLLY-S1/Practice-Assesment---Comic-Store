"""Version 2
This code will create a welcome screen, using TKinter"""
import sys
from tkinter import *

root = Tk()

root.title("WELCOME")
welcome = Label(root, bg="blue4", fg="Turquoise", text="Welcome to the Comic Book Store",
                font=("Times", 20, "bold"))
options = Label(root, fg="Black", text="Please choose an option:",
                font=("Ariel", 10, "bold"))

welcome.pack(side=TOP)
options.pack(side=TOP)


def sell():
    print("Sell Comics")


def show():
    print("Show Stock")


def restock():
    print("Restock Comics")


def exit():
    print("Goodbye")
    sys.exit()


sell_b1 = Button(root, text="Sell Comics", command=sell)
show_b2 = Button(root, text="Show Stock", command=show)
restock_b3 = Button(root, text="Restock Comics", command=restock)
exit_b4 = Button(root, text="Exit", command=exit)

sell_b1.pack()
show_b2.pack()
restock_b3.pack()
exit_b4.pack()

root.mainloop()
