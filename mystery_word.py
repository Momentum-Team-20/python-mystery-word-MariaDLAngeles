import random
MAX_INCORRECT_TRIES = 8


def play_game():
    # read the words
    f = open("words.txt", 'r')
    all_words = f.read()
    word_list = all_words.split()
    chosen_word = random.choice(word_list)
    print(chosen_word)
    guesses = []
    display = ["_" for character in chosen_word]
    print(display)
    remaining_tries_counter = 8
    # start loop here
    while remaining_tries_counter > 0:
        guess = input("Guess a letter!")
        print(guess)
        guesses.append(guess)
        if guess in chosen_word:
            print('correct!')
            for index in range(len(chosen_word)):
                if guess == chosen_word[index]:
                    display[index] = guess
                    print(display)
                    print('chosen_word: ',chosen_word)
                    print(guesses)
            if chosen_word == ''.join(display):
                print('you won!')
        else:
            remaining_tries_counter = remaining_tries_counter-1
            print('incorrect!')
        print('You have ', f'{remaining_tries_counter}', ' tries remaining')
    print('Game Over!')
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
