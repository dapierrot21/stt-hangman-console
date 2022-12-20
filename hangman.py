import datetime
import speech_recognition as sr  # speech recogniton.
import pyttsx3
import subprocess  # to process various system commands.
from random_word import RandomWords


class Hangman:

    def __init__(self):
        self.wrong_guesses = []
        self.correct_letters = []
        self.random_word = self.create_random_word()
        self.letters_for_random_word = [letter for letter in self.random_word]
        self.place_holder_for_correct_letters = [
            [] for word in self.random_word]

    # Creates random word
    def create_random_word(self):
        r = RandomWords()
        word = r.get_random_word()
        return word

    def check_player_letter(self, player_guess):
        if player_guess not in self.letters_for_random_word:
            self.wrong_guesses.append(player_guess)

        indices = [i for i, x in enumerate(
            self.letters_for_random_word) if x == player_guess]
        for index in indices:
            if player_guess in self.place_holder_for_correct_letters[index]:
                print("You already choose this letter.")
            else:
                self.place_holder_for_correct_letters[index] += player_guess
                self.correct_letters.append(player_guess)

    def greeting_of_the_day(self, name):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            print("Hello,Good Morning {player_name}!".format(
                player_name=self.name))
        elif hour >= 12 and hour < 18:
            print("Hello,Good Afternoon {player_name}!".format(
                player_name=self.name))
        else:
            Player.speak("Hello,Good Evening {player_name}!".format(
                player_name=self.name))
            print("Hello,Good Evening {player_name}!".format(
                player_name=self.name))


class Player:
    engine = pyttsx3.init()
    engine.setProperty('rate', 75)

    def __init__(self, name):
        self.name = name

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("If you can not get your letter recognized then try saying a word with that letter as the first letter in the word. Ex: for the letter \"c\" try saying cat.")
            print("Speak")
            # Recommended for situations where the ambient noise level is unpredictable, which seems to be the majority of use cases. If the ambient noise level is strictly controlled, better results might be achieved by setting this to False to turn it off.
            r.dynamic_energy_threshold = True
            # r.adjust_for_ambient_noise(source, duration=2.5)
            r.pause_threshold = 0.5
            audio = r.listen(source, phrase_time_limit=5)
            statement = ""
            try:
                statement = r.recognize_google(audio, language='en-US').lower()
                print(f"You said: {statement[0]}\n")

            except sr.UnknownValueError:
                print("Sorry I could not hear you.")
            except sr.RequestError as e:
                print("Request Failed; {0}".format(e))
            return statement[0]


if __name__ == "__main__":
    player = Player('Dean')
    hangman = Hangman()

    number_of_guesses = len(hangman.random_word)
    count = 0  # is going to be the sum of the len(wrong_guess).

    while count < number_of_guesses:

        print(hangman.greeting_of_the_day)
        print("Welcome to Speech-to-Text Hangman Console Game.")
        print("\n")

        print("The number of guesses you have is based on the length of the word.")
        print("The word contains {space} spaces.".format(
            space=len(hangman.place_holder_for_correct_letters)))
        print(hangman.place_holder_for_correct_letters)
        print("\n")

        print("Now let\'s guess a letter.")
        print(hangman.random_word)

        while count != number_of_guesses:
            letter = player.takeCommand()
            results = hangman.check_player_letter(letter)
            if letter in hangman.correct_letters:
                print(hangman.place_holder_for_correct_letters)
                print("Correct letter: {correct_letters}".format(
                    correct_letters=hangman.place_holder_for_correct_letters))
                count += 1
            if letter in hangman.wrong_guesses:
                print(hangman.place_holder_for_correct_letters)
                print("Wrong letters: {wrong_letters}".format(
                    wrong_letters=hangman.wrong_guesses))
                count += 1
        print(hangman.random_word)
