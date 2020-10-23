import re

string = input()

calories_per_day = 2000
pattern = r"(\||#)([\w\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1"
total_calories = 0
matches = re.findall(pattern, string)

for match in matches:
    if match and int(match[3])<=10000:
        item_name = match[1]
        expiration_date = match[2]
        calories = int(match[3])
        total_calories += calories
        print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

days = total_calories // calories_per_day
print(f"You have food to last you for: {days} days!")