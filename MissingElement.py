# https://codility.com/programmers/task/perm_missing_elem/

def solution(A):
  sum_a = sum(A)
  sum_b = sum(range(1, len(A) + 2))
  
  return sum_b - sum_a
