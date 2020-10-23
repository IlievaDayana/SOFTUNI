pool = {}

while True:
    command = input()
    if command == "Season end":
        break

    if " -> " in command:
        command = command.split(" -> ")
        player = command[0]
        pos = command[1]
        skill = int(command[2])
        if player not in pool.keys():
            pool[player]={pos:skill}
        elif player in pool.keys() and pos != pool[player]:
            pool[player][pos] = skill
        elif player in pool.keys() and pos == pool[player][pos] and pool[player][pos]<skill:
            pool[player][pos]=skill
    elif " vs " in command:
        command = command.split(" vs ")
        player1 = command[0]
        player2 = command[1]
        if player1 in pool.keys() and player2 in pool.keys():
            for position in pool[player1]:
                if position in pool[player2]:
                    total1=sum(pool[player1].values())
                    total2= sum(pool[player2].values())
                    if total1 > total2:
                        del pool[player2]
                    elif total2>total1:
                        del pool[player1]
players_total = {}
for player,value in pool.items():
    players_total[player]=sum(pool[player].values())

players_total = dict(sorted(players_total.items(),key = lambda a:(-a[1],a[0])))

for player,total in players_total.items():
    print(f"{player}: {total} skill")
    sorted_skills = dict(sorted(pool[player].items(),key = lambda b:(-b[1],b[0])))
    for key,value in sorted_skills.items():
        print(f"- {key} <::> {value}")
