#Write your code below this line 👇


import math
#print(int(math.ceil(4.2)))
height =0
width = 0
coverage = 0

def paint_calc(height, width, cover):
    print(f"You'll need {int(math.ceil((float(height) * float(width)) / float(cover)))} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

