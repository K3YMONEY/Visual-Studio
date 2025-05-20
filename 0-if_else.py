#program to determine the type of triangle
angle1 = int(input('enter angle 1: ' ))
angle2 = int(input('enter angle 2: '))
angle3 = int(input('enter angle 3: '))

if angle1 + angle2 + angle3 == 180:
    if angle1 == angle2 == angle3:
        print('equilateral')
    elif angle1 != angle2 != angle3:
        print('scalene')
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print('isosceles')
else: 
     if angle1 + angle2 + angle3 != 180:
        print('not a triangle')






