def frame_stewart(n, k, source, target, auxiliary1, auxiliary2):
    if n == 0:
        return
    if n == 1:
        print(f"Move disk {k} from {source} to {target}")
        return
    frame_stewart(n-2, k, source, auxiliary1, auxiliary2, target)
    print(f"Move disk {k+n-1} from {source} to {auxiliary2}")
    print(f"Move disk {k+n-2} from {source} to {target}")
    print(f"Move disk {k+n-1} from {auxiliary2} to {target}")
    frame_stewart(n-2, k, auxiliary1, target, source, auxiliary2)

n = 4  # Number of disks
k = 1  # Disk numbering starts at k
frame_stewart(n, k, 'A', 'D', 'B', 'C')
