comics = []
lizard = []
ww = []
sd = []


class Comic:
    def __init__(self, comic_type, name, price):
        self.comic_type = comic_type
        self.name = name
        self.price = price
        comics.append(self)
        if type == "Lizard Man":
            lizard.append(self)
        elif type == "Water Woman":
            ww.append(self)
        elif type == "Super Dude":
            sd.append(self)
        else:
            print("invalid")


def display_comics(self):
    print(f"#################\n"
          f"Name: {self.name}\n"
          f"Type: {self.type}\n"
          f"Price: ${self.price}\n")


def print_comics():
    for comic in comics:
        display_comics()


# MAIN ROUTINE
print_comics()
