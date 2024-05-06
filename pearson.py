#!/usr/bin/env python3
import pandas as pd
import math as m
import numpy as np
df=pd.read_csv('/root/nicko/bioinformatics_proj/AZD6244_cleaned.csv')
#Total of all x and all y
x_sum=df['ic50_effect_size'].sum()
y_sum=df['fdr'].sum()

#Total of all x**2 and y**2
df.insert(2,'ic50_effect_size sq',[i**2 for i in df['ic50_effect_size']],True)
df.insert(3,'fdrsq',[i**2 for i in df['fdr']],True)
xsq_sum=df['ic50_effect_size sq'].sum()
ysq_sum=df['fdrsq'].sum()

#Total of all x*y
df.insert(4,'x_mult_y',df['ic50_effect_size']*df['fdrsq'],True)
x_mult_y=df['x_mult_y'].sum()

#Calulate r in pearson correlation equation.

def pearson(xsum,ysum,xsqsum,ysqsum,xmult_y):
        r=((10*(xmult_y)-((xsum)*(ysum)))/m.sqrt((xsqsum-(xsum)**2)*(ysqsum-(ysum)**2)))
        return r
print(pearson(x_sum,y_sum,xsq_sum,ysq_sum,x_mult_y))
