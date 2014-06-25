
# coding: utf-8

# In[141]:

# Import necessary packages
import scipy as sp
import numpy as np
from pylab import *
import matplotlib.pyplot as plt


# In[142]:

# Write a program that prints 'Hello World' to the screen.
print 'Hello world!'


# In[143]:

# Write a program that asks the user for his name and greets him with his name.
temp1 = raw_input('Input your name: ')
print 'Greetings, ' + temp1


# In[144]:

# Modify the previous program such that only the users Alice and Bob are greeted with their names.
temp2 = raw_input('What is your name: ')
if temp2 != 'James':
    print 'Intruder alert!'
else:
    print 'Hail, Lord James'
if temp2 == 'Tim':
    print 'Oh...and sup idiot'


# In[145]:

# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
temp3 = input('Input a number: ')
print sum(range(1,temp3+1))


# In[146]:

# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
temp4 = input('Input a number: ')
count = 0
for integer in range(1,temp4+1):
    if integer % 3 == 0:
        count = count + integer
    elif integer % 5 == 0:
        count = count + integer
print count


# In[147]:

# Write a program that asks the user for a number n and gives him the possibility to choose between computing the sum and computing the product of 1,…,n.
temp5 = input('Input a number: ')
temp6 = raw_input('Compute sum or product: ')

if temp6 == 'sum':
    print sum(range(1,temp5+1))
elif temp6 == 'product':
    product = 1
    for integer in range(1,temp5+1):
        product = product*integer
    print product


# In[148]:

# Write a program that prints a multiplication table for numbers up to 12.
import pandas as pa

labels = range(1,13)
data = np.array(range(1,13))

for rows in range(2,13):
    data = np.vstack([data,[x*rows for x in range(1,13)]])
    
output = pa.DataFrame(data,labels,labels)

print output


# In[249]:

# Write a program that takes a number as input and determines if it is prime.            
def isprime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not num & 1:
        return False
    end = num**0.5 + 1
    begin = 3
    
    while begin <= end:
        if num % begin == 0:
            return False
        begin += 2
    
    return True

pnum = input('Enter an integer: ')
if isprime(num):
    print '%s is prime' % num
else:
    print '%s is not prime' % num


# In[6]:

# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether his number was too large or too small. Include a check to make sure the guess is in the correct range.
import random

rnum = random.randint(1,10)

num = input('Guess a number in the set [1,10]: ')

while num > 10 and num < 1:
    print 'Number not in specified range.'
    num = input('Guess a number in the set [1,10]: ')

if num > rnum:
    print 'Too high'
elif num < rnum:
    print 'Too low'
else:
    print 'I let you win'


# In[248]:

# On to lists and strings


# In[ ]:

# Write a function that returns the largest element in a list.
