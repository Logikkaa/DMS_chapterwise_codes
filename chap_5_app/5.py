def schedule_talks(talks):
    talks.sort(key=lambda x: x[1])  # Sort by end times
    n = len(talks)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = max(talks[i - 1][2] + dp[j] for j in range(i) if talks[j][1] <= talks[i - 1][0])

    max_attendance = dp[n]
    selected_talks = []

    while n > 0:
        if dp[n] != dp[n - 1]:
            selected_talks.append(talks[n - 1])
            n -= 1
        else:
            n -= 1

    return max_attendance, selected_talks

talks = [(1, 3, 5), (2, 4, 3), (3, 5, 7), (4, 6, 2)]
max_attendance, selected_talks = schedule_talks(talks)
print(f"Max Total Attendance: {max_attendance}")
print("Selected Talks:")
for talk in selected_talks:
    print(f"Start: {talk[0]}, End: {talk[1]}, Attendees: {talk[2]}")
