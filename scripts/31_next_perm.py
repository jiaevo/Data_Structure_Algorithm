def permute(nums):
    start = len(nums)-1
    start_next = start - 1
    flag = 0
    if len(nums) == 1:
        return
    while(start_next != 0):
        if nums[start] > nums[start_next]:
            print('in')
            i = nums[start]
            j = nums[start_next]
            nums[start] = j
            nums[start_next] = i
            break
        elif nums[start] < nums[start_next]:
            flag = 1
            break
        start = start - 1
        start_next = start_next - 1
    if flag == 1:
        nums.sort()
    