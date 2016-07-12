# https://codility.com/programmers/task/brackets/

def solution(S):
    stack = []
    pairs = {")": "(",
            "]": "[",
            "}": "{"}
    
    for x in S:
        if x in "([{":
            stack.append(x)
        elif stack == [] or pairs[x] != stack.pop():
            return 0
            
    if stack == []:         
        return 1
    else:
        return 0
