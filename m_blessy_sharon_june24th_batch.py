# -*- coding: utf-8 -*-
"""M.Blessy sharon june24th batch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GcKXRiDircrvK0i0MrS9ZmhEPmVcqfE-
"""

#Question 1: Write a Python program to count the number of characters in a string without using len function.

var = 'python java'
count = 0
for char in var:
  count += 1
print('result:',count)

"""### Question 2: Write a Python program to reverse a string without using [::-1]"""

var = 'python'
reversed_var = ''
for i in range(len(var)-1,-1,-1):
  reversed_var += var[i]
print('result :',reversed_var)

"""Question 3: Write a Python program to check if a string is a palindrome don't use [::-1].

"""

var = 'NUN'
is_palindrome = True
length = 0
for char in var:
  length += 1
for i in range(length // 2):
  if var[i] !=var[length -i - 1]:
     is_palindrome = False
if is_palindrome:
  print('result : it is a palindrome')
else:
  print('result : it is not a palindrome')

#Question 4: Write a Python program to find the most common character in a string.
var = 'Hello World'
char_count = {}
for char in var:
  if char !=' ':
    char_count[char]=char_count.get(char,0)+1
    most_common_char = max(char_count,key=char_count.get)
print(f'result : {most_common_char},because {most_common_char} is repeating{char_count[most_common_char]} times')

#Question 5: Write a Python program to check if two strings are anagrams.
var1 = 'listen'
var2 = 'silent'
var1 = var1.replace(' ','').lower()
var2 = var2.replace(' ','').lower()
char_count1 = {}
char_count2 = {}
for char in var1:
  char_count1[char] = char_count1.get(char,0)+1
for char in var2:
  char_count2[char] = char_count2.get(char,0)+1
if char_count1 == char_count2:
   print('result : both are anagram because characters in var2 are in var1')
else:
   print('result :both are not anagram beacuse characters in var2 are not in var1')

#Question 6: Write a Python program to remove all the vowels from a string.
var = 'python'
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in var:
  if char in vowels:
    pass
  else:
    print(char,end='')

#Question 7: Write a Python program to find the longest word in a string.
var = 'python is Easy Language'
words =var.split()
longest_word = ''
max_length = 0
for word in words:
  if len(word)>max_length:
    longest_word = word
print(f'result : {longest_word}')

#Question 8: Write a Python program to capitalize the first letter of each word in a string [dont use built-in-function title].
var = 'python is easy'
words = var.split()
result = ' '.join(word[0].upper() +word [1:] for word in words)
print(f'result : {result}')

#Question 9: Write a Python program to find the frequency of each character in a string.
var = 'sharuk Khan'
char_count = {}
for char in var:
  if char in char_count:
    char_count[char]+=1
  else:
      char_count[char] = 1
print(f'result : {char_count}')

var = 'sharuk khan'
even_ascii_sum = 0
for char in var:
  ascii_value =ord(char)
  if ascii_value% 2 ==0:
    even_ascii_sum += ascii_value
print(f'result : {even_ascii_sum}')

