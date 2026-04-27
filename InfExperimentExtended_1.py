Streichhölzer = int(input("Wie viele Streichhölzer es zu Beginn geben? "))
WegznmdHölzer = int(input("Wie viele Streichhlözer darf man auf einmal wegnehmen?"))

_skipPlr1 = False

while Streichhölzer > 0:
    if _skipPlr1 == False:
        inputplr1 = int(input(f"Übrige Streichhölzer: {Streichhölzer}. Spieler 1, gib eine Zahl zwischen 1 und {WegznmdHölzer} ein:"))
        if inputplr1 < 0 or inputplr1 > WegznmdHölzer:
            print("Ungültige Zahleingabe!")
            continue
        else:
            Streichhölzer -= inputplr1
            if Streichhölzer <= 0:
                print("Spieler 2 hat gewonnen!")
                break


    if _skipPlr1 == True:
        _skipPlr1 == False
    inputplr2 = int(input(f"Übrige Streichhölzer: {Streichhölzer}. Spieler 2, gib eine Zahl zwischen 1 und {WegznmdHölzer} ein:"))
    if inputplr2 < 0 or inputplr2 > WegznmdHölzer:
        print("Ungültige Zahleingabe!")
        _skipPlr1 = True
        continue
    else:
        Streichhölzer -= inputplr2
        if Streichhölzer <= 0:
            print("Spieler 2 hat gewonnen!")
            break