import re

pattern = r"([#|$|%|*|&]+)(?P<racername>[A-z]+)\1[=]{1}(?P<lengeohash>[0-9]+)[!]{2}(?P<geocode>[\S]+)$"


while True:
    string = input()
    p = re.compile(pattern)
    if p:
        r = p.search(string)
        if r:
            name = r.group("racername")
            length = r.group("lengeohash")
            geocode=r.group("geocode")
            new = []
            if int(length) == len(geocode):
                for letter in  geocode:
                    new.append(chr(int(length)+ord(letter)))
                new = "".join(new)
                print(f"Coordinates found! {name} -> {new}")
                break
            else:
                print("Nothing found!")
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")
