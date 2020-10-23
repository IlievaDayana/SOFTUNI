from collections import deque

males = [int(i) for i in input().split(" ")]
females = deque([int(i) for i in input().split(" ")])
success = 0
while females and males:
    current_female = females[0]
    current_male = males[-1]
    if current_male <= 0:
        males.pop()
    elif current_female <= 0:
        females.popleft()

    if current_female == current_male:
        males.pop()
        females.popleft()
        success += 1
    else:
        females.popleft()
        males[-1] = current_male - 2
    if current_female % 25 == 0:
        females.popleft()
    if current_male % 25 == 0:
        males.pop()


print(f"Matches: {success}")
if males:
    print("Males left:", ", ".join(map(str, males)))
else:
    print("Males left: none")
if females:
    print("Females left:",", ".join(map(str,females)))
else:
    print("Females left: none")
