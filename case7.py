
total = 0
valid = True

for i in range(3):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        valid = False
    else:
        cost = price * quantity
        total += cost
        print("Product cost: Rs.", cost)

if not valid:
    print("Invalid input; bill not generated")
else:
    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Subtotal: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final bill: Rs.", final_bill)
