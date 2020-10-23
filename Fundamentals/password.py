import re

pattern = r"([@|*]{1})([A-Z]{1}[a-z]{2,})\1\:{1} {1}\[([A-Za-z]{1})\]\|{1}\[([A-Za-z]{1})\]\|{1}\[([A-Za-z]{1})\]\|{1}$"

num = int(input())
for n in range(0,num):
    string = input()
    p = re.compile(pattern)
    if p:
        r = p.search(string)
        if r:
            action = r.group(2)
            a = r.group(3)
            b=r.group(4)
            c=r.group(5)
            print(f"{action}: {ord(a)} {ord(b)} {ord(c)}")
        else:
            print("Valid message not found!")
