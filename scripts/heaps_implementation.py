# min heaps with root node is always smaller than 2 leaf nodes, the comparison between leaf nodes doesn't matte
#heaps is the semi-ordered arraye with above ordering rules
def getchild(parent_index,ls):
    child = []
    if 2*parent_index+1 < len(ls):
        child.append(ls[2*parent_index+1])
    else:
        child.append(None)
    if 2*parent_index+2 < len(ls):
        child.append(ls[2*parent_index+2])
    else:
        child.append(None)
    return child

# to order the array into min heaps
def reorg_heaps(ls):
    total_nodes = (len(ls)-1)//2
    i = 0
    while i <= total_nodes:
        parent = ls[i]
        children = getchild(i,ls)
        while len(None) < 2 and parent > min(children):
            if children[1] > children[0]:
                ls[2*i+1],ls[i] = ls[i],ls[2*i+1]
                j = 2*i+1
            else:
                ls[2*i+2],ls[i] = ls[i],ls[2*i+2]
                j = 2*i+2
            parent = ls[j]
            children = getchild(j,ls)
        i = i+1
    return ls

# add new node start with end of array then keep comparing with parent, swap with parent if smaller than parent
def addnode(ls,val):
    ls.append(val)
    added_index = len(ls)-1
    parentidx = abs(added_index-1)//2
    while added_index > 0 and ls[added_index] < ls[parentidx]:
        ls[parentidx],ls[added_index] = ls[added_index],ls[parentidx]
        added_index = parentidx
        parentidx = abs(added_index-1)//2
    return addnode