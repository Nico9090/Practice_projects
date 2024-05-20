#!/usr/bin/env python3

#Convert numbers into their corresponding letter

class Into_Let:
        def __init__(self,num):
                self.num=num
        def to_let(self):
                letters=['first','a','b','c','d','e','f']
                print(letters[self.num])
num1=Into_Let(1)
print(num1.to_let())


