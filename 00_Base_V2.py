# # # import sys
# # # from tkinter import *
# # #
# # # # Comic storage
# # # comics = []
# # # sd = []
# # # ww = []
# # # lm = []
# # #
# # # root = Tk()
# # #
# # #
# # # class Comic:
# # #     def __init__(self, comic_type, name, price):
# # #         self.comic_type = comic_type
# # #         self.name = name
# # #         self.price = price
# # #         comics.append(self)
# # #         if comic_type == "Lizard Man":
# # #             lm.append(self)
# # #         elif comic_type == "Water Woman":
# # #             ww.append(self)
# # #         elif comic_type == "Super Dude":
# # #             sd.append(self)
# # #         else:
# # #             print("INVALID")
# # #
# # #     def display_info(self):
# # #         print(f"#################\n"
# # #               f"Name: {self.name}\n"
# # #               f"Type: {self.comic_type}\n"
# # #               f"Price: ${self.price}\n")
# # #
# # #
# # # def print_comics():
# # #     print("FULL INVENTORY")
# # #     print("#################\n")
# # #     print("STOCK NUMBERS: \n"
# # #           "#################\n"
# # #           f"Water Woman: {len(ww)}\n"
# # #           f"Super Dude: {len(sd)}\n"
# # #           f"Lizard Man: {len(lm)}\n")
# # #     for comic in comics:
# # #         comic.display_info()
# # #
# # #
# # # def add_comic():
# # #     add_window = Toplevel(root)
# # #     add_window.title = "ADD NEW COMIC"
# # #
# # #     # Entry widgets for user input
# # #     Label(add_window, text="Enter Comic Name: ").pack(side=TOP, fill=X)
# # #     name_entry = Entry(add_window)
# # #     name_entry.pack(side=TOP, fill=X)
# # #     Label(add_window, text="Enter Comic Type: ").pack(side=TOP, fill=X)
# # #     type_entry = Entry(add_window)
# # #     type_entry.pack(side=TOP, fill=X)
# # #     Label(add_window, text="Enter Comic Price: ").pack(side=TOP, fill=X)
# # #     price_entry = Entry(add_window)
# # #     price_entry.pack(side=TOP, fill=X)
# # #
# # #     def add_new_comic():
# # #         # Get user input from Entry widgets
# # #         name = name_entry.get()
# # #         comic_type = type_entry.get()
# # #         price = float(price_entry.get())  # Convert price to float
# # #
# # #         # Create new Comic object
# # #         new_comic = Comic(comic_type, name, price)
# # #
# # #         # Clear Entry widgets after adding comic
# # #         name_entry.delete(0, END)
# # #         type_entry.delete(0, END)
# # #         price_entry.delete(0, END)
# # #
# # #         # Close the add window
# # #         add_window.destroy()
# # #
# # #     # Button to add the new comic
# # #     add_button = Button(add_window, text="Add Comic", command=add_new_comic)
# # #     add_button.pack()
# # #
# # #
# # # def count_comic():
# # #     add_window = Toplevel(root)
# # #     root.title = "COMIC STOCK"
# # #
# # #     def show():
# # #         label.config(text=f"Selected comic type: {clicked.get()}")
# # #
# # #     Label(root,
# # #           text="Select comic type to show stock or press 'Inventory' to print a full list of all comic details").pack()
# # #
# # #     options = ["Lizard Man", "Water Woman", "Super Dude"]
# # #     clicked = StringVar()
# # #     clicked.set("Lizard Man")
# # #     drop = OptionMenu(root, clicked, *options)
# # #     drop.pack()
# # #
# # #     label = Label(root, text=" ")
# # #     label.pack()
# # #
# # #
# # #     def show_stock_count():
# # #         if clicked.get() == "Water Woman":
# # #             stock_count = len(ww)
# # #         elif clicked.get() == "Super Dude":
# # #             stock_count = len(sd)
# # #         else:
# # #             stock_count = len(lm)
# # #         stock_label.config(text=f"There are {stock_count} comics in stock")
# # #
# # #     stock_label = Label(root, text="")
# # #     stock_label.pack()
# # #
# # #     Button(root, text="SHOW COMIC STOCK", command=show_stock_count).pack()
# # #     Button(root, text="INVENTORY", command=print_comics).pack(side=BOTTOM)
# # #     Button(root, text="ADD STOCK", command=add_comic).pack(side=BOTTOM)
# # #
# # #
# # # def sell():
# # #     print("Sell Comics")
# # #
# # #
# # # def restock():
# # #     print("Restock Comics")
# # #
# # #
# # # def exit():
# # #     print("Goodbye")
# # #     sys.exit()
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# # import tkinter as tk
# #
# #
# # def restock():
# #     print("Restock Comics")
# #
# #
# # class ComicScreens:
# #     def __init__(self, master):
# #         self.master = master
# #         self.master.title("Comic Book Store")
# #
# #         # Comic storage
# #         self.comics = []
# #         self.sd = []
# #         self.ww = []
# #         self.lm = []
# #
# #         self.welcome()
# #
# #         class Comic:
# #             def __init__(self, comic_type, name, price):
# #                 self.comic_type = comic_type
# #                 self.name = name
# #                 self.price = price
# #                 comics.append(self)
# #                 if comic_type == "Lizard Man":
# #                     lm.append(self)
# #                 elif comic_type == "Water Woman":
# #                     ww.append(self)
# #                 elif comic_type == "Super Dude":
# #                     sd.append(self)
# #                 else:
# #                     print("INVALID")
# #
# #             def display_info(self):
# #                 print(f"#################\n"
# #                       f"Name: {self.name}\n"
# #                       f"Type: {self.comic_type}\n"
# #                       f"Price: ${self.price}\n")
# #
# #         def print_comics():
# #             print("FULL INVENTORY")
# #             print("#################\n")
# #             print("STOCK NUMBERS: \n"
# #                   "#################\n"
# #                   f"Water Woman: {len(ww)}\n"
# #                   f"Super Dude: {len(sd)}\n"
# #                   f"Lizard Man: {len(lm)}\n")
# #             for comic in comics:
# #                 comic.display_info()
# #
# #         def add_comic(self):
# #             add_window = tk.Toplevel(self.master)
# #             add_window.title("ADD NEW COMIC")
# #             # Entry widgets for user input
# #             Label(add_window, text="Enter Comic Name: ").pack(side=TOP, fill=X)
# #             name_entry = Entry(add_window)
# #             name_entry.pack(side=TOP, fill=X)
# #             Label(add_window, text="Enter Comic Type: ").pack(side=TOP, fill=X)
# #             type_entry = Entry(add_window)
# #             type_entry.pack(side=TOP, fill=X)
# #             Label(add_window, text="Enter Comic Price: ").pack(side=TOP, fill=X)
# #             price_entry = Entry(add_window)
# #             price_entry.pack(side=TOP, fill=X)
# #
# #             def add_new_comic():
# #                 # Get user input from Entry widgets
# #                 name = name_entry.get()
# #                 comic_type = type_entry.get()
# #                 price = float(price_entry.get())  # Convert price to float
# #
# #                 # Create new Comic object
# #                 new_comic = Comic(comic_type, name, price)
# #
# #                 # Clear Entry widgets after adding comic
# #                 name_entry.delete(0, END)
# #                 type_entry.delete(0, END)
# #                 price_entry.delete(0, END)
# #
# #                 # Close the add window
# #                 add_window.destroy()
# #
# #             # Button to add the new comic
# #             add_button = Button(add_window, text="Add Comic", command=add_new_comic)
# #             add_button.pack()
# #
# #                 # Add comic widgets here
# #
# #         def show_stock(self):
# #             stock_window = tk.Toplevel(self.master)
# #             stock_window.title("COMIC STOCK")
# #
# #                 # Show stock widgets here
# #
# #         def sell(self):
# #             print("Sell Comics")
# #
# #         def exit_app(self):
# #             print("Goodbye")
# #             self.master.quit()
# #
# #         def count_comic():
# #             add_window = Toplevel(root)
# #             root.title = "COMIC STOCK"
# #
# #             def show():
# #                 label.config(text=f"Selected comic type: {clicked.get()}")
# #
# #             Label(root,
# #                   text="Select comic type to show stock or press 'Inventory' to print a full list of all comic details").pack()
# #
# #             options = ["Lizard Man", "Water Woman", "Super Dude"]
# #             clicked = StringVar()
# #             clicked.set("Lizard Man")
# #             drop = OptionMenu(root, clicked, *options)
# #             drop.pack()
# #
# #             label = Label(root, text=" ")
# #             label.pack()
# #
# #             def show_stock_count():
# #                 if clicked.get() == "Water Woman":
# #                     stock_count = len(ww)
# #                 elif clicked.get() == "Super Dude":
# #                     stock_count = len(sd)
# #                 else:
# #                     stock_count = len(lm)
# #                 stock_label.config(text=f"There are {stock_count} comics in stock")
# #
# #             stock_label = Label(root, text="")
# #             stock_label.pack()
# #
# #             Button(root, text="SHOW COMIC STOCK", command=show_stock_count).pack()
# #             Button(root, text="INVENTORY", command=print_comics).pack(side=BOTTOM)
# #             Button(root, text="ADD STOCK", command=add_comic).pack(side=BOTTOM)
# #
# #     def welcome(self):
# #         welcome_label = tk.Label(self.master, text="Welcome to the Comic Book Store", font=("Times", 20, "bold"))
# #         welcome_label.pack()
# #
# #         options_label = tk.Label(self.master, text="Please choose an option:", font=("Arial", 10, "bold"))
# #         options_label.pack()
# #
# #         sell_button = tk.Button(self.master, text="Sell Comics", command=self.sell)
# #         sell_button.pack()
# #
# #         show_stock_button = tk.Button(self.master, text="Show Stock", command=self.show_stock)
# #         show_stock_button.pack()
# #
# #         restock_button = tk.Button(self.master, text="Restock Comics", command=self.add_comic)
# #         restock_button.pack()
# #
# #         exit_button = tk.Button(self.master, text="Exit", command=self.exit_app)
# #         exit_button.pack()
# #
# #
# #
# # root = tk.Tk()
# # app = ComicScreens(root)
# # root.mainloop()
# #
# # # MAIN ROUTINE
# # Comic("Lizard Man", "Saving the lizards", 2.30)
# # Comic("Lizard Man", "The slippery snake", 2.50)
# # Comic("Lizard Man", "The T-Rex", 2.0)
# # Comic("Water Woman", "Saving the ocean", 3.20)
# # Comic("Water Woman", "Saving the sea", 3.50)
# # Comic("Water Woman", "Saving the coast", 3.0)
# # Comic("Super Dude", "Saving the People", 1.75)
# # Comic("Super Dude", "Saving the World", 1.80)
#
# import tkinter as tk
# from tkinter import *
#
#
# class Comic:
#     def __init__(self, comic_type, name, price):
#         self.comic_type = comic_type
#         self.name = name
#         self.price = price
#         comics.append(self)
#         if comic_type == "Lizard Man":
#             lm.append(self)
#         elif comic_type == "Water Woman":
#             ww.append(self)
#         elif comic_type == "Super Dude":
#             sd.append(self)
#         else:
#             print("INVALID")
#
#     def display_info(self):
#         print(f"#################\n"
#               f"Name: {self.name}\n"
#               f"Type: {self.comic_type}\n"
#               f"Price: ${self.price}\n")
#
#
# class ComicScreens:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Comic Book Store")
#
#         self.comics = []
#         self.sd = []
#         self.ww = []
#         self.lm = []
#
#         self.create_widgets()
#
#     def create_widgets(self):
#         welcome_label = tk.Label(self.master, text="Welcome to the Comic Book Store", font=("Times", 20, "bold"))
#         welcome_label.pack()
#
#         options_label = tk.Label(self.master, text="Please choose an option:", font=("Arial", 10, "bold"))
#         options_label.pack()
#
#         sell_button = tk.Button(self.master, text="Sell Comics", command=self.sell)
#         sell_button.pack()
#
#         show_stock_button = tk.Button(self.master, text="Show Stock", command=self.show_stock)
#         show_stock_button.pack()
#
#         restock_button = tk.Button(self.master, text="Restock Comics", command=self.add_comic)
#         restock_button.pack()
#
#         exit_button = tk.Button(self.master, text="Exit", command=self.exit_app)
#         exit_button.pack()
#
#     def add_comic(self):
#         add_window = tk.Toplevel(self.master)
#         add_window.title("ADD NEW COMIC")
#
#         # Entry widgets for user input
#         Label(add_window, text="Enter Comic Name: ").pack(side=TOP, fill=X)
#         name_entry = Entry(add_window)
#         name_entry.pack(side=TOP, fill=X)
#         Label(add_window, text="Enter Comic Type: ").pack(side=TOP, fill=X)
#         type_entry = Entry(add_window)
#         type_entry.pack(side=TOP, fill=X)
#         Label(add_window, text="Enter Comic Price: ").pack(side=TOP, fill=X)
#         price_entry = Entry(add_window)
#         price_entry.pack(side=TOP, fill=X)
#
#         def add_new_comic():
#             # Get user input from Entry widgets
#             name = name_entry.get()
#             comic_type = type_entry.get()
#             price = float(price_entry.get())  # Convert price to float
#
#             # Create new Comic object
#             new_comic = Comic(comic_type, name, price)
#
#             # Clear Entry widgets after adding comic
#             name_entry.delete(0, END)
#             type_entry.delete(0, END)
#             price_entry.delete(0, END)
#
#             # Close the add window
#             add_window.destroy()
#
#         # Button to add the new comic
#         add_button = Button(add_window, text="Add Comic", command=add_new_comic)
#         add_button.pack()
#
#     def show_stock(self):
#         stock_window = tk.Toplevel(self.master)
#         stock_window.title("COMIC STOCK")
#
#         def show():
#
#             label.config(text=f"Selected comic type: {clicked.get()}")
#
#         Label(root,
#               text="Select comic type to show stock or press 'Inventory' to print a full list of all comic details").pack()
#
#         options = ["Lizard Man", "Water Woman", "Super Dude"]
#         clicked = StringVar()
#         clicked.set("Lizard Man")
#         drop = OptionMenu(root, clicked, *options)
#         drop.pack()
#
#         label = Label(root, text=" ")
#         label.pack()
#
#
#         def show_stock_count():
#             if clicked.get() == "Water Woman":
#                 stock_count = len(ww)
#             elif clicked.get() == "Super Dude":
#                 stock_count = len(sd)
#             else:
#                 stock_count = len(lm)
#             stock_label.config(text=f"There are {stock_count} comics in stock")
#
#         stock_label = Label(root, text="")
#         stock_label.pack()
#
#         Button(root, text="SHOW COMIC STOCK", command=show_stock_count).pack()
#         Button(root, text="INVENTORY", command=print_comics).pack(side=BOTTOM)
#         Button(root, text="ADD STOCK", command=add_comic).pack(side=BOTTOM)
#         # Show stock widgets here
#
#     def sell(self):
#         print("Sell Comics")
#
#     def exit_app(self):
#         print("Goodbye")
#         self.master.quit()
#
#
# root = tk.Tk()
# app = ComicScreens(root)
# root.mainloop()
#
# # MAIN ROUTINE
# comics = []
# sd = []
# ww = []
# lm = []
#
# Comic("Lizard Man", "Saving the lizards", 2.30)
# Comic("Lizard Man", "The slippery snake", 2.50)
# Comic("Lizard Man", "The T-Rex", 2.0)
# Comic("Water Woman", "Saving the ocean", 3.20)
# Comic("Water Woman", "Saving the sea", 3.50)
# Comic("Water Woman", "Saving the coast", 3.0)
# Comic("Super Dude", "Saving the People", 1.75)
# Comic("Super Dude", "Saving the World", 1.80)

