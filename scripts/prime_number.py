def isprime(num):
    prime_ind = 0
    for i in range(1,num+1):
        temp = num%i
        if i != 1 and i != num and temp == 0:
            prime_ind = 1
        if prime_ind == 1:
            return 'is not prime'
    return 'is prime'