# https://codility.com/programmers/task/odd_occurrences_in_array/

def solution(A):
    # write your code in Python 2.7
    pairs = {}
    
    for x in A:
        if x in pairs:
            del pairs[x]
        else:
            pairs[x] = 1
    
    return pairs.keys()[0]
