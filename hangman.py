
import random

#Program selects a random word from the list given
word_list=['banana','apple','pineapple','mango']
word=random.choice(word_list)

#Pre-game state
chances=len(word)+2

dashes='_'*len(word)

#Game mechanics
while chances>0:
        print(dashes)
        user_choice=input('Guess a letter: ')
        if user_choice in word:
                for i in range(len(dashes)):
                        if i==word.index(user_choice):
                                dashes=dashes[0:i]+user_choice+dashes[i:-1]
        else:
                chances-=1

if chances ==0:
        print('You lose','The word was ', word,'.')
