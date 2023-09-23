def point_in_polygon(point, polygon):
    x, y = point
    odd_nodes = False
    j = len(polygon) - 1

    for i in range(len(polygon)):
        if (polygon[i][1] < y and polygon[j][1] >= y) or (polygon[j][1] < y and polygon[i][1] >= y):
            if polygon[i][0] + (y - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) * (polygon[j][0] - polygon[i][0]) < x:
                odd_nodes = not odd_nodes
        j = i

    return odd_nodes

# Define the polygon as a list of (x, y) vertices
polygon = [(1, 1), (1, 4), (4, 4), (4, 1)]

# Test points
point_inside = (2, 3)
point_outside = (5, 2)

print("Point inside polygon:", point_in_polygon(point_inside, polygon))
print("Point outside polygon:", point_in_polygon(point_outside, polygon))
