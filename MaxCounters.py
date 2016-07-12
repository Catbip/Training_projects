# https://codility.com/programmers/task/max_counters/

def solution(N, A):
    highest = 0
    base = 0
    counters = [0] * N
    
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            if counters[A[i]-1] < base:
                counters[A[i]-1] = base + 1
            else: 
                counters[A[i]-1] += 1
                
            if counters[A[i]-1] > highest:
                highest = counters[A[i]-1]
        else:
            base = highest
            
    for x in range(N):
        if counters[x] < base:
            counters[x] = base
            
    return counters
