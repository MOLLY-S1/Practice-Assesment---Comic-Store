"""Version !
This code will create a welcome screen, using TKinter"""

from tkinter import *
root = Tk()

root.title("WELCOME")
welcome = Label(root, bg="White", fg="Black", text="Welcome to the Comic Book Store",
                font=("Times", 20, "bold"))
welcome.pack()

sell = Button(root, text="Sell Comics", command=print("Sell Comic"))
show = Button(root, text="Show Stock", command=print("Show Stock"))
restock = Button(root, text="Restock Comics", command=print("Restock Comics"))
leave = Button(root, text="Exit", command=print("Exit"))
sell.pack()
show.pack()
restock.pack()
leave.pack()


root.mainloop()
