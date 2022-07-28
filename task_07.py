def combine_anagrams(words_array):
    arr = list(words_array)
    combined = []
    j = 0
    count = []
    while len(arr) > 0:
        combined.append([arr[0]])
        s = sorted(arr[0])
        del(arr[0])
        for i in range(len(arr)):
            if sorted(arr[i]) == s:
                combined[j].append(arr[i])
                count.append(i)
        for i in range(len(count)):
            del(arr[count[i]-i])
        j += 1
        count = []
    return(combined)