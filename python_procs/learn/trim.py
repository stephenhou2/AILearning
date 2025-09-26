# def trim(s):
#     if not s:
#         return s
#
#     if(s[0] == ' '):
#         return trim(s[1:])
#     elif(s[-1] == ' '):
#         return trim(s[:-1])
#     else:
#         return s


def trim(s):
    while s and s[0] == ' ':
        s = s[1:]

    while s and s[-1] == ' ':
        s = s[:-1]

    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


