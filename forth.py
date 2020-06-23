# for i in range(10):
#     if i==4:
#         continue
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         if i==4:
#             break
#         print(i,"X",j,"=",i*j,end="   ")
#     print()

"""  函数
自动的判断账号长度5--8位，密码8--12位，并且账号必须以小写开头
"""

# def checkname(username):
#     if len(username) >=5 and len(username) <=8:
#         if username[0] in "qazwsxedcrfvtgbyhnujmikopl":
#             print("OK")
#         else:
#             print("账号的首字母必须小写字母开头！")
#     else:
#         print("账号的长度不符合规范，请输入5-8位的账号")

# def  方法/函数的声明
# checkname  方法/函数的名字
#usernsme  方法/函数的参数
# """ 方法的说明 """
#  方法/函数的逻辑代码
# a="7nfkdn"
# checkname(a)

# print()
# checkname()

# def jiafa(a,b):
"""
    这个方法的作用是实现两个数字相加
"""
#     if type(a) is int and type(b) is int:
#         print(a+b) # return a+b
#     else:
#         print("请输入整数")  # return "请输入整数"

# # print(jiafa(9,100))

# try:                  # 异常捕获
#     print(2+ihji1)
# except Exception as e:   # 异常捕获
#     print("上面的代码错了",e)


a = input("请输入你的名字：")
b = input("请输入你的年龄：")
try:

    if int(b)>18:
        print(a,"成年了")
    else:
        print(a,"未成年")
except:
    print("请输入正确的年龄")

#处理用户输入的数据







