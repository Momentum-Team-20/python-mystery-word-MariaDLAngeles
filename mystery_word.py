import random


def play_game():
    # read the words
    f = open("words.txt", 'r')
    all_words = f.read()
    word_list = all_words.split()
    chosen_word = random.choice(word_list)
    # print(chosen_word)
    print('The mystery word is', len(chosen_word), 'letters long')
    guesses = []
    display = ["_" for character in chosen_word]
    print(display)
    remaining_tries_counter = 8
    # start loop here
    while remaining_tries_counter > 0 and chosen_word != ''.join(display):
        guess = input("Guess a letter: ").lower()
        # first we check for valid user inputs (no numbers, no #$@*!)
        if len(guess) > 1:
            print('Invalid entry: Only 1 letter at a time.')
        elif not guess.isalpha():
            print('Invalid entry: Letters only.')
        elif guess in guesses:
            print("You already guessed that!")
            # print('Guess List/Array', guesses)
        # next we check if the user guess is right or wrong
        else:
            # right or wrong, the user guess need to be stored in guesses
            guesses.append(guess)
            # if you guessed RIGHT
            if guess in chosen_word:
                print('Correct!')
                for index in range(len(chosen_word)):
                    if guess == chosen_word[index]:
                        display[index] = guess
                        # print('chosen_word: ', chosen_word)
                        # print(guesses)
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
    # win or lose, we need to know if the player wants to play again
    play_again = input('Want to play again? Y/N ').lower()
    if play_again == 'y':
        play_game()
    else:
        exit()


if __name__ == "__main__":
    play_game()
