name = input()

command = input()

while command != "Sign up":
    command = command.split(" ")
    if command[0] == "Case":
        if command[1]== "lower":
            name = name.lower()
        elif command[1]== "upper":
            name = name.upper()
        print(name)
    elif command[0] == "Reverse":
        start = int(command[1])
        end = int(command[2])
        if start in range(0,len(name)+1) and end in range(0,len(name)+1):
            print("".join(reversed(name[start:end+1])))
    elif command[0] == "Cut":
        substring = command[1]
        if substring in name:
            for letter in substring:
                name = name.replace(letter,"",1)
            print(name)
        else:
            print(f"The word {name} doesn't contain {substring}.")
    elif command[0] == "Replace":
        replacement = command[1]
        name = name.replace(replacement,"*")
        print(name)
    elif command[0] == "Check":
        char = command[1]
        if  char in name:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    command = input()