# jtyurkovich, 2014

# coding: utf-8

# In[1]:

# Write a script that takes this string as input and breaks the code to read the message contained within:
# espqtcdeapcdzyezdzwgpestdrpedespstrspdezqqtgpd
# This code was encrypted using a shift cipher of 11 (t = t + 11 = e, h = h + 11 = s). Hint: use a dict to define the shift (code dict using a for loop; do not hardcode it) and cycle through the message using a for loop.

code = 'espqtcdeapcdzyezdzwgpestdrpedespstrspdezqqtgpd'
abc = 'abcdefghijklmnopqrstuvwxyz'*2

cipher = {}
deciphered = ''

for index in range(26,52):
    cipher[abc[index]] = abc[index - 11]

for letter in code:
    deciphered += cipher[letter]
    
print code
print deciphered


# In[16]:

# Write a script that takes a string as input and determines if it is a palindrome or not. A palindrome is a word or phrase that is the same forward and backward (e.g., radar).
def ispalindrome(word):
    length = len(word)
    word.replace(' ','')
    
    for index in range(0,length/2):
        if word[index] != word[length-index-1]:
            return False
        
        return True
            
word = raw_input('Enter a word: ')

if ispalindrome(word):
    print word+' is a palindrome'
else:
    print word+' is not a palindrome'
