import random

def main():
    display_banner()
    play_game()


def play_game():
    game_finished = False
    words_list = get_words_from_file('words1.txt')
    words_dictionary = build_dictionary(words_list)
    level = int(input('Enter the number of letters in the guessing word: '))
    generated_word = get_word(words_dictionary[level])
    encrypted_list = get_encrypted_list(generated_word)
    while game_finished == False:
        display_word(encrypted_list)
        letter = input('Enter a letter: ')
        check_guess(generated_word, encrypted_list, letter)
        game_finished = check_game_finished(encrypted_list)
        if game_finished:
            congratulate(generated_word)


def display_banner():
    print("*" * 18 + "\nWORD GUESSING GAME\n" + "*" * 18)


def congratulate(word):
    print("GUESS THE WORD: " + word)

    print("=" * 23 + "\n** W E L L   D O N E **\n" + "=" * 23)

def get_words_from_file(filename):
    input_file = open(filename, 'r')
    words = input_file.read().split()
    input_file.close()
    return words

def build_dictionary(words_list):
    new_dict = {}
    for i in range(len(words_list)):
        words_list[i] = words_list[i].lower()

    words_list = sorted(words_list)

    for i in range(len(words_list)):
        if len(words_list[i]) not in new_dict:
            new_dict[len(words_list[i])] = [words_list[i]]
        else:
            new_dict[len(words_list[i])].append(words_list[i])
    return new_dict

def get_word(words_list):
    rand_num = random.randrange(0,len(words_list))
    return words_list[rand_num]

def get_encrypted_list(word):
    new_list = [word[0]]
    for i in range(len(word) - 1):
        new_list.append("*")
    return new_list

def display_word(encrypted_list):
    word = "".join(encrypted_list)
    print("GUESS THE WORD: " + word)

def check_guess(generated_word, encrypted_list, letter):
    for i in range(len(generated_word)):
        if letter == generated_word[i]:
            encrypted_list[i] = letter

def check_game_finished(encrypted_list):
    if "*" not in encrypted_list:
        return True
    else:
        return False
