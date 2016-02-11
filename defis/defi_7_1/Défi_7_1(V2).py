def pyramid():
    x = int(input("Entrez "))
    y = x // 2
    print((y) * ' ' + '*')
    for i in range(y - 1):
        print(' ' * (y - i - 1) + '*' + ' ' * (2 * i + 1) + '*' + ' ' * (y - i - 1))
    print('*' * x)


pyramid()
