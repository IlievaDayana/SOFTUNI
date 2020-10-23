map = {}

command = input()

while command != "Sail":
    command = command.split("||")
    name = command[0]
    population = int(command[1])
    gold = int(command[2])
    if name not in map.keys():
        map[name]=[population,gold]
    elif name in map.keys():
        map[name][0]+= population
        map[name][1]+= gold
    command = input()

new_command = input()

while new_command != "End":
    action = new_command.split("=>")
    if action[0] == "Plunder":
        town = action[1]
        people = int(action[2])
        gold = int(action[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        map[town][0]-=people
        map[town][1]-=gold
        if map[town][0] <=0 or map[town][1]<=0:
            del map[town]
            print(f"{town} has been wiped off the map!")
    elif action[0] == "Prosper":
        town = action[1]
        gold = int(action[2])
        if gold<0:
            print("Gold added cannot be a negative number!")
        elif gold>0:
            map[town][1]+=gold
            print(f"{gold} gold added to the city treasury. {town} now has {map[town][1]} gold.")
    new_command = input()
if map:
    maps_sorted = dict(sorted(map.items(),key=lambda a: (-a[1][1],a[0])))
    print(f"Ahoy, Captain! There are {len(map)} wealthy settlements to go to:")
    for k,v in maps_sorted.items():
        print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")