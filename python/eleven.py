def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant 1"
    elif x < 0 and y > 0:
        return "Quadrant 2"
    elif x < 0 and y < 0:
        return "Quadrant 3"
    elif x > 0 and y < 0:
        return "Quadrant 4"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "On Y-Axis"
    else:
        return "On X-Axis"

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

result = find_quadrant(x, y)
print(f"The point ({x}, {y}) is in: {result}")
