print("Hello i am the rectangle area checker please input the length and width of your rectangle")

wid1 = float(input("what is the width of your rectangle in cm: "))
height1 = float(input("what is the height of your rectangle in cm: "))

def areaOfRectangle(width,height):
    area = width * height
    return area

print("your rectangle has an area of", areaOfRectangle(wid1, height1), "cm squared")