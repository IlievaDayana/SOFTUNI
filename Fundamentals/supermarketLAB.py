from collections import deque

customers = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(customers)} people remaining.")
        break
    elif command == "Paid":
        for customer in range(len(customers)):
            paid_cus = customers.popleft()
            print(paid_cus)
    else:
        customers.append(command)