
capacity = 1000
level = float(input("Enter initial water level: "))

if level < 0 or level > capacity:
    print("Invalid water level")
else:
    for day in range(1, 4):
        inflow = float(input("Enter inflow for day: "))
        outflow = float(input("Enter outflow for day: "))

        if inflow < 0 or outflow < 0:
            print("Invalid inflow or outflow")
            continue

        level = level + inflow - outflow

        if level > capacity:
            print("Overflow detected")
            level = capacity
        elif level < 0:
            print("Water shortage detected")
            level = 0

        print("Day", day, "water level:", level, "litres")
