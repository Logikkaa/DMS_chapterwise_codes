def frame_stewart_reves(n, source, target, auxiliary1, auxiliary2):
    if n == 0:
        return
    if n == 1:
        print(f"Move disk {n} from {source} to {target}")
        return
    k = 2  # Optimal k for Reve's puzzle
    frame_stewart_reves(n-k, source, auxiliary1, auxiliary2, target)
    print(f"Move disk {n-k+1} from {source} to {auxiliary2}")
    frame_stewart_reves(n-k, auxiliary1, target, auxiliary2, source)
    print(f"Move disk {n-k+1} from {auxiliary2} to {target}")
    frame_stewart_reves(n-k, auxiliary2, source, auxiliary1, target)

n_disks_reves = 20
frame_stewart_reves(n_disks_reves, 'A', 'B', 'C', 'D')
