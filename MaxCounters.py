You are given N counters, initially set to 0, and you have two possible operations on them:
increase(X) − counter X is increased by 1, max counter − all counters are set to the maximum value of any counter.
A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:
if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X), if A[K] = N + 1 then operation K is max counter.

Write a function def solution(N, A) that, given an integer N and a non-empty zero-indexed array A consisting of M integers, 
returns a sequence of integers representing the values of the counters.

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
