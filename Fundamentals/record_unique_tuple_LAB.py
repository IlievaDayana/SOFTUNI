def unique_names(count_times):
    names = set()
    for _ in range(count_times):
        names.add(input())
    print("\n".join(names))


unique_names(int(input()))