string = input().split(" ")
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"],
                    "purple": ["blue", "red"],
                    "green": ["yellow", "blue"]}
colors_created = []
waiting_list = []


def correct_color(a, b, primary, secondary):
    if a + b in primary:
        return a + b
    elif b + a in primary:
        return b + a
    elif a + b in secondary.keys():
        return a + b
    elif b + a in secondary.keys():
        return b + a


def receive_color(a, list_to_append, primary, secondary):
    if a in primary:
        list_to_append.append(a)
    elif a in secondary.keys():
        p1, p2 = secondary[a]
        if p1 in list_to_append and p2 in list_to_append:
            list_to_append.append(a)
    return list_to_append


while string:
    if len(string) == 1:
        colors_created = receive_color(string[0], colors_created, main_colors, secondary_colors)
        break
    first = string[0]
    if len(string) > 1:
        last = string[-1]
    else:
        last = ""
    middle_index = int(len(string) / 2) - 1
    curr_col = correct_color(first, last, main_colors, secondary_colors)

    if curr_col in main_colors:
        colors_created = receive_color(curr_col, colors_created, main_colors, secondary_colors)
        string = string[1:len(string) - 1]
    elif curr_col in secondary_colors.keys():
        primary1, primary2 = secondary_colors[curr_col]
        if primary1 in colors_created and primary2 in colors_created:
            colors_created = receive_color(curr_col, colors_created, main_colors, secondary_colors)
            string = string[1:len(string) - 1]
        else:
            colors_created.append(curr_col)
            waiting_list.append(curr_col)
            string = string[1:len(string) - 1]
    else:
        string = string[1:len(string) - 1]
        first = first[0:len(first) - 1]
        last = last[0:len(last) - 1]
        if len(first) > 0:
            string.insert(middle_index, first)
        if len(last) > 0:
            string.insert(middle_index, last)

if waiting_list:
    for color in waiting_list:
        a,b = secondary_colors[color]
        if a not in colors_created or b not in colors_created:
            colors_created.remove(color)


print(colors_created)
