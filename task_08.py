def multiply_numbers(inputs = None):
    if inputs == None:
        return inputs
    mult, count = 1, 0
    if type(inputs) == float:
        inputs = str(inputs).split('.')
    for i in range(len(inputs)):
        if str(inputs[i]) in '0123456789':
            mult *= int(inputs[i])
            count += 1
    if count == 0:
        return None
    else:
        return mult