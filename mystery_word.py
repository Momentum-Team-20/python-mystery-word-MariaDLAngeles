import random


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
    tries = 8
    guess = input("Guess a letter!")
    print(guess)
    guesses.append(guess)
    if guess in chosen_word:
        print('correct!')
        for index in range(len(chosen_word)):
            if guess == chosen_word[index]:
                display[index] = guess
                print(display)
    else:
        print('incorrect!')
        
    
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
