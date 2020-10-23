array = [27, 19, 42, 2, 13, 45, 48]
bigger =[]
for i in range(0,len(array)):
    number = array[i]
    is_bigger = False
    if len(array) == i+1:
        bigger.append(number)
        break
    for j in range(i+1,len(array)):
        next_number = array[j]
        if array[j]<number:
            is_bigger = True
        else:
            is_bigger = False
            break

    if is_bigger:
        bigger.append(number)
print(bigger)