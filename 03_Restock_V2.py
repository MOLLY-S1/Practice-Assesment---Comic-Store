""" ADDING NEW COMICS - now a function"""


def add_comic():
    # add comic
    name = input("Enter comic name: ").title()
    comic_type = input("Enter Comic type: ").title()
    price = float("Enter comic price: ")
    Comic(name, comic_type, price)
