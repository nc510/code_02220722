#计算圆的面积
import math

def computer_area_of_circle(r):
    return round(math.pi * r * r,2)

print(computer_area_of_circle(2))
print(computer_area_of_circle(3.15))
print(computer_area_of_circle(2.8))
print(computer_area_of_circle(6.78))