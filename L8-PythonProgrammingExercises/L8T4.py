import math
print("Hello I am the magic area program i can now do squares, rectangles AND CIRCLES ")

def areaOfSquare(side):
    # side squared
    area = side ** 2
    return area

def areaOfRectangle(width,height):
    # width x height = area2
    area = width * height
    return area


def circleInfo(type1, value):
    # turn whatever we were given into a radius
    if type1 == "radius":
        radius = value
    elif type1 == "diameter":
        radius = value / 2
    elif type1 == "circumference":
        radius = value / (2 * math.pi)

    # work out everything else from the radius
    diameter = radius * 2
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    return radius, diameter, circumference, area

while True:
    ans1 = input("Please input which shape you are trying to find the area for (square, rectangle or circle) ").lower()
    if ans1 in ["square", "rectangle", "circle"]:
        break
    else:
        print("type in either square, rectangle or circle")

if ans1 == "square":
    len1 = int(input("what is the length of 1 side of your square in cm?: "))
    print("your square has an area of", areaOfSquare(len1), "cm squared")

elif ans1 == "rectangle":
    wid1 = float(input("what is the width of your rectangle in cm: "))
    height1 = float(input("what is the height of your rectangle in cm: "))
    print("your rectangle has an area of", areaOfRectangle(wid1, height1), "cm squared")

elif ans1 == "circle":
    type1 = None

    if input("do you know the radius? (yes/no) ").lower() == "yes":
        type1 = "radius"
    elif input("do you know the diameter? (yes/no) ").lower() == "yes":
        type1 = "diameter"
    elif input("do you know the circumference? (yes/no) ").lower() == "yes":
        type1 = "circumference"

    if type1 is None:
        print("sorry, I need the radius, diameter or circumference to work out the area")
    else:
        value = float(input("enter the " + type1 + " in cm: "))
        radius, diameter, circumference, area = circleInfo(type1, value)
        print("with a", type1, "of", value, "cm:")
        print("radius:", round(radius, 2), "cm")
        print("diameter:", round(diameter, 2), "cm")
        print("circumference:", round(circumference, 2), "cm")
        print("area:", round(area, 2), "cm squared")