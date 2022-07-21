
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

num1 = int(input("请输入第一个数字： "))
num2 = int(input("请输入第二个数字： "))
print("输入运算：1，加法;2，减法;3，乘法;4，除法： ")
choice= input("请输入你的选择：(1/2/3/4):")

if choice == "1":
    print(num1 ,"+",num2,"=",add(num1,num2))
elif choice == "2":
    print(num1 ,"-",num2,"=",subtract(num1,num2))
elif choice == "3":
    print(num1 ,"*",num2,"=",multiply(num1,num2))
elif choice == "4":
    print(num1 ,"/",num2,"=",divide(num1,num2))
else:
    print("非法输入!请重新输入")