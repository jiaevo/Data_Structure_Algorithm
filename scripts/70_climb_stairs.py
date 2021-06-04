def climb(stairs):
    def steps(stairs,lst):
        if stairs >= 1:
            steps(stairs-1,lst)
        if stairs >= 2:
            steps(stairs-2,lst)
        if stairs == 0:
            return lst.append(1)
    
    ways = []
    steps(stairs,ways)
    return len(ways)
