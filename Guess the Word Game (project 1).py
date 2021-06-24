import random

def GuessingWords(wordList):
    word = random.choice(wordList)
    playerName = input('What is your name?')
    print(f'Good Luck! {playerName}')
    guessingList = ['_' for x in range(len(word))]
    charList = list(word)
    print('Guess the characters')
    for line in guessingList:
        print(line)
    chance = 3
    while True:
        guess = input('guess a character:')
        if (guess.upper() in charList) or (guess.lower() in charList):
            try:
                place = charList.index(guess.lower())
            except ValueError:
                place = charList.index(guess.upper())
            guessingList[place] = charList[place]
            charList[place] = ''
            for char in guessingList:
                print(char)
        elif guess not in charList:
            chance -= 1
            print(f'Wrong\n'
                  f'You have {chance} more guesses')
            for char in guessingList:
                print(char)
            if (chance == 0) and ('_' in guessingList):
                return f'Game Over\nThe answer is {word}'
        if '_' not in guessingList:
            return f'You win!!\nThe answer is exactly {word}!!'

if __name__ == '__main__':
    guessingWordList = ['Jennie', 'Gaming', 'Friendship', 'Computer', 'Python', 'Eunice']
    print(GuessingWords(guessingWordList))
