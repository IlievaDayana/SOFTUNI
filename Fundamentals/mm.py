bomb_plantation = []

for row in range(int(input())):
    bomb_plantation.append(list(map(int, input().split(" "))))

a = input().split(" ")
targets = []


def print_matrix(m):
    for row in m:
        print(" ".join(map(str, row)))


def explosion(r, c, plantation, y):
    rows = [-1, -1, -1, 1, 1, 1, 0, 0]
    cols = [-1, 0, 1, -1, 0, 1, -1, 1]
    for field in range(8):
        if r + rows[field] in range(len(bomb_plantation)) and c + cols[field] in range(len(bomb_plantation)):
            if plantation[r + rows[field]][c + cols[field]] > 0:
                plantation[r + rows[field]][c + cols[field]] -= y


def return_alive_cells(matrix):
    alive_list_amount = 0
    alive_sum = 0
    for one in matrix:
        alive_sum += sum(num for num in one if num > 0)
        alive_list_amount += sum(1 for num in one if num > 0)
    print(f"Alive cells: {alive_list_amount}\nSum: {alive_sum}")


for i in a:
    targets.append(list(map(int, i.split(","))))

for coordinate in targets:
    (row, column) = coordinate
    magnitut = bomb_plantation[row][column]
    if row in range(len(bomb_plantation)) and column in range(len(bomb_plantation)):
        explosion(row, column, bomb_plantation, magnitut)
        bomb_plantation[row][column] -= magnitut
return_alive_cells(bomb_plantation)
print_matrix(bomb_plantation)
