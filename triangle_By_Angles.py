"""
 Triangular By Angles
 By: M.Yekmaz
 Date: 1400/07/10
"""

x=int(input("Please enter first angle: "))
y=int(input("Please enter second angle: "))
z=int(input("Please enter third angle: "))

if x+y+z==180:
    if x==60 and y==60 and z==60:
        type="equilateral"
    elif x==y or y==z or z==x:
        type="isoceles"
    elif x<90 and y<90 and z<90:
        type="acute"
    elif x==90 or y==90 or z==90:
        type="right"
    else:
        type="obtuse"
    print(f"These 3 angles can make a {type} triangle")
else:
    print("These 3 angles can`t make a triangle")
