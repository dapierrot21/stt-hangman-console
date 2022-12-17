import pyttsx3


class Hangman:

    # List of a stick figure to use as a way to show the player how many tries the player has left yo guess the word correctly.
    def __init__(self):
        # This is where the stick figure will be added too.
        self.wrong_guesses = []

    # Creates random word
    def create_random_word():
        pass

    # Checks the string from the player and see if it's part of the random word
    def check_player_letter(self, letter):
        pass


class Player:

    engine = pyttsx3.init()
    engine.setProperty('rate', 65)

    # Obtains audio from user microphone
    # Use google speech recognition on the audio file and convert to text
    def __init__(self, name):
        self.name = name

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


test = Player('Dean')

test.speak("Hi {player}! welcome to speech to text hangman console game. To play this game you will need to make sure your microphone is on. Using the microphone you will speak your letter to guess the word. Good luck!".format(player=test.name))
