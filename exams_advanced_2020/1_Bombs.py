from collections import deque

effects = deque(map(int, input().split(", ")))
casings = list(map(int, input().split(", ")))

bombs = {40: "Datura Bombs",
         60: "Cherry Bombs",
         120: "Smoke Decoy Bombs", }

pouch = {"Datura Bombs": 0,
         "Cherry Bombs": 0,
         "Smoke Decoy Bombs": 0, }
success = False
while effects and casings:
    effect = effects[0]
    casing = casings[-1]
    result = effect + casing
    if result in bombs.keys():
        name_of_bomb = bombs[result]
        pouch[name_of_bomb] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] = casing - 5
    if pouch["Datura Bombs"] >= 3 and pouch["Cherry Bombs"] >= 3 and pouch["Smoke Decoy Bombs"] >= 3:
        success = True
        break

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print("Bomb Effects:", ", ".join(map(str, effects)))
else:
    print("Bomb Effects: empty")

if casings:
    print("Bomb Casings:", ", ".join(map(str, casings)))
else:
    print("Bomb Casings: empty")
ordered_bombs = dict(sorted(pouch.items(), key=lambda a: a[0]))
[print(f"{k}: {v}") for k, v in ordered_bombs.items()]
