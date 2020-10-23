import re

n = int(input())
pattern = r"@{1}#+([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})@{1}#+"
numbers = r"[0-9]+"
for number in range(0,n):
    item = input()
    match = re.findall(pattern,item)
    number = re.findall(numbers,item)

    if match:
        if number:
            number = "".join(number)
            print(f"Product group: {number}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")

