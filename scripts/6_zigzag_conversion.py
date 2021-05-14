# flip_insert = -1
# n = 3
# zigzag_list = ['']*n
# strs = 'abcd'
# row_number = 0
# flip_insert = 1


def zigzag(strs,n):
    zigzag_list = ['']*n
    row_nmber = 0
    flip_insert = 1
    for i in range(0,len(strs)):
        zigzag_list[row_number] = zigzag_list[row_number] + strs[i]
        if row_number < n - 1 and flip_insert == 1:
            row_number = row_number + 1
        elif row_number > 0 and flip_insert == -1:
            row_number = row_number - 1
        else:
            flip_insert = flip_insert * -1
            row_number = row_number + flip_insert

    # row_to_insert = i % n  - 1
    # if flip_insert == -1:
    #     zigzag_list[row_to_insert].append(str[i])
    # elif flip_insert == 1:
    #     zigzag_list[n - row_to_insert + 1].append(str[i])
    # if row_to_insert - 1 == 0:
    #     flip_insert = flip_insert * -1
    # if flip_insert == 1 and i+1 % n == 1:
    #     flip_insert = flip_insert * -1
    return zigzag_list
