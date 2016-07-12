# https://codility.com/programmers/task/tape_equilibrium/

def solution(A):
    # write your code in Python 2.7
    sum2 = A.pop()
    sum1 = sum(A)
    diff = abs(sum1 - sum2)
    
    while len(A) > 1:
        a = A.pop()
        sum1 = sum1 - a
        sum2 += a
        total = abs(sum1 - sum2)
        
        if total < diff:
            diff = total
            
    return diff
