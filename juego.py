from ahorcado import Ahorcado
import re


def comprobationLifes(lifes):
    if int(lifes) > 1:
        return int(lifes)
    else:
        return print('Please add a valid number')


def comprobationLetter(letter):
    if len(letter) == 1:
        if re.search(r'[a-zA-Z]', letter).group() == True: #revisar
            return letter
    else:
        return print('please only one letter is allowed')


def main():
    lifes = input('Ingrese numero de vidas:   ')
    lifes = comprobationLifes(lifes)
    letter = ''
    poop = Ahorcado(lifes)

    while poop.vidas != 0:

        Ahorcado.dibujar(poop)
        letter = input('ingrese una letra: ').upper()
        comprobationLetter(letter)
        Ahorcado.jugar(poop, letter)


main()
