def med3(a, b, c):
    if (b >= a and a >= c) or (c >= a and a >= b):
        return a
    elif (a > b and b > c) or (c > b and b> a):
        return b
    else:
        return c
    
a = int(input())
b = int(input())
c = int(input())

print('{}'.format(med3(a, b, c)))