file = open("even_lines.txt")
symbols = ["-", ",", ".", "!", "?"]
for index,line in enumerate(file):
    line =line.lstrip(" ")
    line = line.rstrip("\n")
    if index%2 == 0:
        for symbol in symbols:
            line = line.replace(symbol,"@")
        print(" ".join(reversed(line.split(" "))))
