# A non-empty zero-indexed array A consisting of N integers is given. 
# The array contains an odd number of elements, and each element of 
# the array can be paired with another element that has the same value, 
# except for one element that is left unpaired. Write a function 
# def solution(A) that, given an array A consisting of N integers 
# fulfilling the above conditions, returns the value of the unpaired element.

def solution(A):
    # write your code in Python 2.7
    pairs = {}
    
    for x in A:
        if x in pairs:
            del pairs[x]
        else:
            pairs[x] = 1
    
    return pairs.keys()[0]
