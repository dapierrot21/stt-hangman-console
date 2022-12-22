import pyttsx3
import speech_recognition as sr  # speech recogniton.


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
