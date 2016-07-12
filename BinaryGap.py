# https://codility.com/programmers/task/binary_gap/

def solution(N):
    # write your code in Python 2.7
    
    is_gap = False
    count = 0
    gap = 0
    
    while N > 0:
        if N%2 == 0 and is_gap:
            count += 1
        elif N%2 == 1:
            is_gap = True
            if count > gap:      
                gap = count
            count = 0
        N = N//2
                       
return gap
