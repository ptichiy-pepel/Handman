import random


def hangman():
    word = input('Загадай слово или фразу\n')
    wrong_guesses = 0
    stages = ["", 
                "________      ", 
                "|      |      ", 
                "|      0      ", 
                "|     /|\     ", 
                "|     / \     ", 
                "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    
    print('Добро пожаловать на казнь')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Введите букву: ")
        if guess not in remaining_letters:
            wrong_guesses += 1
        for i in remaining_letters:
            if guess in remaining_letters:
                character_index = remaining_letters.index(guess)
                letter_board[character_index] = guess
                remaining_letters[character_index] = '$'
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('Вы выиграли! Было загадано слово:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print(f'Вы проиграли! Было загадано слово: {word}')

hangman()
