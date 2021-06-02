def search_rotated(arry, num):
    #check if it's rotated, find pivot point
    pivot = find_pivot(arry)
    #compare with pivot point, to see if search on left or right of pivot point
    start = pivot
    left = 0
    right = len(arry) - 1  

    if num >= arry[start] and num <= arry[right]:
        left = start
    else:
        right = start
    
    return binary_search(arry = arry[left:right],target = num)

def find_pivot(array):
    left = 0
    right = len(array) - 1
    
    while(left <= right):
        mid = left + (right-left)//2
        if array[mid] > array[right]:
            left = mid + 1
        else:
            right = mid 
    return left

def binary_search(arry,target):
    left = 0
    right = len(target) - 1
    while(left <= right):
        mid = left + (right - left)//2
        if target == arry[mid]:
            return mid
        elif target >= arry[mid]:
            left = mid + 1
        else:
            right = mid - 1

