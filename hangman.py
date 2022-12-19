import datetime
import speech_recognition as sr  # speech recogniton.
import os
import pyttsx3
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

        indices = [i for i, x in enumerate(
            self.letters_for_random_word) if x == player_guess]

        for index in indices:
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
            Player.speak("Hello,Good Evening {player_name}!".format(
                player_name=name))
            print("Hello,Good Evening {player_name}!".format(
                player_name=name))


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
            self.speak("I am now able to take your letter you want to try.")
            print("I am now able to take your letter you want to try.")
            # Recommended for situations where the ambient noise level is unpredictable, which seems to be the majority of use cases. If the ambient noise level is strictly controlled, better results might be achieved by setting this to False to turn it off.
            r.dynamic_energy_threshold = True
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            audio = r.listen(source)
            statement = ""
            try:
                statement = r.recognize_google(audio, language='en-US').lower()
                print(f"You said: {statement[0]}\n")

            except sr.UnknownValueError:
                print("Sorry I could not hear you.")
            except sr.RequestError as e:
                print("Request Failed; {0}".format(e))
            return statement[0]


test_speak = Player('Dean')
test_random_word = Hangman()

# test_speak.speak("Hi {player}! welcome to speech to text hangman console game. To play this game you will need to make sure your microphone is on. Using the microphone you will speak your letter to guess the word. Good luck!".format(player=test_speak.name))

# print(test_random_word.create_random_word())


test_random_word.greeting_of_the_day(test_speak.name)
letter_to_try = test_speak.takeCommand()
test_random_word.check_player_letter(letter_to_try)

print(test_random_word.place_holder_for_correct_letters)
