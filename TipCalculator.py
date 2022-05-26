print("==============================")
print("WELCOME TO THE TIP CALCULATOR")
print("==============================")

print("")

total_bill = input("What was the total bill? $")

print("------------------------------")

split_bill = input("How many people to split the bill? ")

print("------------------------------")

percentage = input("What percentage tip would you like to give? 10, 12 , or 15? ")

percent_convert = percentage[:2]

sb = float(total_bill) / int(split_bill)

if (percent_convert == "10"):
    pb = (sb/100) * 10
    tpb = pb + sb
    fl = "{:.2f}".format(tpb)
    print("------------------------------")
    print(f"Each person should pay: ${fl}")
elif (percent_convert == "12"):
    pb = (sb/100) * 12
    tpb = pb + sb
    fl = "{:.2f}".format(tpb)
    print("------------------------------")
    print(f"Each person should pay: ${fl}")
elif (percent_convert == "15"):
    pb = (sb/100) * 15
    tpb = pb + sb
    fl = "{:.2f}".format(tpb)
    print("------------------------------")
    print(f"Each person should pay: ${fl}")
else:
    print("choose tip from 10, 12 or 15")