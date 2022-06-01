from words import guess_word_list, valid_word_list
import random

print("=== W O R D L E ===")
print(f"Cached {len(guess_word_list)} guess words.")


def debug_mode():
    '''
    This function will be executed when gamers enter 1 for select_mode.
    This mode will give you the word which chosen by you by entering an index (integer) in between 0 - 548.
    The selected word will be shown to you.
    '''
    rand_num = int(input("Enter an index in between 0 - 548: "))
    selected_word = guess_word_list[rand_num]
    print("The selected word is:", selected_word)
    return selected_word


def test_mode():
    '''
    This function will be executed when gamers enter 2 for select_mode.
    This mode will give you the word which chosen by python randomly from list guess_word_list.
    The selected word will be shown to you.
    '''
    rand_num = random.randint(1, 549)
    selected_word = guess_word_list[rand_num]
    print("The selected word is:", selected_word)
    return selected_word


def is_valid(guess):
    '''
    This function will check the selected word is valid or not.
    '''
    if len(guess) != 5:
        print("Word length should be 5.")
        return False
    else:
        for k in range(len(valid_word_list)):
            if valid_word_list[k] == guess:
                return True
        else:
            print("Word", guess, "is not found in the list.")
            return False


# ''' This part is decision part. You will decide to play at debug mode or test mode.'''
select_mode = int(input("Select a mode, Enter (1) for Debug Mode, (2) for Test Mode: "))
if select_mode == 1:
    selected_word = [debug_mode()]
else:
    selected_word = [test_mode()]


# ''' This part will call the is_valid function to check the validity of the selected word.'''
guessed_word = input("Enter a word: ")
while is_valid(guessed_word) == False:
    guessed_word = input("Enter a word: ")
else:
    check_word = [guessed_word]
    # print("Word", guessed_word, "is valid.")

# ''' This part will take the selected and guessed words into a list by separating them into letters.
# In this way, we will be able to check with index whether the letters are correct.'''
for i in range(5):
    selected_word.append(selected_word[0][i])
for i in range(5):
    check_word.append(check_word[0][i])
# print(selected_word)
# print(check_word)

num_attempt = 0
rem_attempt = 5
base = "- - - - -"
while rem_attempt > 0:
    for char in range(5):
        if check_word == selected_word:
            true = (check_word[char + 1])
            print(true.upper(), "", end='')
            rem_attempt = 1
        elif check_word[char + 1] == selected_word[char + 1]:
            letter = check_word[char + 1]
            green = f"\033[92m{letter}\033[0m"  #green
            print(green, "", end='')
        elif check_word[char + 1] in selected_word:
            letter = check_word[char + 1]
            yellow = f"\033[33m{letter}\033[0m"  #yellow
            print(yellow, "", end='')
        else:
            letter = check_word[char + 1]
            print(letter, "", end='')
    num_attempt += 1
    rem_attempt -= 1
    print(("\n" + base)*(5-num_attempt))
    if check_word != selected_word:
        check_word.clear()
        guessed_word = input("\n" + "Enter a word: ")
        while is_valid(guessed_word) == False:
            guessed_word = input("Enter a word: ")
        else:
            check_word = [guessed_word]
        for i in range(5):
            check_word.append(check_word[0][i])
