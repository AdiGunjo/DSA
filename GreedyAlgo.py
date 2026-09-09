def activity_selection(activities):
    # activities: list of (start, end) tuples
    activities.sort(key=lambda a: a[1])  # sort by finish time
    selected = [activities[0]]

    for start, end in activities[1:]:
        if start >= selected[-1][1]:
            selected.append((start, end))

    return selected

acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print("Selected activities:", activity_selection(acts))