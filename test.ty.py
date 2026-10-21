# print('HELLO WORLD')
# name = '小名'
# age = 18
# height = 60
# print(name)
# print(age)
# print(height)
# print(name+str(age)+str(height))
# a=8
# b=7
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# msg = '第一段文字'
# print(msg)
# msg = '修改后的文字'
# print(msg)
# msg = 999
# print(msg)
# name = input('请输入姓名：')
# age = int(input('请输入年龄：'))
# print(f'你叫{name},明年{age+1}岁')



#if elif 函数
# score = int(input('请输入成绩：'))
# if 100>=score >= 90:
#     print('成绩好')
# elif 60<= score <90:
#     print('成绩良好')
# elif 0<= score <60:
#     print('差')
# else :
#     print('成绩无效')



#  while 函数
# i = 1
# while i <= 100:
#     print('hello world')
#     i += 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
#     # print(s)
# print(s)


#  while 嵌套
# i = 1
# while i <= 3:
#     print(f'第{i}次外循环')
#     j = 1
#     while j <= 5:
#         print(f'第{j}次内循环')
#         j += 1
#     i += 1


#  for 函数
# s = 0
# for i in range(1,101):
#     s += i
    # print(s)
# print(s)

#  break
# i = 1
# while i <= 6:
#     print(f'吃了{i}个苹果')
#     if i == 4:
#         print(f'吃到了{i}个，吃到了虫子不吃了')
#         break
#     i += 1

#
# li = [1,2,3]
# print(li,type(li))
# print(li[0:2])
# for i in li:
#     print(i)



# li = ['one','two','three']
# li.append('four')
# li.extend('four')
# li.insert(0,'four')
# print(li)



# li = ['one','two','three']
# li[2] = 'four'
# print(li)



# li = [1,2,3,4,5]
# print(2 in li)
# print(3 not in li)


#   append在列表中增加元素li.append(元素）
# li = ['小明','小红','小智']
# while True:
#     name = input('请输入姓名')
#     if name in li :
#         print(f'你输入的{name}已被使用')
#     else:
#         print(f'{name}输入成功')
#         li.append(name)
#         print(li)
#         break

#   删除列表  del li or del li[下标]删除列表 pop删除元素li.pop(下标）   remove(指定元素）li.remove('')
# li = ['小明','小红','小智']
# del li
# del li[2]
# print(li)

# li.pop(0)
# print(li)

# li.remove('小红')
# print(li)


#  排序sort正序排列     reverse倒叙整体排列
# li = [1,46,98,3,5,76]
# li.sort()
# li.reverse()
# print(li)

# for i in range(11):
# #     print(i)

# li = input('请输入字符串：')
# num = 0
# for s in li:
#     if s.isdigit():
#         num += 1
# print(num)



# week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
# first = input('请输入第一个字母').upper()
# match  = [day for day in week if first in day]
# if len(match) == 1:
#     print(match[0])
# elif len(match) > 1:
#     send = input('请输入第二个字母').lower()
#     for day in match:
#         if day[1] == send:
#             print(day)
#             break
# else:
#     print('没有匹配的星期')



import copy
li = [1,2,3,[4,5,6,]]
li2 = copy.copy(li)
print('li',li)
print('li2',li2)
print('li 内存地址',id(li))
print('li2内存地址',id(li2))





























































