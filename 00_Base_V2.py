import sys
from tkinter import *

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

def sell():
    print("Sell Comics")


def show():
    print("Show Stock")


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


def restock():
    print("Restock Comics")


def exit():
    print("Goodbye")
    sys.exit()


def welcome_screen():
    root = Tk()

    root.title("WELCOME")
    welcome = Label(root, bg="Blue4", fg="turquoise", text="Welcome to the Comic Book Store",
                    font=("Times", 20, "bold"))
    options = Label(root, fg="Black", text="Please choose an option:",
                    font=("Ariel", 10, "bold"))

    welcome.pack(side=TOP)
    options.pack(side=TOP)

    sell_b1 = Button(root, text="Sell Comics", command=sell)
    show_b2 = Button(root, text="Show Stock", command=show)
    restock_b3 = Button(root, text="Restock Comics", command=restock)
    exit_b4 = Button(root, text="Exit", command=exit)

    sell_b1.pack()
    show_b2.pack()
    restock_b3.pack()
    exit_b4.pack()

    root.mainloop()


# MAIN ROUTINE
welcome_screen()
