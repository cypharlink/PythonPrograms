import random
import re

name_string = input("Give me everybody's name, seperated by comma. ")

res1 = bool(re.search(r"\s", name_string))

if res1 == True:
    names = name_string.split(", ")
else:
    names = name_string.split(",")

print("")

num_item = len(names)
ran = random.randint(0, num_item-1)
person = names[ran]

print(f"{person} is going to buy mill today!")