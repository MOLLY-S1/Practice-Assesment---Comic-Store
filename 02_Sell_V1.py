""" Version 1
Using a function and count to count comics per type"""

comics = []


class Comic:
    def __init__(self, comic_type, name, price):
        self.comic_type = comic_type
        self.name = name
        self.price = price
        if comic_type == "Lizard Man" or comic_type == "Water Woman" or comic_type == "Super Dude":
            comics.append(self)
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
