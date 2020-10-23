def count_numbers(numbers):
    count_list = {}
    for num in numbers:
        if num not in count_list:
            count_list[num] = 0
        count_list[num] += 1
    return count_list


def print_info(info):
    for (key, value) in info.items():
        print(f"{key} - {value} times")


items = count_numbers(float(a) for a in input().split(" "))
print_info(items)