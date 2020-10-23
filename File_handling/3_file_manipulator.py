import os
while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    action = command[0]
    file_name = command[1]
    if action == "Create":
        file = open(file_name,"w")
        file.close()
    elif action == "Add":
        content = command[2]
        file = open(file_name,"a")
        file.write(content+"\n")
        file.close()
    elif action == "Replace":
        try:
            open(file_name)
        except FileNotFoundError:
            print("An error occurred")
        else:
            with open(file_name, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace(command[2], command[3])
            with open(file_name, 'w') as file:
                file.write(filedata)
    elif action == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")


