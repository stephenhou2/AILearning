# 常规参数
print("---------------------------------常规参数---------------------------")
def simple_args(name,age):
    print("name:",name)
    print("age:", age)

# 位置传参
simple_args("张三", 10)

# 具名传参
simple_args(name="张三",age=20)

# simple_args(name="张三",20)   错误，具名传参的后面不能再跟位置参数，因为已经没有位置信息
# simple_args(20, name="张三")  错误，第一个参数20会被解析为位置参数，传递给形参name，再次使用具名参数name时，会报重复传参

# 可变位置参数
print("-------------------------------可变位置参数-----------------------------")
def foo_variable_pos_args(name, age, *args):
    print("name:",name)
    print("age:", age)
    for index,element in enumerate(args):
        print(index,element)

foo_variable_pos_args("张三", 10,  2, 3)
arr = [2,3]
foo_variable_pos_args("张三", 10,  *arr)



# 关键字参数
print("-------------------------------关键字参数-----------------------------")
def foo_variable_kw_args(name, age, **kwargs):
    print("name:",name)
    print("age:", age)
    for key,value in kwargs.items():
        print(key,value)

foo_variable_kw_args("张三", 10, a=1,b='helloworld')
dict = {"a":1,"b":'helloworld'}
foo_variable_kw_args("张三", 10, **dict)


# 混合使用
print("-------------------------------各种参数混合使用-----------------------------")
def foo_multi_args(name, age=10, *args, **kwargs):
    print("name:",name)
    print("age:", age)

    for index,element in enumerate(args):
        print(index,element)

    for key,value in kwargs.items():
        print(key,value)

foo_multi_args("张三", 20, 2,3, a=1,b='helloworld')
foo_multi_args("张三", 20, *arr,**dict)