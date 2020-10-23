num = int(input())

stations = []
for n in range(0,num):
    info = input().split(" ")
    stations.append(int(info[0])-int(info[1]))
current = 0
position = 0
for i,station in enumerate(stations):
    current +=station
    if current < 0:
        current = 0
        position = i + 1
print(position)