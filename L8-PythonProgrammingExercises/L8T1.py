print("Hello i am the square area checker please input 1 side of your square")

num1 = int(input("what is the side of your square in cm: "))

def areaOfSquare(side):
    area = side ** 2
    return area

print("your square has an area of", areaOfSquare(num1), "cm squared")