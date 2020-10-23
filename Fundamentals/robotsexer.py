from collections import deque


def clock(h, m, s):
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    return h, m, s


robots = deque([i.split("-") for i in input().split(";")])
prep_time = {}
for x in robots:
    prep_time[x[0]] = int(x[1])
start_time = list(map(int, input().split(":")))
hh = start_time[0]
mm = start_time[1]
ss = start_time[2]
products = deque()

while True:
    command = input()
    if command == "End":
        break
    products.append(command)
occupied_robots = deque()

while products:
    hh, mm, ss = clock(hh, mm, ss)
    current_product = products.popleft()
    for robot in occupied_robots:
        name = robot[0]
        robot[1] = int(robot[1]) - 1
        if robot[1] <= 0:
            robots.append([name, prep_time[name]])
    occupied_robots = [x for x in occupied_robots if int(x[1]) > 0]

    if robots:
        robot_taken = robots.popleft()
        occupied_robots.append(robot_taken)
        print(f"{robot_taken[0]} - {current_product} [{hh:02d}:{mm:02d}:{ss:02d}]")
    else:
        products.append(current_product)
