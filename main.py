import os
import random
import unidecode

os.system("cls" if os.name == "nt" else "clear")

file = open("words.txt")
word_and_tip_list = file.read().split("\n")
word_and_tip = random.choice(word_and_tip_list).lower()
word, tip = word_and_tip.split(",")
word_unidecode = unidecode.unidecode(word)

used_letters = []
lifes = 6

while True:
    print(f"Dica: {tip}.")
    print("Letras já utilizadas:", end=" ")
    for index in range(len(used_letters)):
        print(used_letters[index], end="")
        if index != len(used_letters) - 1:
            print(", ", end="")
    print("")

    head = "o" if lifes <= 5  else " "
    body = "|" if lifes <= 4 else " "
    left_arm = "/" if lifes <= 3 else " "
    right_arm = "\\" if lifes <= 2 else " "
    left_leg = "/" if lifes <= 1 else " "
    right_leg = "\\" if lifes == 0 else " "

    print(" _______")
    print("|       |")
    print("|       {}".format(head))
    print("|      {0}{1}{2}".format(left_arm, body, right_arm))
    print("|      {0} {1}\n".format(left_leg, right_leg))

    letters_showed = 0
    for index in range(len(word_unidecode)):
        if word_unidecode[index] in used_letters:
            print(word[index] + " ", end="")
            letters_showed = letters_showed + 1
        else:
            print("_ ", end="")

    if letters_showed == len(word):
        print("\n\nVocê venceu!")
        break
    else:
        if lifes == 0:
            print("\n\nVocê perdeu!")
            break
        else:
            letter = input("\n\nDigite um letra: ")
            letter = letter.lower()

            os.system("cls" if os.name == "nt" else "clear")

            if letter in used_letters:
                print("Essa letra já foi utilizada!")
            else:
                used_letters.append(letter)
                if letter in word_unidecode:
                    print("Acertou!")
                else:
                    print("Errou!")
                    lifes = lifes - 1
                    