def  count_words(string):
    import re
    string = re.split(r'\W+', string.lower())
    count = {}
    for i in range(len(string)):
        if string[i] not in count.keys():
            count[string[i]] = 1
        else:
            count[string[i]] += 1
    return count