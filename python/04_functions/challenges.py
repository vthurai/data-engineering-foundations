'''
QUESTION 1.
Write a function called is_palindrome.
is_palindrome takes a string as an argument. It returns True if the given string is a palindrome.
print(is_palindrome("racecar")) >> True
print(is_palindrome("aabbcc")) >> False
'''

def is_palindrome(word):
  return word == word[::-1]


'''
QUESTION 2.
Write a function called get_palindromes.
get_palindromes takes a string as an argument.
It returns a list of substrings which are palindromes.
print(get_palindromes("racecar")) >> ['racecar', 'aceca', 'cec']
print(get_palindromes("aabbbaa")) >> ['aabbbaa', 'aa', 'abbba', 'bbb', 'bb', 'bb', 'aa']
'''

def get_palindromes(word):
  pal_list = []
  for i in range(len(word)):
    for j in range(len(word[i:])):
        s = word[i: i+j+1]
        if s == s[::-1] and len(s)>1:
           pal_list.append(s)
  return pal_list
