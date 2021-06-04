def find_first_binary_search(lst,num):
    i = 0
    j = len(lst) - 1
    first = -1
    while(i<=j):
        middle = i + (j-i)//2
        if lst[middle] >= num:
            j = middle - 1
        else:
            i = middle + 1
        if lst[middle] == num:
            first = middle
    return first

def find_last_binary_search(lst,num):
    i = 0
    j = len(lst) - 1
    last = -1
    while(i<=j):
        middle = i + (j-i)//2
        if lst[middle] <= num:
            i = middle + 1
        else:
            j = middle -1
        if lst[middle] == num:
            last = middle
    return last


def first_last_pos(lst,num):
    if len(lst) == 0:
        return [-1,-1]
    first_app = find_first_binary_search(lst,num)
    last_app = find_last_binary_search(lst,num)
    return [first_app,last_app]



    
