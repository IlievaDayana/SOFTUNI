preferences = {}
dislikes = 0
command = input()

while command != "Stop":
    command = command.split("-")
    guest = command[1]
    meal = command[2]
    if command[0]=="Like":
        if guest not in preferences.keys():
            preferences[guest] = [meal]
        elif guest in preferences.keys() and meal not in preferences[guest]:
            preferences[guest].append(meal)
    elif command[0]=="Unlike":
        if guest not in preferences.keys():
            print(f"{guest} is not at the party.")
        elif  meal not in preferences[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif meal in preferences[guest]:
            dislikes+=1
            preferences[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
    command = input()
sorted_preferences = dict(sorted(preferences.items(),key=lambda a:(-len(a[1]),a[0])))

for k,v in sorted_preferences.items():
    preferred_meals = ", ".join(v)
    print(f"{k}: {preferred_meals}")
print(f"Unliked meals: {dislikes}")