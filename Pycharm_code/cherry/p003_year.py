#如果year%4==0 并且 year % 100 ==0 或者 year % 400 ==0：是闰年，否则 不是闰年
year = int(input("请输一个傻的："))
if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
