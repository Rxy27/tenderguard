#输入每天可学习小时数
daily_hour = input("请输入每天可学习的小时数：")
#输入每周学习天数
week_days = input("请输入每周学习的天数：")
#计算每周总学习时间 注意需要把str类型转换为int类型
sum_hour = int(daily_hour) * int( week_days)
#使用 f-string 输出结果
print(f"每周总学习时间为：{sum_hour}h")