def addBinary(a,b):
    i = len(a)-1
    j = len(b)-1
    sum_binary = []
    temp = 0
    carry = 0
    while(i >= 0 or j >= 0):
        if i < 0:
            temp = (int(b[j])+carry)%2
            carry = (int(b[j])+carry)//2
        elif j < 0:
            temp = (int(a[i])+carry)%2
            carry = (int(a[i])+carry)//2
        else:
            temp = (int(a[i])+carry+int(b[j]))%2
            carry = (int(a[i])+carry+int(b[j]))//2
        i = i-1
        j = j-1
        sum_binary.insert(0,str(temp))
    if carry != 0:
        sum_binary.insert(0,str(carry))
    return sum_binary