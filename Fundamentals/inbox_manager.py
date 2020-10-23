statistics = {}

command = input()

while command != "Statistics":
    command = command.split("->")
    if command[0] == "Add":
        user = command[1]
        if user not in statistics.keys():
            statistics[user]=[]
        else:
            print(f"{user} is already registered")
    elif command[0] == "Send":
        user = command[1]
        email = command[2]
        statistics[user].append(email)
    elif command[0] == "Delete":
        user = command[1]
        if user in statistics.keys():
            del statistics[user]
        else:
            print(f"{user} not found!")
    command = input()
print(f"Users count: {len(statistics)}")
sorted_info = dict(sorted(statistics.items(),key=lambda a:(-len(a[1]),a[0])))
for k, v in sorted_info.items():
    print(k)
    for mail in v:
        print(f" - {mail}")
