# import time
# import random
# import pymysql

# # for i in range(10):
# #     time.sleep(1)
# #     print(i)

# # a = random.randint(100,1000)
# # print(a)


# """
# class 声明类的名字
# 然后类的名字的首字母必须大写
# 面向对象编程
# 类里面所有的方法，都必须传一个参数，叫self
# """

class GirlFriend ():
    """
        女朋友
    """
    def __init__(self,sex,high,weight,hair,age): #初始化
        self.sex = sex
        self.high = high 
        self.weight = weight
        self.hair = hair
        self.age = age
    
    def caiyi(self,num):
        """
            才艺表演
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的"+self.sex+"朋友开始了自己的才艺表演之：")
        if num == 1:
            print("胸口碎大石！")
        elif num == 2:
            print("唱跳rap篮球")
        else:
            print("单手开瓶盖!")

    def chuyi(self):
        """
        厨艺持家
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的"+self.sex+"朋友开始了自己的厨艺表演之：")
        print("精通八大菜系！啥都会做")

    def work(self):
        """
        工作赚钱
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的"+self.sex+"朋友开始了自己的工作表演之：")
        print("开挖掘机")



#  类的实例化
limeng = GirlFriend("男","190cm","90kg","锡纸烫","29")

limeng.caiyi(2)
limeng.work()
print(limeng.sex)


class Car(object):
    def __init__(self,brand,yanse,neishi,jilun):
        self.brand = brand
        self.yanse = yanse
        self.neishi = neishi
        self.jilun = jilun

    def bianxing(self):
        print("车子变身为金刚")

    def fly(self):
        print("车子要起飞！")

zhangsan = Car("奔驰","大红","豪华","独轮车")
zhangsan.bianxing()

class Nvpengyou(GirlFriend):
    def work(self):
        print("修电脑！")

object #祖宗类
zhangsan=Nvpengyou("女","160cm","60kg","卷发","19")
zhangsan.work()

#  GirlFriend: 父类
#  Nvpengyou: 子类

