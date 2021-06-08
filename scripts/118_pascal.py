def pascal(numrows):
    counter = 1
    prev = 1
    result = []
    while(counter <= numrows):
        if counter == 1:
            current = [1]
        elif counter == 2:
            current == [1,1]
        else:
            current = generate_row(prev,counter)
        result.append(current)
        prev = current
        counter = counter + 1
    return result

def generate_row(previous, length):
    curr_row = []
    counter = 0
    while(counter <= length-1):
        print(counter)
        if counter == 0:
            curr_row.append(1)
        elif counter < length-1 and counter > 0:
            print('in between')
            curr_row.append(previous[counter-1]+previous[counter])
        else:
            curr_row.append(1)
        counter = counter + 1
        print(curr_row)
    
    return curr_row