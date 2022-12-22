import datetime
from random_word import RandomWords


class Hangman:

    def __init__(self):
        self.wrong_guesses = []
        self.random_word = self.create_random_word()
        self.correct_letters = []
        self.letters_for_random_word = [letter for letter in self.random_word]
        self.place_holder_for_correct_letters = [
            [] for word in self.random_word]

    # Creates random word
    def create_random_word(self):
        r = RandomWords()
        word = r.get_random_word()
        return word

    def check_player_letter(self, player_guess):
        if player_guess in self.wrong_guesses:
            print("You already choose this letter.")

        elif player_guess not in self.letters_for_random_word:
            self.wrong_guesses.append(player_guess)
        else:

            indices = [i for i, x in enumerate(
                self.letters_for_random_word) if x == player_guess]

            for index in indices:
                if player_guess in self.place_holder_for_correct_letters[index]:
                    print("Letter is already in place.")
                else:
                    self.place_holder_for_correct_letters[index] += player_guess
                    self.correct_letters.append(player_guess)

    def greeting_of_the_day(self, name):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            print("Hello,Good Morning {player_name}!".format(
                player_name=name))
        elif hour >= 12 and hour < 18:
            print("Hello,Good Afternoon {player_name}!".format(
                player_name=name))
        else:
            print("Hello,Good Evening {player_name}!".format(
                player_name=name))
