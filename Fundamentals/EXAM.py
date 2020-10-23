string = input()

command = input()

while command != "Travel":
    command = command.split(" ")
    if command[0]=="Add":
        actions = command[1].split(":")
        index = int(actions[1])
        a =actions[2]
        if index in range(0,len(string)):
            string=[i for i in string]
            string.insert(index,a)
            string = "".join(string)
            print(string)
    elif command[0]=="Remove":
        actions = command[1].split(":")
        start = int(actions[1])
        stop = int(actions[2])
        if start in range(0,len(string)) and stop in range(0,len(string)):
            string = [i for i in string]
            string[start:stop+1] = ""
            string = "".join(string)
            print(string)
    elif "Switch" in command[0]:
        action = command[0].split(":")
        old = action[1]
        new = action[2]
        if old in string:
            string = string.replace(old,new)
            print(string)
    command = input()
print(f"Ready for world tour! Planned stops: {string}")