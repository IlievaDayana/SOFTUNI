heroes = {}

command = input()

while command != "End":
    action = command.split(" ")
    if action[0]=="Enroll":
        hero_name = action[1]
        if hero_name not in heroes.keys():
            heroes[hero_name]=[]
        else:
            print(f"{hero_name} is already enrolled.")
    elif action[0] =="Learn":
        hero_name = action[1]
        spell_name = action[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)
    elif action[0] =="Unlearn":
        hero_name = action[1]
        spell_name = action[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)
    command = input()
sorted_heroes =dict(sorted(heroes.items(),key=lambda a:(-len(a[1]),a[0])))
print("Heroes: ")
for k,v in sorted_heroes.items():
    v = ", ".join(v)
    print(f"== {k}: {v}")
