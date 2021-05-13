def removeDuplicates(nums):
    prev = None
    current = None
    new_list = []
    for i in nums:
        current = i
        if current != prev:
            new_list.append(current)
        prev = current
    return new_list
