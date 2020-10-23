n = int(input())
heroes = {}
for num in range(0,n):
    v = input().split(" ")
    heroes[v[0]]=[int(v[1]),int(v[2])]
command = input()
while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        spell_name = command[3]
        hero_name = command[1]
        mana_needed = int(command[2])
        if heroes[hero_name][1]>=mana_needed:
            heroes[hero_name][1]-=mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name][0]-=damage
        if heroes[hero_name][0] >0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if heroes[hero_name][1]+amount>=200:
            print(f"{hero_name} recharged for {200-heroes[hero_name][1]} MP!")
            heroes[hero_name][1] = 200
        else:
            heroes[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if heroes[hero_name][0]+amount>=100:
            print(f"{hero_name} healed for {100-heroes[hero_name][0]} HP!")
            heroes[hero_name][0]=100
        else:
            heroes[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
    command = input()
sorted_heroes = dict(sorted(heroes.items(),key=lambda a: (-a[1][0],a[0])))
for k,v in sorted_heroes.items():
    print(k)
    print(f"  HP: {v[0]}\n  MP: {v[1]}")