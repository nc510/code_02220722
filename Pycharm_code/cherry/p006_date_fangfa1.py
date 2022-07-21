print("请输入年月日，判断这个日期是这一年的第多少天")
year = int(input("请输入年份："))
# print(type(year))
# x = year + 1
# print(x)
month = int(input("请输入月份："))
day = int(input("请输入日："))

import datetime
date1 = datetime.date(year, month, day)
date2 = datetime.date(year - 1,12,31)
tianshu = (date1 - date2).days
print(tianshu)

