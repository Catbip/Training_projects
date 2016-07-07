# A non-empty zero-indexed array A consisting of N integers is given. 
# Array A represents numbers on a tape. Any integer P, such that 0 < P < N, 
# splits this tape into two non-empty parts. The difference between 
# the two parts is the absolute difference between the sum of the first part 
# and the sum of the second part. 

# Write a function def solution(A) that, given a non-empty zero-indexed array A of N integers, 
# returns the minimal difference that can be achieved.

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
