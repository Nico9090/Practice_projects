#!/usr/bin/env python3
import numpy as np
import random

print('Whole numbers please!')
uplim=int(input('What is the highest number? '))
lowlim=int(input('What is the lowest number? '))

chosen_num=random.randint(lowlim,upplim+1)

print(chosen_num)
while chances!=0:
        sele_num=int(input('Guess a number! '))
        if sele_num==chosen_num:
                print('You guessed right!')
                break
        else:
                print('Sorry, wrong guess :(')
                chances-=1
                print('You have ',chances,' more tries.')
