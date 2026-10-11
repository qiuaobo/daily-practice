#      购物小票
# udisk_price = input("U盘价格")
# udisk_num = input("U盘数量")
# gtf_price = input("F卡价格")
# gtf_num = input("F卡数量")
# card_reader_price = input("读卡器价格")
# card_reader_num = input("读卡器数量")
# net_cable_price = input("网线的价格")
# net_cable_num = input("网线的数量")
# name = ('U盘','F卡','读卡器','网线')
# print('-'*40)
# print('单号:DH202311010001')
# print('时间: 2023-11-01 20: 56: 15')
# print('-'*40)
# print('名称    数量   单价    金额')
# print("U盘 ",udisk_num,udisk_price,int(udisk_num)*int(udisk_price),sep="     ")
# print("F卡 ",gtf_num,gtf_price,int(gtf_num)*int(gtf_price),sep="     ")
# print("读卡器",card_reader_num,card_reader_price,int(card_reader_num)*int(card_reader_price),sep="    ")
# print("网线", net_cable_num,net_cable_price,int(net_cable_num)*int(net_cable_price),sep="     ")
# print('-'*40)
# total_price = udisk_price+gtf_price+card_reader_price+net_cable_price
# total_num = udisk_num+gtf_num+card_reader_num+net_cable_num
# print('总数:',total_num,        '总额:',total_price,sep='    ')
# print('-'*40)
# print('实收:',total_price,      '找零：0.00',sep='    ')
# print('-'*40)
# print('收银：管理员')
# print('-'*40)




#   植物证书

# name = input('请输入名字')
# plant = input('请输入植物名称')
# print('植物证书\t')
# print('-'*50)
# print(name  ,'谢谢你：')
# print("你申请的",plant,"将由伊利公益基金会负责种下。查看种植进程>")
# print('树苗编号：NO.HBI66308960305')
# print('申请时间：2023年11月10日')
# print('种植地点：鄂尔多斯')
# print('-'*50)

# BMI计算
# height = float(input('请输入身高（m)'))
# weight = float(input('请输入体重（kg)'))
# BMI = weight / height / height
# if BMI < 18.5:
#     print('偏瘦')
# elif 23.9 >= BMI >= 18.5:
#     print('正常')
# elif 27.9 >= BMI >= 24.0:
#     print('超重')
# elif BMI >= 28 :
#     print('肥胖')
# else:
#     print('错误')



# 算时间间隔
# start_time = int(input("请输入起始时间小时数："))
# start_minute = int(input("请输入起始时间分钟数："))
# end_hour = int(input("请输入结束时间小时数："))
# end_minute = int(input("请输入结束时间分钟数："))
#
# start_total_minutes = start_time * 40 + start_minute
# end_total_minutes = end_hour * 40 + end_minute
# duration_minutes = end_total_minutes - start_total_minutes
# hour = duration_minutes // 60
# minute = duration_minutes % 60
# print('时间间隔为',hour,'小时',minute,'分钟')


# a = 3.14
# r = float(input('请输入半径：'))
# s = a * r ** 2
# length = a * r * 2
# print('面积：',s)
# print('周长',length)



# total = 29.5
# time_1 = 3
# a = 4
# b = 2.5
# total_end = total - 3 * a
# time_2 = total_end / b
# print('还需要',time_2,'次才能运输完')



# import random
# num = random.randint(0,100)
# while True:
#     a = int(input('请输入数字'))
#     if a > num:
#         print('大了，继续猜')
#     elif a < num:
#         print('小了，继续猜')
#     elif a == num:
#         print('恭喜你，踩到数字炸弹了')
#         break



con = input('请输入国家')
year = input('请输入年份')
month= input('请输入月份')
day = input('请输入日期')
hour = input('请输入小时')
min = input('请输入分钟')
second = input('请输入秒')
if con == '中国':
    print(f'{year}年{month}月{day}日{hour}：{min}：{second}')
elif con == '美国':
    print(f'{month}/{day}/{year}{hour}：{min}：{second}')
elif con == '英国'or'澳大利亚'or'法国':
    print(f'{day}/{month}/{year}{hour}：{min}：{second}')
elif con == '德国'or'俄罗斯':
    print(f'{day}.{month}.{year}{hour}：{min}：{second}')
elif con == '中国':
    print(f'{year}-{month}-{day}{hour}：{min}：{second}')























































