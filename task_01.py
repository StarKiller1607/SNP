def is_palindrome(string):
    import re
    string = str(string)
    string = string.lower()
    line = ''; rev = ''
    string = re.split(r'\W+', string)
    for i in range(len(string)):
        line += string[i]
    for i in range(len(line)-1, -1, -1):
        rev += line[i]
    return line == rev
