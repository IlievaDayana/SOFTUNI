file = open("even_lines.txt")
punctuation = ["-", ",", ".", "!", "?","'"]
with open("output.txt", "w") as f:
    for index, line in enumerate(file):
        index +=1
        count_symbols = 0
        punct = 0
        line = line.strip("\n")
        for symbol in line:
            if symbol in punctuation:
                punct += 1
            elif symbol != " " and symbol != "\n":
                count_symbols += 1
        f.write(f"Line{index}: {line} ({count_symbols})({punct})\n")
