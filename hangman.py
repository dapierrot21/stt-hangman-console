import datetime
import speech_recognition as sr  # speech recogniton.
import pyttsx3
import subprocess  # to process various system commands.
from random_word import RandomWords
from PyDictionary import PyDictionary


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
            print("\n")
            print("Remember to use a word instead of a letter.")
            print("Ex: For letter \"c\" -> try saying \"cat\"")
            print("Speak your word now.")
            # Recommended for situations where the ambient noise level is unpredictable, which seems to be the majority of use cases. If the ambient noise level is strictly controlled, better results might be achieved by setting this to False to turn it off.
            r.dynamic_energy_threshold = True
            r.energy_threshold = 4
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 4
            audio = r.listen(source, phrase_time_limit=9, timeout=10)
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

    def meaning_of_word(word):
        try:
            py = PyDictionary()
            meaning_of_word = py.meaning(
                hangman.random_word, disable_errors=True)
        except None:
            print("Sorry having trouble finding the meaning of this word. Good luck.")
        return meaning_of_word

    while count < number_of_guesses:

        hangman.greeting_of_the_day(player.name)
        print("Welcome to Speech-to-Text Hangman Console Game.")
        print("Letters like \"c\", \"u\", \"a\", \"h\" can sound like a word and not the letter your trying.")
        print("So tackle this problem I suggest that you use word instead of letter.")
        print("Ex: letter \"c\" is best heard when \"cat\" is said.")
        print("\n")

        print("The number of guesses you have is based on the length of the word.")
        print("The word contains {space} letters. So you have {space} chances of getting the word correct".format(
            space=len(hangman.place_holder_for_correct_letters)))
        print(hangman.place_holder_for_correct_letters)
        print("\n")

        print("Now let\'s guess a letter. I suggest using a word that has the target letter as the first letter in that word.")
        print(hangman.random_word)

        while count != number_of_guesses:
            print("Meaning of the word: {meaning}".format(
                meaning=meaning_of_word(hangman.random_word)))
            letter = player.takeCommand()
            results = hangman.check_player_letter(letter)
            if len(hangman.correct_letters) == len(hangman.letters_for_random_word):
                print("Congrats! you have won. The word is {word}.".format(
                    word=hangman.random_word))
                break
            else:
                if letter in hangman.letters_for_random_word:
                    print(hangman.place_holder_for_correct_letters)
                    print("Correct! {letter} is within the random word.".format(
                        letter=letter))
                    print("You have {guesses} guesses left.".format(
                        guesses=number_of_guesses - count))

                if letter in hangman.wrong_guesses:
                    print(hangman.place_holder_for_correct_letters)
                    print("Wrong letters: {wrong_letters}".format(
                        wrong_letters=hangman.wrong_guesses))
                    count += 1
                    print("You have {guesses} guesses left.".format(
                        guesses=number_of_guesses - count))
