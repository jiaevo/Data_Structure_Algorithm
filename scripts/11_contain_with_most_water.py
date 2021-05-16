
def maxarea(height):
    l = 0
    r = len(height)-1
    area = 0

    while l < r:
        area = max(area,min(height[l],height[r]) * (r - l))
        if height[l] <= height[r]:
            l = l+1
        elif height[l] > height[r]:
            r = r-1
    return area
