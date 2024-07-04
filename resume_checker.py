#!/usr/bin/env python3
#Read a resume and output important values
import re

r= open('resume.txt','r')

def pull_name(text):
        pattern='^[A-Z]+' '[A-Z]+$'
for line in r:
        if re.search
