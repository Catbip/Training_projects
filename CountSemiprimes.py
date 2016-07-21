# https://codility.com/programmers/task/count_semiprimes/

def solution(N, P, Q):    
    ''' Create a list of all prime numers in range N '''
    check = [True]*(N + 1)
    primes = []
    
    for i in range(2, N + 1):
        if check[i] == True:
            primes.append(i)
            j = i*i
            while j <= N:
                check[j] = False
                j += i
    
    ''' Create a list of all semiprime numbers in range N '''
    semiprimes = []
    
    for i in range(len(primes)):
        for j in primes[i:]:
            semiprimes.append(primes[i] * j)
            
    ''' Solve the queries '''
    answ = []
    
    for i in range(len(P)):
        count = 0
        for j in semiprimes:
            if j >= P[i] and j <= Q[i]:
                count += 1
        answ.append(count)
                
    return answ