import tkinter as tk
from tkinter import *

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

class ComicScreens:
    def __init__(self, master):
        self.master = master
        self.master.title("Comic Book Store")

        self.comics = []
        self.sd = []
        self.ww = []
        self.lm = []

        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self.master, text="Welcome to the Comic Book Store", font=("Times", 20, "bold"))
        welcome_label.pack()

        options_label = tk.Label(self.master, text="Please choose an option:", font=("Arial", 10, "bold"))
        options_label.pack()

        sell_button = tk.Button(self.master, text="Sell Comics", command=self.sell)
        sell_button.pack()

        show_stock_button = tk.Button(self.master, text="Show Stock", command=self.show_stock)
        show_stock_button.pack()

        restock_button = tk.Button(self.master, text="Restock Comics", command=self.add_comic)
        restock_button.pack()

        exit_button = tk.Button(self.master, text="Exit", command=self.exit_app)
        exit_button.pack()

    def add_comic(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("ADD NEW COMIC")

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

            # Clear Entry widgets after adding comic
            name_entry.delete(0, END)
            type_entry.delete(0, END)
            price_entry.delete(0, END)

            # Close the add window
            add_window.destroy()

        # Button to add the new comic
        add_button = Button(add_window, text="Add Comic", command=add_new_comic)
        add_button.pack()

    def show_stock(self):
        stock_window = tk.Toplevel(self.master)
        stock_window.title("COMIC STOCK")

        Label(stock_window,
              text="Select comic type to show stock or press 'Inventory' to print a full list of all comic details").pack()

        options = ["Lizard Man", "Water Woman", "Super Dude"]
        clicked = StringVar()
        clicked.set("Lizard Man")
        drop = OptionMenu(stock_window, clicked, *options)
        drop.pack()

        label = Label(stock_window, text=" ")
        label.pack()

        def show_stock_count():
            stock_count = 0
            comic_type = clicked.get()
            if comic_type == "Water Woman":
                stock_count = len(ww)
            elif comic_type == "Super Dude":
                stock_count = len(sd)
            elif comic_type == "Lizard Man":
                stock_count = len(lm)
            stock_label.config(text=f"There are {stock_count} comics in stock")

        stock_label = Label(stock_window, text="")
        stock_label.pack()

        Button(stock_window, text="SHOW COMIC STOCK", command=show_stock_count).pack()

    def sell(self):
        print("Sell Comics")

    def exit_app(self):
        print("Goodbye")
        self.master.quit()


root = tk.Tk()
app = ComicScreens(root)
root.mainloop()

# MAIN ROUTINE
comics = []
sd = []
ww = []
lm = []

Comic("Lizard Man", "Saving the lizards", 2.30)
Comic("Lizard Man", "The slippery snake", 2.50)
Comic("Lizard Man", "The T-Rex", 2.0)
Comic("Water Woman", "Saving the ocean", 3.20)
Comic("Water Woman", "Saving the sea", 3.50)
Comic("Water Woman", "Saving the coast", 3.0)
Comic("Super Dude", "Saving the People", 1.75)
Comic("Super Dude", "Saving the World", 1.80)
