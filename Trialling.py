import sys
from tkinter import *

root = Tk()

# Comic storage
comics = []
sd = []
ww = []
lm = []
names_prices = {}  # Dictionary to store names and prices


# MAIN ROUTINE


class Comic:
    def __init__(self, comic_type, name, price):
        self.comic_type = comic_type
        self.name = name
        self.price = price
        comics.append(self)
        names_prices[name] = price  # Store name and price in the dictionary
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


Comic("Lizard Man", "Saving the lizards", 2.30)
Comic("Lizard Man", "The slippery snake", 2.50)
Comic("Lizard Man", "The T-Rex", 2.0)
Comic("Water Woman", "Saving the ocean", 3.20)
Comic("Water Woman", "Saving the sea", 3.50)
Comic("Water Woman", "Saving the coast", 3.0)
Comic("Super Dude", "Saving the People", 1.75)
Comic("Super Dude", "Saving the World", 1.80)


def sell_comics_proper():
    clicked = StringVar()
    clicked.set("COMICS FOR SALE")

    def sell_comics():
        nonlocal count
        selected_comic = clicked.get().split(" - ")[0]
        for comic in comics:
            if comic.name == selected_comic:
                count += comic.price
                money.config(text=f"INCOME - ${count}")
                break

    options = []
    for comic in comics:
        if "Comic" in comic.name:
            options.append(comic.name.replace("Comic", "") + f" - ${comic.price}")
        else:
            options.append(comic.name + f" - ${comic.price}")

    drop = OptionMenu(root, clicked, *options)
    drop.pack()
    label = Label(root, text=" ")
    label.pack()
    root.title("SELL COMICS")

    count = 0
    money = Label(root, text=f"INCOME - ${count}")
    money.pack(side=TOP)

    exit_button = Button(root, text="EXIT", command=sys.exit)
    exit_button.pack(side=BOTTOM)
    sell_button = Button(root, text="CONFIRM SALE", command=sell_comics)
    sell_button.pack(side=BOTTOM)


sell_comics_proper()
root.mainloop()
