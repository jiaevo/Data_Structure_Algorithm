def maxarray(ls):
    local_max = 0
    global_max = 0
    for i in ls:
        print('current element:{}'.format(i))
        print('current max:{}'.format(local_max))
        local_max = max(i, local_max+i)
        print('updated max:{}'.format(local_max))
        if local_max > global_max:
            global_max = local_max
        print('global max:{}'.format(global_max))
    return global_max