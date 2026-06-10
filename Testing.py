import tkinter as tk
import sys

root = tk.Tk()
root.title("MeowCalculator")
root.geometry("600x600")
root.configure(bg="#1f242a")

# some acsii arts
ascii_cat = r"""
   /\_/\  (
   ( ^.^ ) _)
   \"/  (
( | | )
(__d b__)
"""

acsii_cat_bye = r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \  `.___________|/
  `--'   `--'
"""

acsii_cat_surprise = r"""
    /\_____/\   !!!!
   /  O   O  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
"""

acsii_cat_sad = r"""
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
"""
wcatlabel = tk.Label(root, font=("Consolas", 14), bg="#1f242a", fg="#f1c40f", text=ascii_cat)
wcatlabel.pack(padx=30, pady=30)
wcatlabel.pack()
hilabel = tk.Label(root, text="Hello! Welcome to meow calculator...")
hilabel.pack()

# after doing math
def after_math_menu(layout, op_name):
    typeslow_print("\nWhat do you wanna do after?")
    formatted_text = layout.format(op=op_name)
    for line in formatted_text.splitlines():
        print(line)
        time.sleep(0.3)
    choice = input("Enter your choice (1-3): ")
    if choice == "3":
        print(acsii_cat_bye)
        print("See you then!")
        time.sleep(4)
        sys.exit()
    return choice

# after picking 1 in q2
def ask_retry():
    while True:
        retry = str(input("Do you wanna try again? y/n: ")).strip().lower()
        if retry == "y":
            return True
        elif retry == "n":
            return False
        else:
            print("\033[31mOnly choose y or n! Nothing else... TT\033[0m")
            time.sleep(2)

# for errors inside the operations
def user_error_input():
    while True: 
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            return num1, num2
        except ValueError:
            print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
            time.sleep(2)
        if not ask_retry():
            return None, None

#addition function
def addition():
    typeslow_print("\n--- You chose Addition Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        num1, num2 = user_error_input()
        if num1 is None:
            return
        time.sleep(0.5)
        typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
        typeslow_print("...", delay=0.5)
        time.sleep(1)
        result = num1 + num2
        print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
        time.sleep(1.5)
        user_action = after_math_menu(q2, "Add")
        if user_action == "1":
            continue
        elif user_action == "2":
            return

#subtraction function
def subtraction():
    typeslow_print("\n--- You chose Subtraction Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        num1, num2 = user_error_input()
        if num1 is None:
            return
        time.sleep(0.5)
        typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
        typeslow_print("...", delay=0.5)
        time.sleep(1)
        result = num1 - num2
        print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
        time.sleep(1.5)
        user_action = after_math_menu(q2, "Subtract")
        if user_action == "1":
            continue
        elif user_action == "2":
            return

# multiply function
def multiplication():
    typeslow_print("\n--- You chose Multiplication Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        num1, num2 = user_error_input()
        if num1 is None:
            return
        time.sleep(0.5)
        typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
        typeslow_print("...", delay=0.5)
        time.sleep(1)
        result = num1 / num2
        print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
        time.sleep(1.5)
        user_action = after_math_menu(q2, "Multiply")
        if user_action == "1":
            continue
        elif user_action == "2":
            return

# divide function
def division():
    typeslow_print("\n--- You chose Division Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        num1, num2 = user_error_input()
        if num1 is None:
            return
        if num2 == 0:
            print("\033[31mError: You can't divide by zero! ₍^. .^₎Ⳋ\033[0m")
            if not ask_retry():
                return
            continue
        time.sleep(0.5)
        typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
        typeslow_print("...", delay=0.5)
        time.sleep(1)
        result = num1 / num2
        print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
        time.sleep(1.5)
        user_action = after_math_menu(q2, "Divide")
        if user_action == "1":
            continue
        elif user_action == "2":
            return

# leaving so soon?
def exit():
    print(acsii_cat_surprise)
    typeslow_print("--- You chose...", delay=0.1, end_line=False)
    typeslow_print(" what?! ---", delay=0.01)
    time.sleep(1)
    for line in acsii_cat_sad.splitlines():
        print(line)
        time.sleep(0.1)
    typeslow_print("\033[31mThe cat seems to be judging you.\033[0m\n", delay=0.1875)
    typeslow_print("You're leaving already? No fun... meow.")
    time.sleep(7)
    sys.exit()

root.mainloop() #this ends the code here
