def coincidence(list=[], range=0):
    list2 = []; i = 0
    while i < len(list):
        if type(list[i]) == int or type(list[i]) == float:
            if list[i] >= range[0] and list[i] <= range[-1]:
                list2.append(list[i])
        i += 1
    list2.sort()
    return list2
