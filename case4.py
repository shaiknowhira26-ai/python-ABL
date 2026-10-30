
units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 200 + (units - 100) * 3
    else:
        bill = 500 + (units - 200) * 5

    bill = bill + 50

    print("Electricity units:", units)
    print("Fixed charge: Rs. 50")
    print("Total bill: Rs.", bill)
