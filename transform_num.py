#!/usr/bin/env python3

#Convert numbers into their corresponding letter

class Num_get:
        def to_Roman(self,num):
                r=['nulla','I','II','III','IV','V']
                ro=r[num]
                return ro
        def to_alpha(self,num):
                a=['N/A','1','2','3','4','5']
                let=a[num]
                return let
print(Num_get().to_Roman(5))
print(Num_get().to_alpha(5))
