import random

print("====================================")
print("Welcome to the PyPassword Generator!")
print("====================================")

print("")

let_inp = int(input("How many letters would you like in your password?\n"))

print("")

sym_inp = int(input("How many symbols would you like?\n"))

print("")

num_inp = int(input("How many numbers would you like?\n"))

print("")

#### LETTERS
let_l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
"T", "U", "V", "W", "X", "Y", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
rl = random.sample(let_l, len(let_l))
let = ""
ll = []
for l in range(0, let_inp):
    let = rl[l]
    ll.append(let)

#### SYMBOLES
sym_l = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
rs = random.sample(sym_l, len(sym_l))
sym = ""
sl = []
for s in range(0, sym_inp):
    sym = rs[s]
    sl.append(sym)

#### NUMBERS
num_l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
rn = random.sample(num_l, len(num_l))
num = ""
nl = []
for n in range(0, num_inp):
    num = rn[n]
    nl.append(num)

for i in ll:
    sl.append(i)

for i in sl:
    nl.append(i)

random_password = random.sample(nl, len(nl))

rp = ""

for i in random_password:
    rp += i

print(f"Your password is: {rp}")