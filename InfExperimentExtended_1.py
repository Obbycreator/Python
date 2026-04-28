import random
from time import sleep

Streichhölzer = int(input("Wie viele Streichhölzer soll es zu Beginn geben? "))
sleep(.25)
WegznmdHölzer = int(input("Wie viele Streichhlözer darf man auf einmal wegnehmen? "))
sleep(.75)
print("Das Spiel beginnt.")
sleep(.75)

while Streichhölzer > 0:
    inputplr1 = int(input(f"Übrige Streichhölzer: {Streichhölzer}. Spieler 1, gib eine Zahl zwischen 1 und {WegznmdHölzer} ein: "))
    if inputplr1 < 0 or inputplr1 > WegznmdHölzer:
        print("Ungültige Zahleingabe!")
        continue
    else:
        Streichhölzer -= inputplr1
        if Streichhölzer <= 0:
            print("Der Roboter gewinnt! ")
            break
    sleep(.75)

    random_abzug = random.randint(1, WegznmdHölzer)
    Streichhölzer -= random_abzug
    print(f"der Roboter hat {random_abzug} Streichhölzer weggenommen. Es bleiben {(Streichhölzer <= 0 and 0) or Streichhölzer} Streichhölzer übrig.")
    sleep(.75)
    if Streichhölzer <= 0:
        print("Spieler hat gewonnen!")
        break
    sleep(.4)
