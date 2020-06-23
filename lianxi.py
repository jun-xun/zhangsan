"""
练习：通过代码获取两段内容，并且计算他们的长度的和
"""
# a=input("请输入：")
# b=input("请输入：")
# print("两串字符串长度和为：",len(a)+len(b))

"""
第二次练习答案：
获取用户输入的个人信息，并且储存到字典中。
个人信息包括了，name,age,sex.
"""
# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# sex = input("请输入你的性别：")
# userinfor = {}
# # userinfor.update(name=name,age=age,sex=sex)
# userinfor["name"] = name
# userinfor["age"] = age
# userinfor["sex"] = sex
# print(userinfor)


"""
练习：
现在有10个学生的成绩，需要录入到系统中
这10个人中分别是：张三，李四，王麻子，二狗，流云，西西，朗杰，小亮，李白，杜甫
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
# highgrade={}  #定义了一个空字典，用来储存大于60的信息
# lowgrade={}  #定义了一个空字典，用来储存小于60的信息
# studentlist = ["张三","李四","王麻子","二狗","流云","西西","朗杰","小亮","李白","杜甫"]
# a=0  # 定义了一个变量，用来控制数组下标的变化
# while a<len(studentlist):  #因为所有人的信息的录入，都是要用input，所以写了循环，len判断了数组的长度，总长度-1就是最大的下标
#     grade =int(input("请输入"+studentlist[a]+"的成绩："))  #录入信息，为了方便判断，所以转换了格式
#     if grade>=60:
#         highgrade[studentlist[a]]=grade  #存到字典中，
#     else:
#         lowgrade[studentlist[a]]=grade
#     a=a+1  #控制下标变化，每一次循环，都+1
# print("大于60的人数：",highgrade)
# print("小于60的人数",lowgrade)

# 方法2
"""
练习：
现在有10个学生的成绩，需要录入到系统中
这10个人中分别是：张三，李四，王麻子，二狗，流云，西西，朗杰，小亮，李白，杜甫
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
# highgrade={}  #定义了一个空字典，用来储存大于60的信息
# lowgrade={}  #定义了一个空字典，用来储存小于60的信息
# studentlist = ["张三","李四","王麻子","二狗","流云","西西","朗杰","小亮","李白","杜甫"]

# for i in studentlist:  #因为所有人的信息的录入，都是要用input，所以写了循环，len判断了数组的长度，总长度-1就是最大的下标
#     grade =int(input("请输入"+i+"的成绩："))  #录入信息，为了方便判断，所以转换了格式
#     if grade>=60:
#         highgrade[i]=grade  #存到字典中，
#     else:
#         lowgrade[i]=grade
  
# print("大于60的人数：",highgrade)
# print("小于60的人数",lowgrade)

"""
练习：打印九九乘法表
"""

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end="  ")  #如果在print中有end的话，就不会换行，每一行就会以end=的值结束
#     print()  # 换行

"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意，红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。用户输入账号和密码，要求账号长度5--8位，密码8--12位，并且账号必须以小写开头。
储存到字典中，{username,password}
"""
 #练习1：
 ######方法1
# f=1
# while f==1:
#     a=30
#     b=35
#     c=3
#     while a>=1:
#         print("红灯还有",a,"秒结束")
#         a=a-1
#     while b>=1:
#         print("绿灯还有",b,"秒结束")
#         b=b-1
#     while c>=1:
#         print("黄灯还有",c,"秒结束")
#         c=c-1
######方法2
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")
# 练习2：


# username=input("请输入你的账号：")
# password=input("请输入你的密码：")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#         if len(password)>=8 and len(password)<=12:
#             print("注册成功",{username,password})
#         else:
#             print("密码的长度不符合规范，请输入8-12位的密码")
#     else:
#         print("请输入小写开头的账号！")
# else:
#     print("账号的长度不符合规范，请输入5-8位的账号")
   
        

# username = input("请输入账号：")
# password = input("请输入密码：")
# if len(username) >=5 and len(username) <=8:
#     if username[0] in "qazwsxedcrfvtgbyhnujmikopl":
#         if len(password) >= 8 and len(password) <= 12:
#             print("注册成功！",{username:password})
#         else:
#             print("密码必须8-12位！")
#     else:
#         print("账号的首字母必须小写字母开头！")
# else:
#     print("账号的长度不符合规范，请输入5-8位的账号")


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="   ")
#     print()

"""
练习：
定义一个方法，用来判断用户输入的账号密码是否符合规范
"""

def checkname(username,password):
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
            if len(password)>=8 and len(password)<=12:
               return True
            else:
                return "密码的长度不符合规范，请输入8-12位的密码"
        else:
            return "请输入小写开头的账号！"
    else:
        return "账号的长度不符合规范，请输入5-8位的账号"


checkname("zhangsa","123456789")




