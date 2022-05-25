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
                        OOOOO          OOOOO
                       OO   OOO      OOO   OO
                       OO     OOO  OOO     OO
                        OOO     OOOO     OOO
      OOOOOO          OO  OOOOOO    OOOOOO  OO          OOOOOO
   OOOO    OOOOO   OOOO                      OOOO   OOOOO    OOOO
               OOOOO     VVVVVV      VVVVVV     OOOOO
                       VVVVVVVVVV  VVVVVVVVVV
                     VVVVVVVVVVVVVVVVVVVVVVVVVV
                     VVVVVVVVVVVVVVVVVVVVVVVVVV
        XXXXXX       VVVVVVVVVVVVVVVVVVVVVVVVVV      XXXXXXX
     XXXXXXXXXXX      VVVVVVVVVVVVVVVVVVVVVVVV      XXXXXXXXXXX
    XXXXXXXXXXXXX      VVVVVVVVVVVVVVVVVVVVVV      XXXXXXXXXXXXX
   XXXXXXXXXXXXXXXX     VVVVVVVVVVVVVVVVVVVV     XXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXX      VVVVVVVVVVVVVVVVVV      XXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXX     XXVVVVVVVVVVVVVVVVXX     XXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXX    XXXVVVVVVVVVVVVVVXXX    XXXXXXXXXXXXXXXX
       XXXXXXXXXXX     XXXX VVVVVVVVVVVV XXXX     XXXXXXXXXXX
           XXXXXXX    XXXX   VVVVVVVVVV   XXXX    XXXXXXX
    XXXXXX  XXXXXXXXXXXXXX    VVVVVVVV    XXXXXXXXXXXXXX  XXXXXX
  XXXXXXXXXXXXXXXXXXXXXX       VVVVVV       XXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXXXX           VVVV           XXXXXXXXXXXXXXXXXXXX
XX XXXXX XXXXXXXXXXXX            VV            XXXXXXXXXXXX XXXXX XX
X  X XX  XXXXXXXXXXXX                          XXXXXXXXXXXX  XX X  X
     X  XXXXXXXXXXXX                            XXXXXXXXXXXX  X
       XXXXXXXXXXXXX                            XXXXXXXXXXXXX
       XXXXXXXXXXXXXX                          XXXXXXXXXXXXXX
       XXXXXXXXXXXXXXX                        XXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXX
       XXXXXXX  XXXXXXXX                    XXXXXXXX  XXXXXXX
      XXXXXXX     XXXXXXX                  XXXXXXX     XXXXXXX
 XXXXXXXXXXX        XXXXXX                XXXXXX        XXXXXXXXXXX
 XXXXXXXXX           XXXXX                XXXXX           XXXXXXXXX
 XXXX                 XXXXX              XXXXX                 XXXX
  XXX                  XXXXX            XXXXX                  XXX
                        XXXX            XXXX
'''

print(logo)

def line():
    print("\n-----------------------------\n")

line()

your_name = input("What is your name?\n  ")

line()

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

line()

if scoreInt < 10 or scoreInt > 90:
    anim()
    print(f"\n\nYour score is {scoreInt}%, you go together like coke and mentos.")
elif scoreInt >= 40 and scoreInt <= 80:
    anim()
    print(f"\n\nYour score is {scoreInt}%, you are born for each other.")
else:
    anim()
    print(f"\n\nYour score is {scoreInt}%.")