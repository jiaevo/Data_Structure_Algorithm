def mysqrt(x):
    possible_sol = list(range(1,x//2+1))
    filter_sol = possible_sol
    while len(filter_sol) > 1:
        if len(filter_sol)%2 == 0:
            middle = (filter_sol[len(filter_sol)//2-1] + filter_sol[len(filter_sol)//2])/2
        else:
            middle = filter_sol[len(filter_sol)//2]
        if x <= middle*middle:
            filter_sol = filter_sol[0:len(filter_sol)//2]
        elif x >= middle*middle:
            filter_sol = filter_sol[len(filter_sol)//2:len(filter_sol)]

    if filter_sol[0]*filter_sol[0] > x:
        sqrt_solution = filter_sol[0] - 1
    else:
        sqrt_solution = filter_sol[0]
    return sqrt_solution


def binarysearch(ls,l,r,num):
    if r >= l:
        mid = l + (r-l)//2

        if ls[mid] == num:
            return mid
        elif ls[mid] > num:
            binarysearch(ls,l,mid-1,num)
        elif ls[mid] < num:
            binarysearch(ls,mid+1,r,num)
    else:
        return -1