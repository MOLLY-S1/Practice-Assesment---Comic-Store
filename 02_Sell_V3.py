""" Version 3
Now incorporates the use of Tk inter"""
from tkinter import *

# Root Window
root = Tk()

# Comic storage
comics = []
sd = []
ww = []
lm = []


class Comic:
    def __init__(self, comic_type, name, price):
        self.comic_type = comic_type
        self.name = name
        self.price = price
        comics.append(self)
        if comic_type == "Lizard Man":
            lm.append(self)
        elif comic_type == "Water Woman":
            ww.append(self)
        elif comic_type == "Super Dude":
            sd.append(self)
        else:
            print("INVALID")

    def display_info(self):

        print(f"#################\n"
              f"Name: {self.name}\n"
              f"Type: {self.comic_type}\n"
              f"Price: ${self.price}\n")




def print_comics():
    print("FULL INVENTORY")
    print("#################\n")
    print("STOCK NUMBERS: \n"
          "#################\n"
          f"Water Woman: {len(ww)}\n"
          f"Super Dude: {len(sd)}\n"
          f"Lizard Man: {len(lm)}\n")
    for comic in comics:
        comic.display_info()


def count_comic():
    def show():
        label.config(text=f"Selected comic type: {clicked.get()}")

    Label(root, text="Select comic type to show stock or press 'Inventory' to print a full list of all comic details").pack()

    options = ["Lizard Man", "Water Woman", "Super Dude"]
    clicked = StringVar()
    clicked.set("Lizard Man")
    drop = OptionMenu(root, clicked, *options)
    drop.pack()

    label = Label(root, text=" ")
    label.pack()
    root.title("SHOW STOCK")

    def show_stock_count():
        if clicked.get() == "Water Woman":
            stock_count = len(ww)
        elif clicked.get() == "Super Dude":
            stock_count = len(sd)
        else:
            stock_count = len(lm)
        stock_label.config(text=f"There are {stock_count} comics in stock")

    stock_label = Label(root, text="")
    stock_label.pack()

    Button(root, text="SHOW COMIC STOCK", command=show_stock_count).pack()
    Button(root, text="INVENTORY", command=print_comics).pack(side=BOTTOM)


# MAIN ROUTINE
Comic("Lizard Man", "Saving the lizards", 2.30)
Comic("Lizard Man", "The slippery snake", 2.50)
Comic("Lizard Man", "The T-Rex", 2.0)
Comic("Water Woman", "Saving the ocean", 3.20)
Comic("Water Woman", "Saving the sea", 3.50)
Comic("Water Woman", "Saving the coast", 3.0)
Comic("Super Dude", "Saving the People", 1.75)
Comic("Super Dude", "Saving the World", 1.80)


count_comic()

root.mainloop()
