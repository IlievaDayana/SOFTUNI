count_presents = int(input())
x = int(input())
hood = []
for _ in range(x):
    hood.append([u for u in input().split(" ")])


def santa_pos(field):
    nice = 0
    row, col = 0, 0
    for q in range(len(field)):
        for w in range(len(field[q])):
            if field[q][w] == "S":
                row, col = q, w
            elif field[q][w] == "V":
                nice += 1
    return nice, row, col


total_nice_kids, curr_row, curr_col = santa_pos(hood)


def new_pos(action, r, c):
    if action == "left":
        return r, c - 1
    elif action == "right":
        return r, c + 1
    elif action == "up":
        return r - 1, c
    elif action == "down":
        return r + 1, c


def validate_move(newr, newc, field):
    if newr in range(len(field)) and newc in range(len(field)):
        return True
    else:
        return False


def cookie_on(r, c, field, presents_avlb):
    good_kid_presents = 0
    presents_given = 0
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]
    for i in range(len(x)):
        if presents_avlb:
            row = r + x[i]
            column = c + y[i]
            if presents_avlb > 0:
                if validate_move(row, column, field):
                    if field[row][column] == "V":
                        good_kid_presents += 1
                        presents_given += 1
                        presents_avlb -= 1
                    elif field[row][column] == "X":
                        presents_given += 1
                        presents_avlb -= 1
                    field[row][column] = "-"
    return presents_given, good_kid_presents, field


def matrix_printer(field):
    for row in field:
        print(" ".join(row))


nice_kids_needing_presents = total_nice_kids
while True:
    command = input()
    if command == "Christmas morning":
        break
    new_row, new_col = new_pos(command, curr_row, curr_col)
    if count_presents > 0:
        if hood[new_row][new_col] == "V":
            nice_kids_needing_presents -= 1
            hood[curr_row][curr_col] = "-"
            curr_row, curr_col = new_row, new_col
            hood[new_row][new_col] = "S"
        elif hood[new_row][new_col] == "-":
            hood[curr_row][curr_col] = "-"
            curr_row, curr_col = new_row, new_col
            hood[new_row][new_col] = "S"
        elif hood[new_row][new_col] == "X":
            hood[curr_row][curr_col] = "-"
            curr_row, curr_col = new_row, new_col
            hood[new_row][new_col] = "S"
            hood[curr_row][curr_col] = "-"
        elif hood[new_row][new_col] == "C":
            hood[new_row][new_col] = "S"
            a, b, field = cookie_on(new_row, new_col, hood, count_presents)
            hood = field
            count_presents -= a
            nice_kids_needing_presents -= b

    if count_presents <= 0 and nice_kids_needing_presents:
        print("Santa ran out of presents!")
        break

    if nice_kids_needing_presents <= 0:
        break

matrix_printer(hood)

if nice_kids_needing_presents > 0:
    print(f"No presents for {nice_kids_needing_presents} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")


###________________________________________________________________________________________________________________


def drop_presents(pos, matrix, available_presents):
    row = pos[0]
    col = pos[1]
    result = 0

    if matrix[row][col - 1] in "XV" and available_presents > 0:
        result += 1
        matrix[row][col - 1] = "-"
        available_presents -= 1

    if matrix[row][col + 1] in "XV" and available_presents > 0:
        result += 1
        matrix[row][col + 1] = "-"
        available_presents -= 1

    if matrix[row - 1][col] in "XV" and available_presents > 0:
        result += 1
        matrix[row - 1][col] = "-"
        available_presents -= 1

    if matrix[row + 1][col] in "XV" and available_presents > 0:
        result += 1
        matrix[row + 1][col] = "-"
        available_presents -= 1

    return result


def get_nice_kids(matrix):
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "V":
                result += 1
    return result


presents = int(input())
n = int(input())
santa_pos = []

matrix = []
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
total_nice_kids = 0

for row in range(n):
    line = input().split()
    for col in range(n):
        if line[col] == "S":
            santa_pos = [row, col]
        if line[col] == "V":
            total_nice_kids += 1
    matrix.append(line)

while True:
    line = input()
    if line == "Christmas morning":
        break

    dir_changes = directions[line]
    new_pos = [santa_pos[0] + dir_changes[0], santa_pos[1] + dir_changes[1]]

    if matrix[new_pos[0]][new_pos[1]] == "V":
        presents -= 1
    elif matrix[new_pos[0]][new_pos[1]] == "C":
        dropped_presents = drop_presents(new_pos, matrix, presents)
        presents -= dropped_presents

    matrix[santa_pos[0]][santa_pos[1]] = "-"
    santa_pos = new_pos
    matrix[santa_pos[0]][santa_pos[1]] = "S"

    if presents <= 0 and get_nice_kids(matrix):
        print("Santa ran out of presents!")
        break

    if not get_nice_kids(matrix):
        break

[print(" ".join(row)) for row in matrix]
nice_kids = get_nice_kids(matrix)

if nice_kids > 0:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
