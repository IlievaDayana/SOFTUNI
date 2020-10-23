data = {}
results = {}
while True:
    com = input()
    if com == "end of contests":
        break
    comm = com.split(":")
    contestant = comm[0]
    password = comm[1]
    if contestant not in data.items():
        data[contestant]=password
while True:
    command = input()
    if command == "end of submissions":
        break
    a = command.split("=>")
    contest = a[0]
    passw = a[1]
    username = a[2]
    points = int(a[3])
    if contest in data.keys():
        if data[contest] == passw:
            if username not in results.keys():
                results[username]={contest:points}
            else:
                if contest in results[username]:
                    if results[username][contest]>results[username][contest]:
                        results[username][contest]=points
                else:
                    results[username][contest]=points

name_best = max(results)
best_result = sum(results[name_best].values())
print(f"Best candidate is {name_best} with total {best_result} points.\nRanking:")
results = dict(sorted(results.items(),key=lambda a: a[0]))
for k,v in results.items():
    print(k)
    value = dict(sorted(v.items(),key=lambda a:(-a[1],a[0])))
    for key,value in value.items():
        print(f"#  {key} -> {value}")