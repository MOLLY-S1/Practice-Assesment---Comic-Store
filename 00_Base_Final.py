import sys
from tkinter import *

root = Tk()

# Comic storage
comics = []
sd = []
ww = []
lm = []
names_prices = {}  # Dictionary to store names and prices


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


def add_comic():
    add_window = Toplevel(root)
    add_window.title = "ADD NEW COMIC"

    # Entry widgets for user input
    Label(add_window, text="Enter Comic Name: ").pack(side=TOP, fill=X)
    name_entry = Entry(add_window)
    name_entry.pack(side=TOP, fill=X)
    Label(add_window, text="Enter Comic Type: ").pack(side=TOP, fill=X)
    type_entry = Entry(add_window)
    type_entry.pack(side=TOP, fill=X)
    Label(add_window, text="Enter Comic Price: ").pack(side=TOP, fill=X)
    price_entry = Entry(add_window)
    price_entry.pack(side=TOP, fill=X)

    def add_new_comic():
        # Get user input from Entry widgets
        name = name_entry.get()
        comic_type = type_entry.get()
        price = float(price_entry.get())  # Convert price to float

        # Create new Comic object
        new_comic = Comic(comic_type, name, price)

        add_window.destroy()

    # Button to add the new comic
    add_button = Button(add_window, text="Add Comic", command=add_new_comic)
    add_button.pack()


def count_comic():
    add_window = Toplevel(root)
    add_window.title = "COMIC STOCK"

    Label(add_window,
          text="Select comic type to show stock or press 'Inventory' to print a full list of all comic details").pack()

    options = ["Lizard Man", "Water Woman", "Super Dude"]
    clicked = StringVar()
    clicked.set("Lizard Man")
    drop = OptionMenu(add_window, clicked, *options)
    drop.pack()

    label = Label(add_window, text=" ")
    label.pack()

    def show_stock_count():
        if clicked.get() == "Water Woman":
            stock_count = len(ww)
        elif clicked.get() == "Super Dude":
            stock_count = len(sd)
        else:
            stock_count = len(lm)
        stock_label.config(text=f"There are {stock_count} comics in stock")

    stock_label = Label(add_window, text="")
    stock_label.pack()

    Button(add_window, text="EXIT", command=add_window.destroy).pack(side=BOTTOM)
    Button(add_window, text="SHOW COMIC STOCK", command=show_stock_count).pack()
    Button(add_window, text="INVENTORY", command=lambda: print(print_comics())).pack(side=BOTTOM)
    Button(add_window, text="ADD STOCK", command=add_comic).pack(side=BOTTOM)


# Sell Comics
def sell_comics_proper():
    add_window = Toplevel(root)
    add_window.title = "SELL COMICS"
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

    drop = OptionMenu(add_window, clicked, *options)
    drop.pack()
    label = Label(add_window, text=" ")
    label.pack()
    root.title("SELL COMICS")

    count = 0
    money = Label(add_window, text=f"INCOME - ${count}")
    money.pack(side=TOP)

    exit_button = Button(add_window, text="EXIT", command=add_window.destroy)
    exit_button.pack(side=BOTTOM)
    sell_button = Button(add_window, text="CONFIRM SALE", command=sell_comics)
    sell_button.pack(side=BOTTOM)


def exit_program():
    print("GOODBYE")
    root.destroy()
    sys.exit()


def welcome_screen():
    root.title("WELCOME")
    welcome = Label(root, bg="Blue4", fg="turquoise", text="Welcome to the Comic Book Store",
                    font=("Times", 20, "bold"))
    options = Label(root, fg="Black", text="Please choose an option:",
                    font=("Ariel", 10, "bold"))

    welcome.pack(side=TOP)
    options.pack(side=TOP)

    sell_b1 = Button(root, text="Sell Comics", command=sell_comics_proper)
    show_b2 = Button(root, text="Show Stock", command=count_comic)
    restock_b3 = Button(root, text="Restock Comics", command=add_comic)
    exit_b4 = Button(root, text="Exit", command=exit_program)

    sell_b1.pack()
    show_b2.pack()
    restock_b3.pack()
    exit_b4.pack()

    root.mainloop()


# MAIN ROUTINE
Comic("Lizard Man", "Saving the lizards", 2.30)
Comic("Lizard Man", "The slippery snake", 2.50)
Comic("Lizard Man", "The T-Rex", 2.0)
Comic("Water Woman", "Saving the ocean", 3.20)
Comic("Water Woman", "Saving the sea", 3.50)
Comic("Water Woman", "Saving the coast", 3.0)
Comic("Super Dude", "Saving the People", 1.75)
Comic("Super Dude", "Saving the World", 1.80)

welcome_screen()
