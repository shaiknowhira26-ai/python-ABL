
distance = float(input("Enter distance in km: "))
mileage1 = float(input("Enter Vehicle 1 mileage: "))
mileage2 = float(input("Enter Vehicle 2 mileage: "))
fuel_price = float(input("Enter fuel price per litre: "))

if distance <= 0 or mileage1 <= 0 or mileage2 <= 0 or fuel_price < 0:
    print("Invalid input")
else:
    fuel1 = distance / mileage1
    fuel2 = distance / mileage2

    cost1 = fuel1 * fuel_price
    cost2 = fuel2 * fuel_price

    print("Vehicle 1 fuel:", round(fuel1, 2), "litres")
    print("Vehicle 1 cost: Rs.", round(cost1, 2))
    print("Vehicle 2 fuel:", round(fuel2, 2), "litres")
    print("Vehicle 2 cost: Rs.", round(cost2, 2))

    if cost1 < cost2:
        print("Vehicle 1 is cheaper")
    elif cost2 < cost1:
        print("Vehicle 2 is cheaper")
    else:
        print("Both vehicles have equal cost")
