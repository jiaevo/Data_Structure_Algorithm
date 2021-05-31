#without modifying the nums1
def merge(nums1, m, nums2, n):
    total = 0
    point_1 = 0
    point_2 = 0
    merged_array = []
    while(total < m+n):
        print('total:{}'.format(total))
        if m == 0:
            merged_array = nums2
            break
        if n == 0:
            merged_array = nums1
            break
        if(nums1[point_1] <= nums2[point_2] and nums1[point_1] != 0):
            merged_array.append(nums1[point_1])
            print('append nums1')
            point_1 = point_1+1
        else:
            merged_array.append(nums2[point_2])
            print('append nums2')
            point_2 = point_2+1
        total = total + 1
    nums1 = merged_array
    return nums1

#modifying nums1 in place
def merge1(nums1, m, nums2, n):
    point_1 = 0
    point_2 = 0
    while(nums1[len(nums1)-1]==0):
        if m == 0:
            nums1.pop(0)
            nums1.extend(nums2)
            break
        if nums1[point_1] == 0:
            if point_2 <= len(nums2)-1:
                nums1[point_1] = nums2[point_2]
                point_1 = point_1+1
                point_2 = point_2+1
        else:
            if nums1[point_1] >= nums2[point_2]:
                nums1.insert(point_1+1,nums2[point_2])
                nums1.pop(len(nums1)-1)
                point_1 = point_1+2
                print('insert num2')
                point_2 = point_2+1
            else:
                point_1 = point_1+1
                print('do nothing')
        
    
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge1(nums1,m,nums2,n)