from ast import Str
import math
import string

#1.	Write a short program to read the appropriate variables, 
#then calculate and output the result of the expression:
#Length:  root of((y-l)^2 + x^2)

y, l, x = input ("Enter your y , l , and x:  ").split()
Length = (float(y)*float(y)*float(l))+float (x)*float (x)
Length2 = math.sqrt(Length)
print("The Length is: ", Length2)