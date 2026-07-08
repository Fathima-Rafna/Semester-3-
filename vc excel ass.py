print("hi rafna")
print(1,2,3,4,)
print(1+7)
print(2*5)

a = 10
b = 20 

print("addition:", a+b)
print("subtraction:", a-b)
print("product:", a*b)
print("division:",a/b)

print("*"*10)

for i in range(1,6):
    print(i)
for i in range(4):
    print(i)    

for i in range(18,30,3):
    print(i)    
for i in range(1,6):
    print("*"*i)    

import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt
rafna = pd.read_excel("s3_july(2026).xlsx")
print(rafna.head())

print("First Five Rows")
print(rafna.head())

print("\nDataset Shape")
print(rafna.shape)

print("\nColumn Names")
print(rafna.columns.tolist())