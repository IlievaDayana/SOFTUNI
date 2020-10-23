number_cars = int(input())
garage = {}
for c in range(0,number_cars):
    car = input().split("|")
    garage[car[0]]=[int(car[1]),int(car[2])]
command = input()
while command != "Stop":
    com = command.split(" : ")
    if com[0] == "Drive":
        car = com[1]
        distance = int(com[2])
        fuel = int(com[3])
        mileage = garage[car][0]
        fuel_in_tank = garage[car][1]
        if fuel_in_tank >=fuel:
            garage[car][1]-=fuel
            garage[car][0]+=distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if garage[car][0]>=100000:
            del garage[car]
            print(f"Time to sell the {car}!")
    elif com[0] == "Refuel":
        car = com[1]
        fuel = int(com[2])
        fuel_in_tank = garage[car][1]
        if fuel_in_tank + fuel > 75:
            garage[car][1] = 75
            print(f"{car} refueled with {fuel+fuel_in_tank-75} liters")
        elif fuel_in_tank+fuel <= 75:
            garage[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif com[0] == "Revert":
        car = com[1]
        km = int(com[2])
        if garage[car][0]-km < 10000:
            garage[car][0]=10000
        else:
            garage[car][0] -= km
            print(f"{car} mileage decreased by {km} kilometers")
    command = input()
sorted_garage = dict(sorted(garage.items(),key=lambda a:(-a[1][0],a[0])))
for k,v in sorted_garage.items():
    print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")