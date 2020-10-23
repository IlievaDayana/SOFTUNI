import os

os.chdir(os.getcwd())
cwd = os.getcwd()
l = [f for f in os.listdir(cwd) if os.path.isfile(f)]
l2 = []
for value in l:
    s = value.split('.')[1]
    l2.append(s)
with open("C:/Users/USER/Desktop/report.txt", "w") as f:
    for x in sorted(set(l2)):
        f.write(f".{x}\n")
        for y in sorted(l):
            a = y.split(".")
            if a[1] == x:
                f.write(f"- - - {y}\n")
