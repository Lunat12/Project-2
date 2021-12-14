import random

print('Welcome to the Guess My Word App')
game_dict = {'colors': ['red', 'blue', 'yellow', 'green', 'purple', 'orange'], 'sports':["basketball", "baseball", "tennis", 'football', 'golf', 'bowling'], 'fruits':['pinneapple','apple','bannana','strawberries','orange','kiwi'], 'animals':['rabbit', 'fox', 'dog', 'cat', 'bird', 'fish']}

game_keys = []

for k in game_dict.keys():
    game_keys.append(k)

isActive = True


while isActive:
    game_category = game_keys[random.randint(0,3)]
    game_word = game_dict[game_category][random.randint(0,5)]

    blank_word = []
    for l in game_word:
        blank_word.append('-')
    
    print(f'\nGuess a {len(game_word)} letter word from the following category: {game_category}')
    guess = ''
    guess_count = 0
    while guess != game_word:
        print(''.join(blank_word))
        user_guess = str(input('\nEnter your guess: ')).lower()
        guess_count += 1

        if user_guess == game_word:
            print(f'\nCorrect! You guessed the word in {guess_count} guesses.')
            break
            
        else:
            isShown = True
            while isShown:
                letter_index = random.randint(0, len(blank_word)-1)
                if blank_word[letter_index] == '-':
                    blank_word[letter_index] = game_word[letter_index]
                    isShown = False
    try:
        f = open('pf_sfii_data.txt', 'a')
        print('bbbbbbbbbb')
        f.write(f'{guess_count}\n')
        f.close()
    except:
        f = open('pf_sfii_data.txt', 'w')
        f.close()
            

    isActive = str(input('Would you like to play again (y/n): ')).lower() == 'y'
try:
    f = open('pf_sfii_data.txt', 'r')
    count_words = 0
    count_attempts = 0
    with open('pf_sfii_data.txt') as f:
        for line in f:
            clean = line.split('\n')
            print('aaaaaaaaa')
            count_words += 1
            count_attempts += int(clean[0])
    print(f'you guessed {count_words} words in {count_attempts} attempts')
    f.close()
except:
    print(f'you guessed 1 word in {guess_count} attempts')

# f = open('pf_sfii_data.txt', 'w') #to empty the file in the end
# f.close()
        
print('\nThank you for playing our game.')