
attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid input")
else:
    percentage = attended / total * 100
    print("Attendance percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Eligible")
    else:
        extra = 0
        while (attended + extra) / (total + extra) < 0.75:
            extra += 1

        print("Status: Not eligible yet")
        print("Additional classes required:", extra)
