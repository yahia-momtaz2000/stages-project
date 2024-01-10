# Calculate Perimeter and Area of the circle
# Area = PI * r ^ 2
# Perimeter = 2 * PI * r
import math

radius = 7

perimeter = 2 * math.pi * radius
area = math.pi * math.pow( radius, 2)
print('Perimeter of the circle = '+str(perimeter))
print('area of the circle = '+ str(area))