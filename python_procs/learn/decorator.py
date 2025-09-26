import time, functools

#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kwargs):
#         t = time.time()
#         ret = fn(*args,**kwargs)
#         print("执行%s一共耗时%f s" %(fn.__name__ , time.time()-t))
#         return ret
#     return wrapper
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print('测试成功!')


def log(arg):
    def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kwargs):
                if isinstance(arg, str):
                    print('%s %s()...' % (arg, fn.__name__))
                    return fn(*args, **kwargs)
                else:
                    print('call %s()...' % fn.__name__)
                    return fn(*args, **kwargs)
            return wrapper

    if isinstance(arg, str):
        return decorator
    else:
        return decorator(arg)



# def log(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kwargs):
#         print('call %s()...' % fn.__name__)
#         return fn(*args, **kwargs)
#     return wrapper

@log
def f1():
    pass


@log('execute')
def f2():
    pass


f1()

f2()