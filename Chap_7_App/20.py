import itertools

def assign_frequencies(stations_distances, min_distance):
    n = len(stations_distances)
    frequencies = {}
    
    for i in range(n):
        frequencies[i] = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if stations_distances[i][j] >= min_distance:
                frequencies[i].append(j)
                frequencies[j].append(i)
                
    colors = [-1] * n
    
    def is_safe(station, color):
        for neighbor in frequencies[station]:
            if colors[neighbor] == color:
                return False
        return True
    
    def color_stations(station):
        for color in range(n):
            if is_safe(station, color):
                return color
        return -1
    
    for station in range(n):
        colors[station] = color_stations(station)
        
    return colors

# Example input: List of distances and minimum allowable distance
stations_distances = [
    [0, 4, 6, 8],
    [4, 0, 5, 9],
    [6, 5, 0, 3],
    [8, 9, 3, 0]
]
min_distance = 5

coloring = assign_frequencies(stations_distances, min_distance)
print("Coloring of Stations:", coloring)
