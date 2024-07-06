'''
Hangman: Implement the wordguessing game with visual progress and hints.
'''


class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guesses = set()
        self.max_attempts = 6

    def display_word(self):
        display = ""
        for char in self.word:
            if char in self.guesses:
                display += char
            else:
                display += "_"
        return display

    def make_guess(self, letter):
        letter = letter.lower()
        self.guesses.add(letter)
        if letter not in self.word:
            self.max_attempts -= 1

    def is_game_over(self):
        return self.max_attempts == 0 or "_" not in self.display_word()

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            print(f"Word: {self.display_word()}  (Attempts left: {self.max_attempts})")
            guess = input("Guess a letter: ")
            self.make_guess(guess)
        if "_" not in self.display_word():
            print(f"Congratulations! You guessed the word: {self.word}")
        else:
            print(f"Game over! The word was: {self.word}")

# Example usage
if __name__ == "__main__":
    secret_word = "python"  # Replace with any word you like
    game = Hangman(secret_word)
    game.play()
