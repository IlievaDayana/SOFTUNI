n = int(input())
plants = {}
plant_rating = {}
for num in range(0,n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    if plant not in plants.keys():
        plants[plant]= [rarity]
    elif plant in plants.keys():
        plants.update({plant:[rarity]})

command = input()

while command != "Exhibition":
    if ": " in command:
        command = command.split(": ")
        if command[0]=="Rate":
            if " - " in command[1]:
                action = command[1].split(" - ")
                plant=action[0]
                rating=int(action[1])
                if plant not in plant_rating.keys():
                    plant_rating[plant]=[rating]
                else:
                    plant_rating[plant].append(rating)
            else:
                print("error")
        elif command[0]=="Update":
            if " - " in command[1]:
                action = command[1].split(" - ")
                plant=action[0]
                new_rarity=int(action[1])
                plants.update({plant: [new_rarity]})
            else:
                print("error")
        elif command[0]=="Reset":
            if command[1]:
                plant = command[1]
                plant_rating[plant]=[0]
            else:
                print("error")
        else:
            print("error")
    else:
        print("error")

    command = input()
for k,v in plants.items():
    if k in plant_rating.keys() and len(plant_rating[k])>0:
        average = sum(plant_rating[k])/len(plant_rating[k])
        plants[k].append(average)
    else:
        plants[k].append(v)

sorted_plants = dict(sorted(plants.items(),key=lambda a: (-a[1][0],-a[1][1])))
print("Plants for the exhibition:")
for key,value in sorted_plants.items():
    print(f"- {key}; Rarity: {sorted_plants[key][0]}; Rating: {sorted_plants[key][1]:.2f}")