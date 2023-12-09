def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Example usage:
base1_length = 5
base2_length = 9
height_value = 4
area_result = trapezoid_area(base1_length, base2_length, height_value)
print(f"The area of the trapezoid is: {area_result}")
