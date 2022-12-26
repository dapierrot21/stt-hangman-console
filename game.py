from player import Player
from hangman import Hangman


if __name__ == "__main__":
    player = Player('Dean')
    hangman = Hangman()

    number_of_guesses = len(hangman.random_word)
    count = 0  # is going to be the sum of the len(wrong_guess).

    while count < number_of_guesses:

        hangman.greeting_of_the_day(player.name)
        print("Welcome to Speech-to-Text Hangman Console Game.")
        print("Letters like \"c\", \"u\", \"a\", \"h\" can sound like a word and not the letter your trying.")
        print("So tackle this problem I suggest that you use word instead of letter.")
        print("Ex: Letter \"c\" is best heard when \"cat\" is said.")
        print("\n")

        print("The number of guesses you have is based on the length of the word.")
        print("The word contains {space} letters. So you have {space} chances of getting the word correct".format(
            space=len(hangman.place_holder_for_correct_letters)))
        print(hangman.place_holder_for_correct_letters)
        print("\n")

        print("Now let\'s guess a letter. I suggest using a word that has the target letter as the first letter in that word.")

        while count != number_of_guesses:
            print("Meaning of the word: {meaning}".format(
                meaning=hangman.meaning_of_word(hangman.random_word)))
            letter = player.take_command()
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
