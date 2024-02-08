#Anthony Lozbin
#This program allows the user to enter the number of sides of a polygon and the length of each side, then calculates the perimeter and area.

class Polygon:
    def __init__(self):
        self.__num_sides = 0
        self.__length_sides = 0.0

    def get_num_sides(self):
        return self.__num_sides

    def get_length_sides(self):
        return self.__length_sides

    def set_num_sides(self, num_sides):
        self.__num_sides = num_sides

    def set_length_sides(self, length_sides):
        self.__length_sides = length_sides

    def perimeter(self):
        num_sides = self.get_num_sides()
        length_sides = self.get_length_sides()
        perimeter = num_sides * length_sides
        return perimeter

    def area(self):
        import math
        num_sides = self.get_num_sides()
        length_sides = self.get_length_sides()
        area = (num_sides * (length_sides ** 2)) / (4 * (math.tan(math.pi / num_sides)))
        return area

def main():
    polygon = Polygon()
    
    num_sides = int(input('Enter the number of sides (>= 3): '))
    if num_sides >= 3:
        polygon.set_num_sides(num_sides)
    else:
        while num_sides < 3:
            num_sides = int(input('Invalid entry. Re-enter the number of sides (>= 3): '))

    length_sides = float(input('Enter the length of each of the sides (>= 0.1): '))
    if length_sides >= 0.1:
        polygon.set_length_sides(length_sides)
    else:
        while length_sides < 0.1:
            length_sides = float(input('Invalid entry. Re-enter the length of each of the sides (>= 0.1): '))

    print(f'The polygon has {polygon.get_num_sides()} sides. Each side is {polygon.get_length_sides()} units in length.')
    print(f'The perimeter of the polygon is {polygon.perimeter():.3f} units and its area is {polygon.area():.3f} square units.')

main()
