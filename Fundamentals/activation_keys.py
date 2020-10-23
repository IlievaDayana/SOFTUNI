raw = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        if substring in raw:
            print(f"{raw} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        upper_lower = command[1]
        start = int(command[2])
        stop = int(command[3])
        if upper_lower == "Upper":
            new = []
            for index in range(0,len(raw)):
                if index in range(start,stop):
                    new.append(raw[index].upper())
                else:
                    new.append(raw[index])
        elif upper_lower == "Lower":
            new = []
            for index in range(0, len(raw)):
                if index in range(start, stop):
                    new.append(raw[index].lower())
                else:
                    new.append(raw[index])
        raw = "".join(new)
        print("".join(raw))
    elif action == "Slice":
        start = int(command[1])
        stop = int(command[2])
        new = []
        for i in range(0,len(raw)):
            if not i in range(start,stop):
                new.append(raw[i])
        raw = "".join(new)
        print(raw)

    command = input()
print(f"Your activation key is: {raw}")
