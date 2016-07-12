Write a function def solution(S) that, given a string S consisting of N characters, 
returns 1 if S is properly nested and 0 otherwise.

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
