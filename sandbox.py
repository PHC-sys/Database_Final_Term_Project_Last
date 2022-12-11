def converter(*args):
    length = len(args)
    string = ''
    for i in range(length):
        string += args[i]
        if length-i == 1:
            break
        string += ','
    return string
