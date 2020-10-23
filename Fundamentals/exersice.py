count_presents = int(input())
neighborhood = [input().split() for x in range(int(input()))]


def santa_position(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == "S":
                return x, y


def print_matrix(m):
    for row in m:
        print(" ".join(row), end="  \n")


def valid(field, row, col):
    if row in range(len(field)) and col in range(len(field)):
        return True
    else:
        return False


def presents(field, row, col, presents_availvable):
    coordinates_cookier = [1, -1, 0, 0]
    coordinates_cookiec = [0, 0, 1, -1]
    result = 0
    for i in range(len(coordinates_cookier)):
        r = coordinates_cookier[i] + row
        c = coordinates_cookiec[i] + col
        if valid(field, r, c) and presents_availvable > 0:
            if field[r][c] == "V" or field[r][c] == "X":
                field[r][c] = "-"
                presents_availvable -= 1
                result += 1

    return result


def nice_kids_counter(field):
    count = 0
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == "V":
                count += 1
    return count


current_row, current_col = santa_position(neighborhood)
nice_kids = nice_kids_counter(neighborhood)
nice_kids_with_presents = 0
while True:
    action = input()
    if action == "Christmas morning":
        break
    if action == "up":
        if valid(neighborhood, current_row - 1, current_col):
            neighborhood[current_row][current_col] = "-"
            current_row, current_col = current_row - 1, current_col
    elif action == "down":
        if valid(neighborhood, current_row + 1, current_col):
            neighborhood[current_row][current_col] = "-"
            current_row, current_col = current_row + 1, current_col
    elif action == "left":
        if valid(neighborhood, current_row, current_col - 1):
            neighborhood[current_row][current_col] = "-"
            current_row, current_col = current_row, current_col - 1
    elif action == "right":
        if valid(neighborhood, current_row, current_col + 1):
            neighborhood[current_row][current_col] = "-"
            current_row, current_col = current_row, current_col + 1

    if count_presents > 0:
        if neighborhood[current_row][current_col] == "V":
            neighborhood[current_row][current_col] = "S"
            nice_kids_with_presents += 1
            count_presents -= 1
        elif neighborhood[current_row][current_col] == "C":
            neighborhood[current_row][current_col] = "S"
            dropped_presents = presents(neighborhood, current_row, current_col, count_presents)
            count_presents -= dropped_presents
    if count_presents <= 0 and nice_kids_counter(neighborhood):
        print("Santa ran out of presents!")
        break
    if not nice_kids_counter(neighborhood):
        break

print_matrix(neighborhood)
nice_kids = nice_kids_counter(neighborhood)
if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
elif nice_kids > 0:
    print(f"No presents for {nice_kids} nice kid/s.")
