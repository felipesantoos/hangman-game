import shutil

START_BOLD = "\033[1m"
END_BOLD = "\033[0m"
TERMINAL_LENGTH = shutil.get_terminal_size().columns

def header(tip, used_letters):
    print((START_BOLD + "THE HANGMAN GAME" + END_BOLD).center(shutil.get_terminal_size().columns))
    print(f"{START_BOLD}Dica:{END_BOLD} {tip}.")
    print(f"{START_BOLD}Letras já utilizadas:{END_BOLD}", end=" ")
    if len(used_letters) == 0:
        print("nenhuma.")
    else:
        for index in range(len(used_letters)):
            print(used_letters[index], end="")
            if index != len(used_letters) - 1:
                print(", ", end="")
        print("")

def strength(lifes):
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

def win():
    print("\n\n+" + "-" * (TERMINAL_LENGTH - 2) + "+")
    print("|", end="")
    print(f"{START_BOLD}Você venceu!{END_BOLD}".center(TERMINAL_LENGTH + 6), end="")
    print("|")
    print("+" + "-" * (TERMINAL_LENGTH - 2) + "+")

def lost():
    print("\n\n+" + "-" * (TERMINAL_LENGTH - 2) + "+")
    print("|", end="")
    print(f"{START_BOLD}Você perdeu!{END_BOLD}".center(TERMINAL_LENGTH + 6), end="")
    print("|")
    print("+" + "-" * (TERMINAL_LENGTH - 2) + "+")
