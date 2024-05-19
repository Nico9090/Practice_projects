#!/usr/bin/env python3

num_subj=int(input('How many subjects? '))
subj=[]
scores=[]
for i in range(0,num_subj):
        subj.append(input('Enter the subject: '))
        scores.append(input('Enter score: '))
for i in range(len(subj)):
        print(subj[i],' ',scores[i])
