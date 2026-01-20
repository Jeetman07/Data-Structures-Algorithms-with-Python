def combine_lists(list1,list2):
    newlist = []
    position = 0
    i = 0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            newlist.append(list1[i])
            i+=1
        else:
            newlist.append(list2[j])
            j+=1
    newlist.extend(list1[i:])
    newlist.extend(list2[j:])
    return newlist