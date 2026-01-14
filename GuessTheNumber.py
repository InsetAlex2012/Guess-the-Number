#https://github.com/TkinterEP/ttkthemes/tree/master/screenshots

import random
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

random_number = 0
max_number = 200

tries = 0

def start_game():
    global difficulty, random_number, max_number, spin_box

    root.title("Guess the Number! - Game")

    start_button.destroy()
    name_label.pack_forget()
    radio_1.destroy()
    radio_2.destroy()
    radio_3.destroy()
    title_label.config(font = ("Rubik Mono One", 10))
    image_label.pack(pady = 20)


    difficulty = difficulty.get()

    if difficulty == 1:
        random_number = random.randint(0,50)
        max_number = 50
    elif difficulty == 2:
        random_number = random.randint(0, 100)
        max_number = 100
    elif difficulty == 3:
        random_number = random.randint(0,200)
        max_number = 200


    spin_box.pack(pady = 40)
    spin_box.config(to=max_number)

    tries_label.pack(pady = 10)

    guess_button.pack()
    name_label.configure(font = ("Rubik Mono One", 10), text = "By AlexIsNotInset")
    name_label.pack(pady = 6)

def guess():
    global tries, random_number, spin_box, difficulty

    try:
        spin_box_value = int(spin_box.get())
    except ValueError:
        image_label.configure(image=question_img)
        root.title("Guess the Number! - Invalid")
        return

    tries += 1
    tries_label.configure(text=f"Tries: {tries}")

    if difficulty == 1:
        if 1 <= tries <= 2:
            tries_label.configure(foreground = "green")
        elif 3 <= tries <= 4:
            tries_label.configure(foreground = "gold")
        elif 5 <= tries <= 6:
            tries_label.configure(foreground = "red")
        else:
            tries_label.configure(foreground = "black")

    if difficulty == 2:
        if 1 <= tries <= 3:
            tries_label.configure(foreground = "green")
        elif 4 <= tries <= 5:
            tries_label.configure(foreground = "gold")
        elif 6 <= tries <= 8:
            tries_label.configure(foreground = "red")
        else:
            tries_label.configure(foreground = "black")

    if difficulty == 3:
        if 1 <= tries <= 4:
            tries_label.configure(foreground = "green")
        elif 5 <= tries <= 7:
            tries_label.configure(foreground = "gold")
        elif 8 <= tries <= 11:
            tries_label.configure(foreground = "red")
        else:
            tries_label.configure(foreground = "black")



    if spin_box_value > random_number:
        image_label.configure(image = down_img)
        root.title("Guess the Number! - Lower")

    elif spin_box_value < random_number:
        image_label.configure(image = up_img)
        root.title("Guess the Number! - Higher")

    else:
        image_label.configure(image = correct_img)
        guess_button.configure(state = "disabled")
        root.title("Guess the Number! - Victory")

        spin_box.destroy()

        victory_label = Label(root, text = "You win!", foreground = "green", font = ("Rubik Mono One", 30))
        victory_label.pack(pady = 20)

        tries_label.pack_forget()
        tries_label.pack()
        tries_label.configure(font = ("Rubik Mono One", 15))

        guess_button.pack_forget()
        guess_button.pack(pady = 20)

        name_label.pack_forget()
        name_label.pack()


root = ThemedTk(theme ="breeze")
root.geometry("600x400")
root.title("Guess the Number! - Python Project")
root.configure(themebg ="breeze")
root.resizable(False, False)

up_img = PhotoImage(file = "up.png")
down_img = PhotoImage(file = "down.png")
correct_img = PhotoImage(file = "correct.png")
question_img = PhotoImage(file = "question.png")
dice_img = PhotoImage(file = "dice.png")

root.iconphoto(True, dice_img)

image_label = Label(root, image = dice_img)


title_label = Label(root, text = "Guess the number!", background = "light blue", font = ("Rubik Mono One", 30))
title_label.pack()

difficulty = IntVar()
difficulty.set(2)

radio_style = Style()
radio_style.configure("TRadiobutton", font=("Rubik Mono One", 10))

spin_box = Spinbox(root, from_ = 0, to = max_number)

radio_1 = Radiobutton(root, text = "Easy: 0-50", value = 1, variable = difficulty, style = "TRadiobutton", cursor = "hand2")
radio_1.place(x=10, y=100)

radio_2 = Radiobutton(root, text = "Medium: 0-100", value = 2, variable = difficulty, style = "TRadiobutton", cursor = "hand2")
radio_2.place(x=220, y=100)

radio_3 = Radiobutton(root, text = "Hard: 0-200", value = 3, variable = difficulty, style = "TRadiobutton", cursor = "hand2")
radio_3.place(x=440, y=100)


button_style = Style()
button_style.configure("TButton", font = ("Rubik Mono One", 20))

tries_label = Label(root, text = f"Tries: {tries}", font=("Rubik Mono One", 8))


start_button = Button(root, text = "Start Game!", style = "TButton", command = start_game, cursor = "hand2")
start_button.pack(expand = True)

guess_button = Button(root, text = "Guess!", style = "TButton", command = guess, cursor = "hand2")

name_label = Label(root, text = "By AlexIsNotInset!", font = ("Rubik Mono One", 15))
name_label.pack()


root.mainloop()
