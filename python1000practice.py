#day1
# Q1
# lis=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         lis.append(str(i))
#         pass
#     pass
# print(','.join(lis))
# # 简化版：
# print(*(i for i in range(2000,3201) if i%7==0 and i%5!=0),sep=",")
# Q2
# n=int(input('请输入数字：'))
# res=1
# for i in range(1,n+1):
#     res*=i
#     pass
# print(res)
# 定义函数
# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x*(x-1)
#     pass
# x=int(input())
# print(fact(x))#调用函数
# while循环
# while i<=n:
#     res=i*res
#     i=i+1
#     pass
# 又或者
# n=int(input())
# def fact(x):return 1 if x<=1 else x*fact(x-1)#递归调用
# print(fact(n))
#Q 3
# dic={}
# n=int(input())
# for i in range(1,n+1):
#     dic[i]=i**2
#     pass
# print(dic)
# # 更简单的做法1
# dic={i:i*2 for i in range(1,n+1)}#直接赋值

# day2
# Q4
#卡在了自己忘记了如何将列表强制转换成元组
# 如何分割自己输入的一大串内容
# 输入的字符串分割后自动存为列表类型
# c=input('请输入一组数字，以逗号隔开：')#输入以‘，’分隔的字符串
# l=c.split(",")#以’，‘分割输入的内容，分割的各个子部分构成列表
# t=tuple(l)#将列表强制转换成元组
# print(l)
# print(t)
# #简便
# print(tuple(input('请输入一组数字，以逗号隔开：').split(',')))
# Q5
# class Strr():
#     def __init__(self,gets):
#         self.gets=gets
#     def getString(self):
#         info=self.gets
#         pass
#     def printString(self):
#         print(self.gets)
#     pass
# strr=Strr(input('请输入：'))
# strr.getString()
# strr.printString()
# # 或者
# class Strr():
#     def __init__(self):
#         self.gets=""#定义好类型，是个字符串（声明变量）
#     def getString(self):
#         self.gets=input('请输入：')
#         pass
#     def printString(self):
#         print(self.gets.upper())
#     pass
# strr=Strr()
# strr.getString()
# strr.printString()
# 或者
# class Strr():
#     def getString(self):
#         self.gets=input('请输入：')
#         pass
#     def printString(self):
#         print(self.gets)#和print(self.gets.upper()有什么区别？
#     pass
# strr=Strr()
# strr.getString()
# strr.printString()
# /Q6
# import math
# res=[]
# def cal(x):
#     for item in x:
#         n=int(math.sqrt(100*int(item)/30))
#         res.append(n)
#         pass
#     return res
# num=input('请以逗号隔开：')
# li=num.split(',')
# print(cal(li))
# 或者
# def cal(x):
#     return math.sqrt((100*x)/30)
# x=input().split(',')
# x=[str(round(cal(int(i)))) for i in x]
# print(",".join(x))
# Q7
# import numpy
# x=int(input("请输入x："))
# y=int(input("请输入y："))
# a=numpy.zeros(shape=(x,y))#定义一个空数组，虽然看起来是一个全0数组，但由于之后要写值覆盖，所以无所谓
# for i in range(0,x):
#     for j in range(0,y):
#         a[i][j]=i*j#给矩阵中每个元素赋值
#         pass
#     pass
# print(a)
# 或者
# x,y=map(int,input().split(','))
# lis=[]#定义一个空列表
# for i in range(x):
#     tem=[]#定义一个子 空列表
#     for j in range(y):
#         tem.append(i*j)#算好每一行的值作为一个子列表
#         pass
#     lis.append(tem)#遍历完所有行之后形成总列表
#     pass
# print(lis)
# 或者
# x,y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)
# 列表当中的每个元素可以又是一个列表
# Q8
# lis=input().split(',')
# lis.sort()#即可以按数字大小排序，也可以按字母顺序进行排序
# print(lis) #按列表输出
# 或者
# print(','.join(lis))#按字符串输出
# Q9
# lst = []
# while True:#当break后，true会置为false，循环停止
#     s=input("输入")#输入完要求字符后，按回车，会再要求输入一次，此时继续按回车，那么第二次输入的字符长度为0，表示已经输入完毕，循环停止
#     if len(s)==0:
#            break
#     lst.append(s.upper())
#     pass
# for lines in lst:
#     print(lines)
# #由于字符串的两句话之间有换行，所以如何获取全部字符不遗漏第二行是关键，区分换行和输入结束
# # 最后是按换行的字符串输出，而非列表，要一行一行输出就用循环