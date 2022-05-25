print("============================")
print("WELCOME TO PIZZA DELICERIES!")
print("============================")

def line():
    print("\n--------------\n")

line()

size = input("What size pizza do you want? S, M or L\n")

line()

add_pepperoni = input("Do you want pepperoni? Y or N\n")

line()

extra_cheese = input("Do you want extra cheese? Y or N\n")

class Price:
    def __init__(self, price, peper, cheese):
        if add_pepperoni == "Y":
            price += peper
            if extra_cheese == "Y":
                price += cheese
                print(f"Total price is ${price}")
            else:
                print(f"Total price is ${price}") 
        else:
            if extra_cheese == "Y":
                price += cheese
                print(f"Total price is ${price}")
            else:
                print(f"Total price is ${price}")


if size == "S":
    Price = Price(15, 2, 1)
elif size == "M":
    Price = Price(20, 3, 1)
elif size == "L":
    Price = Price(25, 3, 1)