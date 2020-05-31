# 判断
# a = 1
# b = 2
# if a==1:
#     print("a=1")
# if a > b:
#     print("a比b大")
# else:
#     print("b更大")

# age = int(input("请输入你的年龄："))
# if age>60:
#     print("你应该退休了")
# elif age>30:
#     print("家庭的责任很重吧")
# elif age>20:
#     print("一定要好好规划你的未来！")
# else:
#     print("读书的时候，要认真！")
   
# if age > 20 and age <=30:
#     print("一定要好好规划你的未来！")
# elif age > 30:
#     print("家庭的责任很重吧")
# elif age > 60:
#     print("你应该退休了")
# else:
#     print("读书的时候，要认真！")


# a = "你好"
# if a in "你好，今天你好帅！": #用来判断a是否在后面条件的里面
#     print("OK")
# else:
#     print("不OK")

# a = input("请输入：")
# if a=="":
#     print("不能为空!")
#     exit()
# if a in "0123456789":
#     a=int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()

# if a>5:
#     print("大")
# else:
#     print("小")

# a = 10
# if type(a) is int: # is可以用来判断类型是啥
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# a = 1
# while a<10:
#     print("哈哈哈",a)
#     a=a+2

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

# 遍历

# a = "你好，今天你吃了么？"
# a = ["张三","李四","王麻子","二狗","流云","西西","朗杰","小亮","李白","杜甫"]
# for i in a:  # 在 a 中读出来的每一个字，赋值给 i  (i就是遍历对象的每一个值)
#     print(i)  #在打印i的时候，就是把a 中每一个字打印出来

# b = list(range(0,100,4))  #自动生成了一个数列,步进/步长
# print(b)

# for i in range(100):
#     print(i)

# for i in range(10):
#     print(i)

a = ["张三","李四","王麻子","二狗","流云","西西","朗杰","小亮","李白","杜甫"]
for i in a:
    print(i,end="||")
    print("--------")

    #练习1：
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
