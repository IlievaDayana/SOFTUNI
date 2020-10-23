size = int(input())
field = [[i for i in input().split()] for x in range(size)]


def start(field):
    for i in range(size):
        for x in range(size):
            if field[i][x] == "B":
                return i, x


def results(key, field, r, c):
    result = 0
    coordinates = []
    if key == "up" and r - 1 in range(len(field)):
        for i in range(r - 1, 0 - 1, -1):
            if field[i][c] != "X":
                coordinates.append([i, c])
                result += int(field[i][c])
            else:
                break
        return result, coordinates
    elif key == "down" and r + 1 in range(len(field)):
        for i in range(r + 1, len(field)):
            if field[i][c] != "X":
                coordinates.append([i, c])

                result += int(field[i][c])
            else:
                break
        return result, coordinates
    elif key == "left" and c - 1 in range(len(field)):
        for i in range(c - 1, 0 - 1, -1):
            if field[r][i] != "X":
                coordinates.append([r, i])
                result += int(field[r][i])
            else:
                break
        return result, coordinates
    elif key == "right" and c + 1 in range(len(field)):
        for i in range(c + 1, len(field)):
            if field[r][i] != "X":
                coordinates.append([r, i])
                result += int(field[r][i])
            else:
                break
        return result, coordinates
    else:
        return None


r, c = start(field)

a = {"up": results("up", field, r, c), "down": results("down", field, r, c), "left": results("left", field, r, c),
     "right": results("right", field, r, c)}
best_path = None
best_result = -9999999999999
best_coordinates = []
for k, v in a.items():
    if v:
        value, coordinates = v
        if value > best_result:
            best_result = value
            best_path = k
            best_coordinates = coordinates
print(best_path)
[print(i) for i in best_coordinates]
print(best_result)
