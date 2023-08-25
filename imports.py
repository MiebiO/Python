import random
import os
import shapes

number = random.randint(0,10)

base = random.randint(1,10)
height = random.randint(1,10)

area = shapes.area_of_triangle(base,height)

print(base, height, area)