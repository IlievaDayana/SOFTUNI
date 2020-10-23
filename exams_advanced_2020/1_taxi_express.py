from collections import deque

customers = deque([int(i) for i in input().split(", ")])
taxis = deque([int(j) for j in input().split(", ")])
total_time = 0
while customers:
    customer = customers.popleft()
    taxi = taxis.pop()
    if customer < taxi:
        total_time += customer
        taxis.appendleft(taxi)
    else:
        customers.appendleft(customer)
    if customers and not taxis:
        print("Not all customers were driven to their destinations")
        print(f"Customers left:", ", ".join(map(str, customers)))
        break

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
