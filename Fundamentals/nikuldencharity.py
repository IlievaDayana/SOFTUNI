text = input()

command = input()

while command != "Finish":
    command = command.split(" ")
    if command[0] == "Replace":
        current = command[1]
        new = command[2]
        text = text.replace(current,new)
        print(text)
    elif command[0]=="Cut":
        start = int(command[1])
        end = int(command[2])
        if start not in range(0,len(text)) or end not in range(0,len(text)):
            print("Invalid indexes!")
        else:
            new =[i for i in text]
            for i in range(start,end+1):
                new.remove(text[i])
            text = "".join(new)
            print(text)
    elif command[0]=="Make":
        up_low = command[1]
        if up_low == "Upper":
            text = text.upper()
        elif up_low == "Lower":
            text = text.lower()
        print(text)
    elif command[0]=="Check":
        check = command[1]
        if check in text:
            print(f"Message contains {check}")
        elif check not in text:
            print(f"Message doesn't contain {check}")
    elif command[0]=="Sum":
        start = int(command[1])
        end = int(command[2])
        if start not in range(0,len(text)) or end not in range(0,len(text)):
            print("Invalid indexes!")
        else:
            substring = text[start:end+1]
            total = 0
            for letter in substring:
                total += ord(letter)
            print(total)

    command = input()