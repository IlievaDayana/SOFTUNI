a = input()
command = input()
while command != "End":
    command = command.split(" ")

    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        a = a.replace(char,replacement)
        print(a)
    elif command[0] == "Includes":
        string = command[1]
        if string in a:
            print("True")
        else:
            print("False")
    elif command[0] == "Start":
        string = command[1]
        if a.startswith(string):
            print("True")
        else:
            print("False")
    elif command[0] == "Lowercase":
        a = a.lower()
        print(a)
    elif command[0] == "FindIndex":
        char = command[1]
        c = a.rfind(char)
        print(c)
    elif command[0] == "Remove":
        startIndex = int(command[1])
        count = int(command[2])
        b = [i for i in a]
        for index in range(startIndex,startIndex+count):
            b.remove(a[index])
        a="".join(b)
        print(a)


    command = input()