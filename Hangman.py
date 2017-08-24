import random


class Hangman(object):
    def __init__(self):
        self.data = []
        self.data_shown = []
        self.letters_guessed = []
        self.guesses_count = 0
        self.boolean = False
        self.winning_message = True

    def pick_word(self):
        words = ("HAPPY", "AMERICA", "EASY", "DIFFICULT", "ANSWER", "SCHOOL", "HOMEWORK", "MONKEY", "GIRAFFE", "TWENTY")
        #words = "".join(map(str, open('wordlist.txt', 'r').readlines())).strip('/n').split()
        self.data = list(random.choice(words).upper())
        #print(words)
        #print(self.data)

    def fill_fields(self):
        for i in range(len(self.data)):
            self.data_shown.append("_")
        print("The word is " + ''.join(map(str, self.data_shown)))

    def draw_hangman(self):
        if self.guesses_count == 0:
            print("******************************************")
            print("         ")
            print("         ")
            print("#        ")
            print("#        ")
            print("###      ")
            print("# #      ")
        elif self.guesses_count == 1:
            print("******************************************")
            print("    ()   ")
            print("   _/|\  ")
            print("#    |/  ")
            print("#    |   ")
            print("### / \  ")
            print("# #_| _\ ")
        elif self.guesses_count == 2:
            print("******************************************")
            print("    ()   ")
            print("    /|   ")
            print("#  / |   ")
            print("#    |   ")
            print("###  |   ")
            print("# # _|   ")
        elif self.guesses_count == 3:
            print("******************************************")
            print("    ()   ")
            print("   /|\   ")
            print("#  || \  ")
            print("#   |\   ")
            print("### | |  ")
            print("# #/_ |_ ")
        elif self.guesses_count == 4:
            print("******************************************")
            print("    ()   ")
            print("    |\_  ")
            print("#   |    ")
            print("#   |    ")
            print("### |    ")
            print("# # |_   ")
        elif self.guesses_count == 5:
            print("******************************************")
            print("      () ")
            print("     /|  ")
            print("#   /  \ ")
            print("#   \    ")
            print("###  |   ")
            print("# # /_   ")
        elif self.guesses_count == 6:
            print("******************************************")
            print("         ")
            print("     ()  ")
            print("#   /|   ")
            print("#  /_\   ")
            print("###  \   ")
            print("# #  /_  ")
        elif self.guesses_count == 7:
            print("******************************************")
            print("         ")
            print("   ()    ")
            print("# /\     ")
            print("# \_\    ")
            print("###  \   ")
            print("# #  /_  ")
        elif self.guesses_count == 8:
            print("******************************************")
            print("         ")
            print(" ()      ")
            print("#|\      ")
            print("#\_\     ")
            print("### \    ")
            print("# #  \_  ")


    def run_game(self):
        while self.data_shown != self.data:
            guess = input("Guess a letter: ").upper()
            # If letter corresponds to the actual letter at that index, then replace shown letter
            for i in range(len(self.data)):
                if guess == self.data[i]:
                    self.data_shown[i] = guess
                    self.boolean = True
            if guess in self.letters_guessed:
                print("Already guessed that letter!")
            if guess.isalpha() is False or len(guess) > 1:
                print("That is not a valid entry!")
            elif self.boolean is True:
                self.letters_guessed.append(guess)
            else:
                self.letters_guessed.append(guess)
                self.guesses_count += 1
            self.boolean = False
            self.draw_hangman()
            print("The word is " + ''.join(map(str, self.data_shown)))
            print("Letters guessed: " + ' '.join(map(str, self.letters_guessed)))
            if self.guesses_count == 8:
                print("The word was " + "".join(map(str, self.data)))
                print("He sat down and is warming your chair... :( Better luck next time!")
                self.data_shown = self.data
                self.winning_message = False
                if input("Play again? (Y/N)").upper() == "Y":
                    play()
        if self.winning_message is True:
            print(r"*************************************************************************************** ")
            print(r"  ___    ___ ________  ___  ___          ___       __   ________  ________   ___        ")
            print(r" |\  \  /  /|\   __  \|\  \|\  \        |\  \     |\  \|\   __  \|\   ___  \|\  \       ")
            print(r" \ \  \/  / \ \  \|\  \ \  \\\  \       \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \  \      ")
            print(r"  \ \    / / \ \  \\\  \ \  \\\  \       \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \     ")
            print(r"   \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \__\    ")
            print(r" __/  / /      \ \_______\ \_______\       \ \____________\ \_______\ \__\\ \__\|__|    ")
            print(r"|\___/ /        \|_______|\|_______|        \|____________|\|_______|\|__| \|__|   ___  ")
            print(r"\|___|/                                                                           |\__\ ")
            print(r"                                                                                  \|__| ")
            print(r"*************************************************************************************** ")
            if input("Play again? (Y/N)").upper() == "Y":
                play()


def play():
    print("Welcome to Sit-Man! Don't let the man sit on your chair!")
    player = Hangman()
    player.pick_word()
    player.fill_fields()
    player.draw_hangman()
    player.run_game()


play()



