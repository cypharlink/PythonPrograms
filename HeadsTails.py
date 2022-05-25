import random

start = int(input("Enter 0 to start! : "))

if start == 0:
    ran = random.randint(0, 1)
    if ran == 0:
        print("Heads")
    else:
        print("Tails")