def frame_conjecture(n, k):
    return 2 ** k - 1 >= n

n_disks_verify = 20
for k in range(1, n_disks_verify + 1):
    if frame_conjecture(n_disks_verify, k):
        print(f"For n = {n_disks_verify}, optimal k = {k}")
        break
