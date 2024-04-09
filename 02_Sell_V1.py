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
        if type == "Lizard Man" or type == "Water Woman" or type == "Super Dude":
            comics.append(self)
        else:
            print("INVALID")


def display_comics(self):
    print(f"#################\n"
          f"Name: {self.name}\n"
          f"Type: {self.type}\n"
          f"Price: ${self.price}\n")


def print_comics():
    for comic in comics:
        comic.display_comics()


def count_comic():
    ww_count = 0
    sd_count = 0
    lm_count = 0
    for comic in comics:
        if comic.comic_type == "Water Woman":
            ww_count += 1
        elif comic.comic_type == "Super Dude":
            sd_count += 1
        elif comic.comic_type == "Lizard Man":
            lm_count += 1
        else:
            comics.remove(comic)


# MAIN ROUTINE
print_comics()
