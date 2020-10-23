from collections import deque

levels = {
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
    150: "Doll"
}
crafted = {
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0,
    "Bicycle": 0,

}

materials = [int(i) for i in input().split(" ")]
magics = deque([int(j) for j in input().split(" ")])
holiday_on = False

while materials and magics:
    material = materials[-1]
    magic = magics[0]
    result = material * magic
    if magic == 0:
        magics.popleft()
        continue
    if material == 0:
        materials.pop()
        continue
    if result in levels.keys():
        item = levels[result]
        crafted[item] += 1
        materials.pop()
        magics.popleft()
    elif result < 0:
        result = material + magic
        materials.pop()
        magics.popleft()
        materials.append(result)
    elif result > 0:
        magics.popleft()
        materials[-1] += 15
    if crafted["Doll"] >= 1 and crafted["Wooden train"] >= 1 or crafted["Teddy bear"] >= 1 and crafted["Bicycle"] >= 1:
        holiday_on = True


if holiday_on:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print("Materials left:", ", ".join(map(str, materials)))
if magics:
    print("Magic left:", ", ".join(map(str, magics)))
