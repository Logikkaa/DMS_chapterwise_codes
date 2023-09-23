def is_ear(vertex, prev_vertex, next_vertex, polygon):
    triangle = [prev_vertex, vertex, next_vertex]
    for point in polygon:
        if point not in triangle:
            if is_point_inside_triangle(point, triangle):
                return False
    return True

def is_point_inside_triangle(point, triangle):
    ax, ay = triangle[0]
    bx, by = triangle[1]
    cx, cy = triangle[2]
    px, py = point

    detT = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    alpha = ((by - cy) * (px - cx) + (cx - bx) * (py - cy)) / detT
    beta = ((cy - ay) * (px - cx) + (ax - cx) * (py - cy)) / detT
    gamma = 1 - alpha - beta

    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1

def ear_clipping(polygon):
    triangles = []
    while len(polygon) >= 3:
        for i, vertex in enumerate(polygon):
            prev_vertex = polygon[i - 1]
            next_vertex = polygon[(i + 1) % len(polygon)]
            if is_ear(vertex, prev_vertex, next_vertex, polygon):
                triangles.append((prev_vertex, vertex, next_vertex))
                polygon.remove(vertex)
                break
    return triangles

# Define the polygon as a list of (x, y) vertices
polygon = [(1, 1), (1, 4), (4, 4), (4, 1)]

triangles = ear_clipping(polygon)
print("Triangulated triangles:", triangles)
