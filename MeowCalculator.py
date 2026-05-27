# adding some imports
import time
import sys
import math

# some acsii arts
acsii_cat = r"""
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

# Some questions
q1 = """
o--------------------o
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
o--------------------o
"""

q2 = """
o~~~~~~~~~~~~~~~~~~~~o
1. {op} more numbers
2. Go back to the menu
3. Exit
o~~~~~~~~~~~~~~~~~~~~o
"""

# functions to call in main code

# for typewriting effect
def typeslow_print(text, delay=0.05, end_line =True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    if end_line:
        print()

# after doing math
def after_math_menu(layout, op_name):
    typeslow_print("\nWhat do you wanna do after?")
    formatted_text = layout.format(op=op_name)
    for line in formatted_text.splitlines():
        print(line)
        time.sleep(0.3)
    choice = input("Enter your choice (1-3): ")
    return choice

#addition function
def addition():
    typeslow_print("\n--- You chose Addition Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            time.sleep(0.5)
            typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
            typeslow_print("...", delay=0.5)
            time.sleep(1)
            result = num1 + num2
            print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
            time.sleep(1.5)

            while True:
                user_action = after_math_menu(q2, "Add")

                if user_action == "1":
                    break
                elif user_action == "2":
                    return
                elif user_action == "3":
                    print(acsii_cat_bye)
                    print("See you then!")
                    time.sleep(4)
                    sys.exit()
                else:
                    print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
                    time.sleep(3)
            continue

        except ValueError:
            print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
            time.sleep(3)
            while True:
                retry = str(input("Do you wanna try again? y/n "))
                if retry == "y":
                    break
                elif retry == "n":
                    return
                else:
                    print("\033[31mOnly choose y or n! Nothing else... TT\033[0m")
                    time.sleep(3)

#subtraction function
def subtraction():
    typeslow_print("\n--- You chose Subtraction Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            time.sleep(0.5)
            typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
            typeslow_print("...", delay=0.5)
            time.sleep(1)
            result = num1 - num2
            print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
            time.sleep(1.5)

            while True:
                user_action = after_math_menu(q2, "Subtract")

                if user_action == "1":
                    break
                elif user_action == "2":
                    return
                elif user_action == "3":
                    print(acsii_cat_bye)
                    print("See you then!")
                    time.sleep(4)
                    sys.exit()
                else:
                    print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
                    time.sleep(3)
            continue

        except ValueError:
            print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
            time.sleep(3)
            while True:
                retry = str(input("Do you wanna try again? y/n "))
                if retry == "y":
                    break
                elif retry == "n":
                    return
                else:
                    print("\033[31mOnly choose y or n! Nothing else... TT\033[0m")
                    time.sleep(3)

# multiply function
def multiplication():
    typeslow_print("\n--- You chose Multiplication Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            time.sleep(0.5)
            typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
            typeslow_print("...", delay=0.5)
            time.sleep(1)
            result = num1 * num2
            print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
            time.sleep(1.5)

            while True:
                user_action = after_math_menu(q2, "Multiply")

                if user_action == "1":
                    break
                elif user_action == "2":
                    return
                elif user_action == "3":
                    print(acsii_cat_bye)
                    print("See you then!")
                    time.sleep(4)
                    sys.exit()
                else:
                    print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
                    time.sleep(3)
            continue

        except ValueError:
            print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
            time.sleep(3)
            while True:
                retry = str(input("Do you wanna try again? y/n "))
                if retry == "y":
                    break
                elif retry == "n":
                    return
                else:
                    print("\033[31mOnly choose y or n! Nothing else... TT\033[0m")
                    time.sleep(3)

# divide function
def division():
    typeslow_print("\n--- You chose Division Mode! ---")
    typeslow_print("Let's pick some numbers, meow!")
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            time.sleep(0.5)
            typeslow_print("\033[33mGive me a second to think /ᐠ˶>ﻌ<˶ᐟ\\ \033[0m")
            typeslow_print("...", delay=0.5)
            time.sleep(1)
            result = num1 / num2
            print(f"\033[32mThe answer is {result}, meow! ฅ^•⩊•^ ฅ\033[0m")
            time.sleep(1.5)

            while True:
                user_action = after_math_menu(q2, "Divide")

                if user_action == "1":
                    break
                elif user_action == "2":
                    return
                elif user_action == "3":
                    print(acsii_cat_bye)
                    print("See you then!")
                    time.sleep(4)
                    sys.exit()
                else:
                    print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
                    time.sleep(3)
            continue

        except ValueError:
            print("\033[31mPlease pick a number only! No letters or symbols. (╥﹏╥)\033[0m\n")
            time.sleep(3)
            while True:
                retry = str(input("Do you wanna try again? y/n "))
                if retry == "y":
                    break
                elif retry == "n":
                    return
                else:
                    print("\033[31mOnly choose y or n! Nothing else... TT\033[0m")
                    time.sleep(3)

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

# start code
print(acsii_cat)
typeslow_print("Hello! Welcome to meow calculator...", end_line=False)
sys.stdout.flush()
time.sleep(1)
typeslow_print(" except this calculator likes to ask questions.", delay=0.01)
time.sleep(0.5)
typeslow_print("So?")
sys.stdout.flush()
time.sleep(0.5)
while True:
    typeslow_print("\nWhat can I help you with?")
    for line in q1.splitlines():
        print(line)
        time.sleep(0.3)
    typeslow_print("Select a number of your choice, meow: ", end_line=False)
    choice = input()

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        multiplication()

    elif choice == "4":
        division()

    elif choice == "5":
        exit()
    else:
        print("\033[31mPlease choose within the provided numbers only (1-5). /ᐠﹷ ‸ ﹷ ᐟ\ﾉ\033[0m\n")
        time.sleep(3)