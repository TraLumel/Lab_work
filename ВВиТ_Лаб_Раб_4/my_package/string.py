def reverse (x):
    return x[::-1]
def lesenka (x):
    s=''
    for i in range(len(x)):
        if i % 2 == 0:
            s += x[i].upper()
        else:
            s += x[i].lower()
    return s
