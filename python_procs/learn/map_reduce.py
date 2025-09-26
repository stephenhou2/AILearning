from functools import reduce


def squre(x):
    return x * x

r = map(squre,[1,2,3,4,5])
print(r)
print(list(r))

def contact(x,y):
    return '' + x + y

s1 = reduce(contact,['a','b','c','d','e','f','g'])

print(s1)


def prod(L):
    return reduce(lambda x,y :  x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':-1}

def to_num(s):
    return  DIGITS[s]


def str2float(s):
    numbers = map(to_num,s)
    point = 0

    def to_float(x, y):
        nonlocal point

        if y == -1:
            point = 1
            return x

        if point == 0:
            return x * 10 + y
        else:
            point *= 10
            return x + y/point


    return reduce(to_float,numbers)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')