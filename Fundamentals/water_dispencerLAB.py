from collections import deque

liters = int(input())
queue = deque()
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)
while True:
    command = input().split(" ")
    if command[0] == "End":
        print(f"{liters} liters left")
        break
    elif command[0] == "refill":
        lit = int(command[1])
        liters += lit
    else:
        liters_for_person = int(command[0])
        if liters_for_person <=liters:
            liters -= liters_for_person
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")