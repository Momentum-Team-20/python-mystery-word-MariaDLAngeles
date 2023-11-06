import random


def validation(guess, guesses):
    if len(guess) > 1:
        print('Invalid entry: Only 1 letter at a time.')
        return False
    elif not guess.isalpha():
        print('Invalid entry: Letters only.')
        return False
    elif guess in guesses:
        print("You already guessed that!")
        return False
    else:
        return True


# let's put this whole function in a while loop so the game is only running while the user is playing
def play_game():
    f = open("words.txt", 'r')
    all_words = f.read()
    # read the words - OPENING AND READING CAN BE A FUNCTION -- SHOULD OPENING, READING, AND CHOOSING A WORD BEA FUNCTION OR 2/3 SEPARATE FUNCTIONS
    word_list = all_words.split()
    chosen_word = random.choice(word_list)
    print(chosen_word)
    print('The mystery word is', len(chosen_word), 'letters long')
    guesses = []
    display = ["_" for character in chosen_word]
    print(display)
    remaining_tries_counter = 8
    # Loop starts here
    while remaining_tries_counter > 0 and chosen_word != ''.join(display):
        guess = input("Guess a letter: ").lower()
        if validation(guess, guesses) is True:
            guesses.append(guess)
            # if you guessed RIGHT
            if guess in chosen_word:
                print('Correct!')
                for index in range(len(chosen_word)):
                    if guess == chosen_word[index]:
                        display[index] = guess
                if chosen_word == ''.join(display):
                    print('You won!')
            # if you guessed WRONG
            else:
                remaining_tries_counter = remaining_tries_counter-1
                print('Nope! You have ', remaining_tries_counter, 'tries left')
        # right or wrong, we print display
            print(display)
        # if tries run out, we reveal the chosen word
            if remaining_tries_counter == 0:
                print("Oh no! Your mystery word was:", chosen_word)


if __name__ == "__main__":
    while True:
        play_game()
    # win or lose, we need to know if the player wants to play again
    # PLAY AGAIN CAN BE A FUNCTION
        play_again = input('Want to play again? Y/N ').lower()
        if play_again == 'y':
            continue
        else:
            exit()
