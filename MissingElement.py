# A zero-indexed array A consisting of N different integers is given. 
# The array contains integers in the range [1..(N + 1)], which means 
# that exactly one element is missing. Your goal is to find that missing element.

# Write a function def solution(A) that, given a zero-indexed array A, 
# vreturns the value of the missing element.

def solution(A):
  sum_a = sum(A)
  sum_b = sum(range(1, len(A) + 2))
  
  return sum_b - sum_a
