li = list(range(100))
print(li)

# arr[start(include):stop(exclude）:step]

# 每隔5个取一次
print(li[::5])

# 取index=0个到index=2的元素（前3个）
print(li[:3])

# 取index=1个到index=2的元素
print(li[1:3])

# 取index=len-3个到index=len-1的元素（倒数第3个到倒数第2个）
print(li[-3:-1])

#取index=len-1的元素（最后一个）
print(li[-1:])

#注意这里的stop如果使用倒数时，0并不代表最后一个，而是第一个
# 错误的写法,返回一个空数组
print(li[-2:0])
# 正确的写法，返回最后两个元素组成的切片
print(li[-2:len(li)])


# 复制list
copy = li[:]
print(copy)