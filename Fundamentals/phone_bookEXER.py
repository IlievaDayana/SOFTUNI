def phones(line):
    phonebook = {}
    while True:
        if line.isalnum():
            break
        (name, phone) = line.split("-")
        phonebook[name] = phone
        line = input()
    return line,phonebook


def searches(n, book):
    for num in range(int(n)):
        name = input()
        if name in book.keys():
            print(f"{name} -> {book[name]}")
        else:
            print(f"Contact {name} does not exist.")


a = phones(input())
searches(int(a[0]),a[1])