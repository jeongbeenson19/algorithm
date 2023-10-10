def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    
a = int(input('정수 a: '))
b = int(input('정수 b: '))
c = int(input('정수 c: '))

print('중앙값은 {}입니다.'.format(med3(a, b, c)))