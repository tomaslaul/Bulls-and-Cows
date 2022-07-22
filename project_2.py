"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Laul
email: tomas.laul@me.com
discord: Tomáš#1025
"""

import random
from re import A

#pomocne promenne
oddelovac = "-" * 48

#nahodne cislo
nahodne_cislo = random.sample(range(0, 9), 4)
if nahodne_cislo[0] == 0:
    nahodne_cislo[0] = 1
nahodne_cislo[0] = str(nahodne_cislo[0])
nahodne_cislo[1] = str(nahodne_cislo[1])
nahodne_cislo[2] = str(nahodne_cislo[2])
nahodne_cislo[3] = str(nahodne_cislo[3])

#uvod
def uvod() -> None:
    print("Hi there!")
    print(oddelovac)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(oddelovac)
    print("Enter a number:")
    print(oddelovac)

#kontrola zadani
def vstup(tip: str):
    result = False
    if not tip.isdecimal():
        print(f"Please input numbers only! \n{oddelovac}")
    elif len(tip) != 4:
        print(f"Please input 4 numbers! \n{oddelovac}")
    elif tip[0] == "0":
        print(f"Number cannot begin with 0! \n{oddelovac}")
    elif len(set(tip)) != 4:
        print(f"All digits must be unique! \n{oddelovac}")
    else:
        result = True
    return result

#vyhodnocení shody
def vyhodnoceni(tip: str, nahodne_cislo: list):
    bulls, cows = 0, 0

    for i, number in enumerate(tip):
        if number == nahodne_cislo[i]:
            bulls += 1
        elif number in nahodne_cislo:
            cows += 1
    #stav, plural
    if bulls != 4:
        stav = f"{bulls} bull"
        if bulls > 1:
            stav = f"{bulls} bulls"
        stav += f", {cows} cow"
        if cows > 1:
            stav += "s"
        return stav

#vysledek
def vysledek(pokusy: int):
    print("Correct, you've guessed the right number")
    print("in", pokusy, "guesses")

def main():
    pokusy = 0
    uvod()

    while True:
        tip = input(">>> ")
        if vstup(tip):
            pokusy += 1
            message = vyhodnoceni(tip, nahodne_cislo)
            if not message:
                vysledek(pokusy)
                print(oddelovac)
                break
            else:
                print(message)
                print(oddelovac)

    if pokusy <= 10:
        print("That's amazing")
    elif pokusy < 25:
        print("That's average")
    else:
        print("That's not so good")
main()