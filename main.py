import os
import random
import unidecode
import messages as msg

os.system("cls" if os.name == "nt" else "clear")

file = open("words.txt")
word_and_tip_list = file.read().split("\n")
word_and_tip = random.choice(word_and_tip_list).lower()
word, tip = word_and_tip.split(",")
word_unidecode = unidecode.unidecode(word)

used_letters = []
lifes = 6

while True:
    msg.header(tip, used_letters)
    msg.strength(lifes)

    letters_showed = 0
    for index in range(len(word_unidecode)):
        if word_unidecode[index] in used_letters:
            print(word[index] + " ", end="")
            letters_showed = letters_showed + 1
        else:
            print("_ ", end="")

    if letters_showed == len(word):
        msg.win()
        break
    else:
        if lifes == 0:
            msg.lost()
            break
        else:
            letter = input("\n\nDigite um letra: ")
            letter = letter.lower()

            os.system("cls" if os.name == "nt" else "clear")

            if letter in used_letters:
                print("Essa letra já foi utilizada!")
            else:
                used_letters.append(letter)
                if letter not in word_unidecode:
                    lifes = lifes - 1
                    