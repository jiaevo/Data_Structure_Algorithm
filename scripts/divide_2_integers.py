#brutal force, O(N)
def divide(dividend,divisor):
    quotient = 0
    negative_ind = (dividend < 0) ^ (divisor < 0)
    if negative_ind:
        if dividend < 0:
            dividend = -dividend
        elif divisor < 0:
            divisor = -divisor

    while(dividend >= divisor):
        dividend = dividend - divisor
        quotient = quotient + 1
    
    if negative_ind:
        quotient = -quotient
    return quotient

#double divsior every interation, nearly O((logN)^2)
def divide1(dividend,divisor):
    quotient = 0
    negative_ind = (dividend < 0) ^ (divisor < 0)
    if negative_ind:
        if dividend < 0:
            dividend = -dividend
        elif divisor < 0:
            divisor = -divisor

    quotient = 0

    while(dividend >= divisor):
        accum = divisor
        i = 1
        while(accum + accum <= dividend and accum < pow(2,31)>>1):        
            accum = accum + accum
            i = i + i
        dividend = dividend - accum
        quotient = i + quotient
    
    if negative_ind:
        quotient = -quotient
    return quotient
#find the max divsior first, then subtract it from dividend, then shift counter back to 0 nearly O(logN)
def divide2(dividend,divisor):
    quotient = 0
    negative_ind = (dividend < 0) ^ (divisor < 0)
    if negative_ind:
        if dividend < 0:
            dividend = -dividend
        elif divisor < 0:
            divisor = -divisor
    quotient = 0
    i = 1
    accum = divisor
    while(accum+accum < dividend and accum < pow(2,31)>>1):
        accum = accum + accum
        i = i << 1
    while(dividend >= divisor):
        print(i)
        print(accum)
        print(dividend)
        if(dividend >= accum):
            print('in')
            dividend = dividend - accum
            quotient = i + quotient
            print(quotient)
        accum = accum >> 1
        i = i >> 1

    if negative_ind:
        quotient = -quotient
    return quotient