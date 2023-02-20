'''
QUESTION 1.
Write a function that returns the nth fibonnacci number (1, 1, 2, 3, 5, 8 ... etc.)
Use recursion.
print(fibonnacci(1)) >> 1
print(fibonnacci(2)) >> 1
print(fibonnacci(5)) >> 5
'''

def fibonnacci(n):
  pass


'''
QUESTION 2.
Write the binary search function from the previous challenge using recursion this time.
'''

def binary_search_recursive(sorted_list, n):
  pass


'''
QUESTION 3.
We want a function that will sort a list of integers in order from least to greatest.
We will use a method of sorting called merge sort. This uses a "divide and conquer" algorithm.

Merge sort will take a list and sort it. To implement merge sort:
Step 1: Pick a point in the middle of the list.
Step 2: Divide the list from the middle into a left sublist and a right sublist.
Step 3: Recursively call merge_sort() on both left and right sublists. Don't forget your base case!
Step 4: Now we need to merge the two lists into one sorted list. To do this:
  Step 4a: Compare the first element of both left and right sublists. You should keep track of their indicies to make things easier.
  Step 4b: Pick the smaller element and place it in the correct position in the original list.
  Step 4c: Move on to the next index. Compare elements again, place, and continue until both left and right lists are exhausted. 
  Step 4d: If there are any elements remaining that were not compared, move them to the original list.
Step 5: The two lists are now merged. The recursive call should take care of the rest, and the list will now be sorted.

unsorted = [5, 17, 0, -31, 14, 8, 66, -2, 6, 22]
merge_sort(unsorted)
print(unsorted) >> [-31, -2, 0, 5, 6, 8, 14, 17, 22, 66]
'''

def merge_sort(lst):
  pass
