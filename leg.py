import math

base = int(input("Please input a base of the right triangle: "))
hype = int(input("Please input the hypotenuse of the right triangle: "))

base = base**2
hype = hype**2

output = int(((hype-base)**(1/2)))


print(str(output))