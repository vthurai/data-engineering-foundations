'''
QUESTION 1.
Write a function called is_palindrome.
is_palindrome takes a string as an argument. It returns True if the given string is a palindrome.
print(is_palindrome("racecar")) >> True
print(is_palindrome("aabbcc")) >> False
'''
def is_palindrome():
    pass


'''
QUESTION 2.
Write a function called get_palindromes.
get_palindromes takes a string as an argument.
It returns a list of substrings which are palindromes.
print(get_palindromes("racecar")) >> ['racecar', 'aceca', 'cec']
print(get_palindromes("aabbbaa")) >> ['aabbbaa', 'aa', 'abbba', 'bbb', 'bb', 'bb', 'aa']
'''
def get_palindromes():
    pass


'''
QUESTION 3
Binary Search.
Write a function called binary_search.
binary_search takes two arguments: a *sorted* list of numbers, and a number to search for.
binary_search returns the index of the given number inside the list.
(You can assume the given number will always be in the list)
First, try to write this function yourself, and don't use any built-in functions.

Now, try to write the function using the "binary search" method.
Binary search works as follows:
Step 1: Pick a point inside the list. The middle of the list would be a good starting point.
Step 2: If the two numbers are equivalent, then return it's index and we are done.
Step 3: If the number is not the correct one, compare the two. Search the left side of the list
        if the chosen number is less than the list number, or the right side if it is greater.
Step 4: Repeat until the number is found, and return it's index.

print(binary_search([-2, 0, 6, 9, 11, 27], 0)) >> 1

Is this method of searching more "efficient" than the first one you wrote? Why or why not?
Consider for instance, the steps you take when searching for a word inside a (real) dictionary.
'''
def binary_search():
    pass