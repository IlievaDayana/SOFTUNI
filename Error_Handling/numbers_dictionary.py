numbers_dictionary = {}

line = str(input())
n = None
while line != "Search":
    if line == "Search":
        while True:
            searched_item = str(input())
            if searched_item == "Remove":
                while True:
                    item_to_remove = str(input())
                    if item_to_remove == "End":
                        print(numbers_dictionary)
                        break
                    try:
                        numbers_dictionary.pop(item_to_remove)
                    except KeyError:
                        print("Number does not exist in directory")  # Removing non-existing number

                break
            try:
                print(numbers_dictionary[searched_item])
            except KeyError:
                print("Number does not exist in directory")  # Searching for non-existing number
        break
    try:
        numbers_dictionary[line] = int(input())
    except ValueError:
        print("The variable number must be an integer")  # Passing non_integer type
    line = input()
