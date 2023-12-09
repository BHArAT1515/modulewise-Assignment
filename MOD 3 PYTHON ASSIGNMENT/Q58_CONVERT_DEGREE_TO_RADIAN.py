import math

def degree_to_radian(degrees):
    radians = math.radians(degrees)
    return radians

# Example usage:
degree_value = 45
radian_value = degree_to_radian(degree_value)
print(f"{degree_value} degrees is equal to {radian_value} radians.")
