string = input()

command = input()

while command != "Done":
    command = command.split(" ")
    if command[0] == "TakeOdd":
        new_string = []
        for index,letter in enumerate(string):
            if index%2!=0:
                new_string.append(letter)
        string="".join(new_string)
        print(string)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        string = [i for i in string]
        string[index:index+length]=""
        string = "".join(string)
        print(string)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in string:
            string = "".join(string).replace(substring,substitute)
            print(string)
        else:
            print("Nothing to replace!")


    command = input()
print(f"Your password is: {string}")