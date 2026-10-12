print("Hello I am the magic area guide but i can only do squares or rectangles")



def areaOfSquare(side):
    area = side ** 2
    return area

def areaOfRectangle(width,height):
    area = width * height
    return area

while True:
    ans1 = input("Are you looking to find the area of a square or rectangle? ").lower()
    if ans1 in ["square", "rectangle"]:
        break
    else:
        print("type in either square or rectangle")

if ans1 == "square":
    len1 = int(input("what is the length of 1 side of your square in cm?: "))
    print("your square has an area of", areaOfSquare(len1), "cm squared")

else:
    wid1 = float(input("what is the width of your rectangle in cm: "))
    height1 = float(input("what is the height of your rectangle in cm: "))
    print("your rectangle has an area of", areaOfRectangle(wid1, height1), "cm squared")