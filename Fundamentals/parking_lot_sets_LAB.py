def cars(number):
    parking_lot= set()
    for num in range(number):
        (command,registration) = input().split(", ")
        if command == "IN":
            parking_lot.add(registration)
        else:
            parking_lot.remove(registration)
    return parking_lot


lot = "\n".join(cars(int(input())))
if lot:
    print(lot)
else:
    print('Parking Lot is Empty')