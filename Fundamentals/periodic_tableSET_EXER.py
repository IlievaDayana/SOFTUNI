def unique_chemicals(number):
    chemicals = set()
    for i in range(number):
        a = input().split(" ")
        for ch in a:
            chemicals.add(ch)
    print("\n".join(chemicals))


unique_chemicals(int(input()))