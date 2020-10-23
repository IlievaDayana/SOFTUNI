import re

emojis = r"([*]{2}|[:]{2})([A-Z]{1}[a-z]{2,})\1"
numbers = r"[0-9]"

raw = input()
threshold = 0

numbers_match = re.findall(numbers,raw)
for index, num in enumerate(numbers_match):
    if num:
        if index == 0:
            threshold+= int(num)
        else:
            threshold*=int(num)

cool_emojis = []
total = 0
matches = re.finditer(emojis,raw)
for match in matches:
    if match:
        value = 0
        a = re.compile(r"([*]{2}|[:]{2})([A-Z]{1}[a-z]{2,})\1")
        b = a.match(match[0])
        name = b.group(2)
        total += 1
        for letter in name:
            value += ord(letter)
        if value >= threshold:
            cool_emojis.append(match[0])


print(f"Cool threshold: {threshold}")
print(f"{total} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)

