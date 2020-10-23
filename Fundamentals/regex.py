import re
letters = r"([^0-9.\/+*-])"
digits = r"[\+|\-]?\d+[\.]?\d*"
multdivide = r"([\*|\/]+)"
splitpattern = r"[, ]+"
demons = {}
test_str = re.split(splitpattern,input())

for demon in test_str:
    lett = re.findall(letters, demon)
    digs = re.findall(digits, demon)
    divmul = re.findall(multdivide, demon)

    name = "".join([i for i in lett])

    damage = 0
    if digs:
        d = [i for i in digs]
        for digit in d:
            damage += float(digit)

    if divmul:
        for symbol in divmul:
            if symbol == "*":
                damage*=2
            elif symbol == "/":
                damage/=2

    health = 0
    for u in name:
        health += ord(u)
    demons[demon]={health:damage}

demsort= dict(sorted(demons.items()))
for demon,points in demsort.items():
    print(demon, end = "")
    for p in points:
        print(f" - {p} health, {demsort[demon][p]:.2f} damage")