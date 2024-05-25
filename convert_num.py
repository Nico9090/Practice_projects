#!/usr/bin/env python3
class Convert:
        def to_Roman(self,num):
                """Works for only numbers 1 through 20. Brainstorming more efficient ways"""
                while num>=1 and num<4:
                        r='I'*num
                if num==4:
                        r='IV'
                while num>4 and num<=8:
                        r='V'+'I'*(num-5)
                if num == 9:
                        r='IX'
                while num>14 and num<19:
                        r='X'+'V'+'I'*(num-15)
                if num == 20:
                        r='XX'
                return r
print(Convert().to_Roman(3))

#Problem with this code is that the it runs indefinitely. 
