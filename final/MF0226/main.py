from random import randint

class GetRandomWord:
    def __init__(self):
        self.words = ["pepe", "casa", "padre", "marido", "mujer", "hombre"]

    def get_word(self):
        word = self.words[randint(0,5)]
        return word

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []

    def guess(self, letter):
        if(letter in self.word and letter not in self.guessed):
            print("You guessed the letter!")
        if(letter not in self.word and letter not in self.guessed):
            print("You guessed wrong!")
        if(letter in self.guessed):
            print("You already guessed that letter")

    def get_status(self):
        print("Guess the word:")
        for x in self.word:
            if x in self.guessed:
                print(x, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        j = 0
        for letter in self.word:
            if letter in self.guessed:
                j = j + 1
        if(j == len(self.word)):
            return True
        else:
            return False



class PlayGame:
    def __init__(self):
        self.word = GetRandomWord().get_word()
        self.hanged = Hangman(self.word)

    def play(self):
        while not self.hanged.check_if_player_won():
            self.hanged.get_status()
            letter = input("Give a letter: ")
            self.hanged.guess(letter)
            self.hanged.guessed.append(letter)
            if self.hanged.check_if_player_won():
                print("You won!")



if __name__ == '__main__':
    playgame = PlayGame()
    playgame.play()
