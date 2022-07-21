
# from random import randint
import random

#声明函数
def guess(start, end, maxTime):
    value = random.randint(start, end)

    for i in range(maxTime):
        prompt = "开始猜吧，请输入一个整数，" if i == 0 else "再猜一次"

        try:
            guessNum = int(input(prompt))
            if guessNum == value:
                print("恭喜你,猜对了!")
                break
            elif guessNum > value:
                print("你猜大了!")
            else:
                print("你猜小了!")
        except:
            print("请输入整数!")
    else:
        print("很遗憾,游戏结束!")
        print("正确答案是:",value,"再接再励哦~")

#调用函数
guess(1,100,5)