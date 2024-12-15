def sum(x=0, y=0):
    try:
        return int(x)+int(y)
    except ValueError:
        print('Неверно указанно число.')