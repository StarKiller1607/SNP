def sort_list(list):
    if list == []:
        return []
    ma = max(list); maxp = []; mi = min(list); minp = []
    for i in range(len(list)):
        if list[i] == ma:
            maxp.append(i)
        elif list[i] == mi:
            minp.append(i)
    for i in range(len(maxp)):
        list[maxp[i]] = mi
    for i in range(len(minp)):
        list[minp[i]] = ma
    list.append(mi)
    return list
