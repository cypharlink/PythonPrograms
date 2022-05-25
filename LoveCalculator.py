import time
import sys

def anim():
    print("Loading:")
    animation = ["❤ ", "❤ ❤ ", "❤ ❤ ❤ ", "❤ ❤ ❤ ❤ ", "❤ ❤ ❤ ❤ ❤ "]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()



logo = '''

────────╠███████───███████╠─────────────
───────╠█████████─╠█████████────────────
───────█████████████████████╠───────────
──────╠██████████████████████───────────
──────███████████████████████───────────
──────███████████████████████╠──────────
──────███████████████████████╠──────────
──────███████████████████████───────────
──────╠██████████████████████───────────
──────╠█████████████████████╠───────────
───────█████████████████████────────────
───────╠███████████████████╠────────────
────────╠███████████──╠████─────────────
─────────██████████─────╠█╠─────────────
─────────╠████████──███─────────────────
──────────╠███████─╠█████───────────────
─────╠╠────╠██████─╠███████─────────────
──█████╠────╠█████╠─╠███████╠───────────
─╠███████╠█╠─╠█████╠──████████╠─────────
╠███████████╠──█████───╠████████╠───────
╠█████████████──╠██╠─────╠████████╠─────
─██████████████───────────█████████╠────
──╠█████████████╠───────╠███████████╠───
───╠█████████████████████████████████╠──
────╠█████████████████████████████████──
─────╠█████████████████████████████████─
───────████████████████████████████████╠
────────╠███████████████████████████████
─────────╠██████████████████████████████
───────────█████████████████████████████
────────────╠██████████████████████████─
───────────────────────────────╠██████──
─────────────────────────────────███╠───
─────────────────────────────────╠█╠────


'''

print(logo)

def dot():
    print("\n-----------------------------\n")

dot()

your_name = input("What is your name?\n  ")

dot()

their_name = input("What is their name?\n  ")

add_name = your_name.upper() + their_name.upper()

num_t = add_name.count("T")
num_r = add_name.count("R")
num_u = add_name.count("U")
num_e = add_name.count("E")

num_l = add_name.count("L")
num_o = add_name.count("O")
num_v = add_name.count("V")
num_e = add_name.count("E")

add_true = num_t + num_r + num_u + num_e
add_love = num_l + num_o + num_v + num_e

scoreStr = str(add_true) + str(add_love)
scoreInt = int(scoreStr)

dot()

if scoreInt < 10 or scoreInt > 90:
    anim()
    print(f"\n\nYour score is {scoreInt}%, you go together like coke and mentos.")
elif scoreInt >= 40 and scoreInt <= 80:
    anim()
    print(f"\n\nYour score is {scoreInt}%, you are born for each other.")
else:
    anim()
    print(f"\n\nYour score is {scoreInt}%.")