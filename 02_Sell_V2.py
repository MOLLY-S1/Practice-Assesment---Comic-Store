""" Version 2
Using a list and length to count comics per type"""

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
    for comic in comics:
        comic.display_info()


def count_comic():
    ww_count = len(ww)
    sd_count = len(sd)
    lm_count = len(lm)
    print(ww_count)
    print(sd_count)
    print(lm_count)


# MAIN ROUTINE
Comic("Lizard Man", "Saving the lizards", 2.30)
Comic("Lizard Man", "The slippery snake", 2.50)
Comic("Lizard Man", "The T-Rex", 2.0)
Comic("Water Woman", "Saving the ocean", 3.20)
Comic("Water Woman", "Saving the sea", 3.50)
Comic("Water Woman", "Saving the coast", 3.0)
Comic("Super Dude", "Saving the People", 1.75)
Comic("Super Dude", "Saving the World", 1.80)
Comic("Super Dude", "Saving the School", 1.50)

print_comics()
count_comic()
