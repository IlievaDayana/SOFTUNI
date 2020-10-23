def guest_list(number):
    listed = set()
    for _ in range(number):
        listed.add(input())
    return listed


def guests_arrived(command):
    list_arrived = set()
    while True:
        if command == "END":
            break
        list_arrived.add(command)
        command = input()
    return list_arrived


def not_arrived(people_listed_in, people_arrived):
    information = people_listed_in - people_arrived
    return information


def print_information(to_sort):
    sorted_info = sorted(to_sort)
    print(len(sorted_info))
    for guest in sorted_info:
        if guest[0].isdigit:
            print(guest)
    for guest in sorted_info:
        if not guest[0].isdigit:
            print(guest)


a = guest_list(int(input()))
b = guests_arrived(input())
print_information(not_arrived(a, b))
