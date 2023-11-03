import random


def play_game():
    # read the words
    f = open("words.txt", 'r')
    all_words = f.read()
    word_list = all_words.split()
    chosen_word = random.choice(word_list)
    print(chosen_word)
    print('The mystery word is', len(chosen_word), 'letters long')
    guesses = []
    display = ["_" for character in chosen_word]
    print(display)
    remaining_tries_counter = 8
    # start loop here
    while remaining_tries_counter > 0 and chosen_word != ''.join(display):
        # this is true for when the game is lost
        # game is won when the loop is false
        guess = input("Guess a letter! ").lower()
        # we need to check that our guess is valid(no repeats, no more than 1 letter)
        if len(guess) > 1:
            print('Guess ONE letter at a time!')
        elif not guess.isalpha():
            print('Guess a LETTER!')
        elif guess in guesses:
            print("You already guessed that!")
            print('Guess List/Array', guesses)
        # getting here means the input is valid and now we check the guess for right or wrong
        else:
            # then we append the guess to our array/list and then do the rest
            guesses.append(guess)
            # this is if you guessed right
            if guess in chosen_word:
                print('correct!')
                for index in range(len(chosen_word)):
                    if guess == chosen_word[index]:
                        display[index] = guess
                        print(display)
                        print('chosen_word: ', chosen_word)
                        print(guesses)
                if chosen_word == ''.join(display):
                    # remaining_tries_counter = 0
                    print('You won!')
                    # this is where you win and the game ends
            # this is if you guessed wrong
            else:
                remaining_tries_counter = remaining_tries_counter-1
                print('Nope! You have ', f'{remaining_tries_counter} tries left')
    # print('You finished the game!')
    play_again = input('Want to play again? Y/N ').lower()
    if play_again == 'y':
        play_game()
    else:
        exit()

    # this is where you lose and the game ends
    # letters = [letter for letter in chosen_word]
    # print(letters)
        # blanks = '_' * len(chosen_word)
        # guessed_letters = []
        # guessed = False
        # tries = 8
        # print("Guess a letter!")
        # print("Number of tries: ", f'{tries}')
        # print('\n')


if __name__ == "__main__":
    play_game()
