def plus_one(ls):
    add_ls = []
    carry_on = 0
    for i in range(len(ls)-1,-1,-1):
        print('carry_on:{}'.format(carry_on))
        print('current digit:{}'.format(ls[i]))
        if i == len(ls)-1:
            added = ls[i]+1
        else:
            added = ls[i]+carry_on
        digit = added%10
        print('updated digit:{}'.format(digit))
        carry_on = added//10
        add_ls.insert(0,digit)
    if carry_on != 0:
        add_ls.insert(0,carry_on)
    return add_ls
