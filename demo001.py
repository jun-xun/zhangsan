# a=input("请输入：")
# b=input("请输入：")
# print("两串字符串长度和为：",len(a)+len(b))

#元组，下标，从0开始编号
# a=(1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","哈哈","西西",True,False) #
# print(a[-3])
# #切片
# print(a[0:4]) # 左闭右开
# print(a[4:10])
# print(a[10:])

# print(a.index("西西"))
# print(a.count("哈哈"))
#二维元组
# b=(a,"哈哈","喜喜")
# print(b[0][3])

# 数组
# a=[1,2,3,4,"哈哈","西西",True,False]
# a.append("append1")
# a.append("append2")
# # print(a)
#元组一旦写好之后不可以修改，而数组是可以修改的
# a.insert(2,"insert")
# print(a)
# b = a.pop(0) # 剪切
# c = a.pop(0) # 剪切
# print(b+c)
# print(b)
# # a.clear()
#
# xx = ["你好","不好"]
# # a.extend(xx)
# print(a+xx)
# print(a)
# a.remove("哈哈")
# print(a)

# # 下标不要超出范围 = 越界
# xx = [a,0,1,2,3]
# xx[99]

"""
python的语法：
所有的方法都是以小括号结尾的。比如，print(),input(),len()
元组，数组，字典的取值，，都是用中括号，比如 a[0]
元组，数组，字典的定义，分别是(),[],{}
"""


"""
字典的特点：
1，字典中的值没有顺序。
2，字典的结构必须是 键值对的结构。key:value
3，字典的取值，是通过key去取这个value
任何地方的字符串都要加 引号 " "

"""
# a = {"name":"张三",0:"哈哈","age":"25"}
# # 取值
# print(a["name"])
# # 新增
# a["height"] = "183cm"
# print(a)
# # 修改
# a["name"] = "李四"
# print(a)
#
# b = a.get("name")  # get：把值取出来(取值)
# print(b)
# b = a.pop("name")  # pop: 把值拿走（剪切）
# print(b)
# print(a)
# a.update(name=1111)  # update: 可以新增，可以修改（新增或修改）
# print(a)
#
# print("--------------")
# print(a.get("name"))
# print(a["name"])
"""
# 代码正常情况下，这两种方法结果一样
"""
#
#  # 数组和字典的删除
# del a["name"]
# print(a)
#
# del a[0]
# print(a)

"""
a = {}
b = input("请输入您的姓名：")
c = input("请输入您的年龄：")
d = input("请输入您的性别：")
a.update(name=b)
a.update(age=c)
a.update(sex=d)
print("个人信息为：",a)
"""

a = {}
b = input("请输入您的姓名：")
c = input("请输入您的年龄：")
d = input("请输入您的性别：")
a["name"] = b
a["age"] = c
a["sex"] = d
print("您的个人信息为：",a)










