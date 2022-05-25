print("=======================")
print("WELCOME TO TREASURY MAP")
print("=======================")
print("")

def dot():
    print("")
    print("--------------------------------------")
    print("")

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

dot()

num = input("Where do you want to put the treasure? ")

dot()

column_num = int(num[0])
row_num = int(num[1])

c = column_num - 1
r = row_num - 1

map[r][c] = "X"

print(f"{row1}\n{row2}\n{row3}")