def  connect_dicts(dict1, dict2):
    c =[]
    sumv1, sumv2 = 0, 0
    for value in dict1.values():
        sumv1 += value
    for value in dict2.values():
        sumv2 += value
    if sumv1 > sumv2:
        for key in dict2.keys():
            if key in dict1.keys() and dict1[key] >= 10:
                c.append(key)
        for i in range(len(c)):
            del(dict2[c[i]])
    else:
        for key in dict1.keys():
            if key in dict2.keys() and dict2[key] >= 10:
                c.append(key)
        for i in range(len(c)):
            del(dict1[c[i]])
    d = {}
    for key in dict1.keys():
        if dict1[key] >= 10:
            d[key] = dict1[key]
    for key in dict2.keys():
        if dict2[key] >= 10:
            d[key] = dict2[key]
    return({i: j for i, j in sorted(d.items(), key=lambda item: item[1])})