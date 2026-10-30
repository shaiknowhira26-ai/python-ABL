
venue = float(input("Enter venue expense: "))
equipment = float(input("Enter equipment expense: "))
catering = float(input("Enter catering expense: "))
transport = float(input("Enter transport expense: "))

participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per person: "))
sponsorship = float(input("Enter sponsorship amount: "))

if (min(venue, equipment, catering, transport, fee, sponsorship) < 0
        or participants < 0):
    print("Invalid input")
else:
    expenses = venue + equipment + catering + transport
    income = participants * fee + sponsorship
    balance = income - expenses

    print("Total expenses: Rs.", expenses)
    print("Total income: Rs.", income)

    if balance >= 0:
        print("Surplus: Rs.", balance)
    else:
        print("Shortage: Rs.", -balance)
