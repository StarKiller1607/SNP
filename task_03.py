def max_odd(array):
    max = 0
    for i in range(len(array)):
        #for j in range(len(array[i])):
        if type(array[i]) == int or type(array[i]) == float:
            if array[i] % 2 != 0 and array[i] > max:
                max = array[i]
    if max == 0:
        return None
    else:
        return int(max)
