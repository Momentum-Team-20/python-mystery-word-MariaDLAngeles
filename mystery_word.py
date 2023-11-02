import random


def play_game():
    # read the words
    f = open("words.txt", 'r')
    # print(f.read())
    # randomly pick one word
    all_words = f.read()
    word_list = all_words.split()
    chosen_word = random.choice(word_list)
    print(chosen_word)
    # displaying chosen word as blanks by taking the length of the word and * it by _'s
    blanks = '_' * len(chosen_word)
    print(blanks) 


if __name__ == "__main__":
    play_game()
