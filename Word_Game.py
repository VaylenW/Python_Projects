import random
import json

word_pool = list(json.load(open('word_list.json')))

print("You will guess a four letter word.")

def word_choice():
    global user_guess
    global guess_number
    global correct_word
    global comparison_list_green
    user_guess = ""
    word_pool_2 = {item["number"]: item["word"] for item in word_pool}
    correct_word = random.choice(word_pool_2)
    guess_number = 1
    comparison_list_green = []

def comparison():
    for i in range(len(user_guess)):
        if user_guess[i] == correct_word[i]:
            comparison_list_green.append(user_guess[i])
            comparison_list_green_count = len(comparison_list_green)
            for i in range(comparison_list_green_count):
                print(f"The letter '{comparison_list_green[i]}' is in the correct word and in the right place.")
    user_guess_set = set(user_guess.upper())
    correct_word_set = set(correct_word.upper())
    if user_guess_set.intersection(correct_word_set):
        #fix this formatting and false negatives later
        print(f"The letter(s) {user_guess_set & correct_word_set} are in the word but not in the right place.")
    comparison_list_green.clear()


word_choice()
#testing
print(correct_word)
while user_guess != correct_word:
    print(f"Please input guess number {guess_number}.")
    user_guess = input(": ").capitalize()
    if user_guess == correct_word:
        print(f"Correct! The word was '{correct_word}' and it took you {guess_number} guesses!")
        replay = input("Play again? Y/N: ").capitalize()
        if replay == "Y":
            word_choice()
        else:
            break
    elif len(user_guess) != 4:
        print("Incorrect guess length!")
        pass
    else:
        guess_number += 1
        comparison()
