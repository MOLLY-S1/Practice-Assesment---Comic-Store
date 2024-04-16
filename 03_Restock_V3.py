""" ADDING NEW COMICS - now with tk inter - now added to the sell function"""

from tkinter import *

root = Tk()


def add_comic():
    # add comic
    name = Entry(root, text= "Enter comic name: ").title()
    comic_type = Entry("Enter Comic type: ").title()
    price = Entry("Enter comic price: ")
    Comic(name, comic_type, price)