
marks = []

for i in range(5):
    mark = int(input("Enter subject mark: "))
    marks.append(mark)

valid = True

for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid marks")
else:
    total = sum(marks)
    percentage = total / 5

    print("Total marks:", total)
    print("Percentage:", percentage)

    if min(marks) < 35:
        print("Result: Fail")
    else:
        print("Result: Pass")

        if percentage >= 90:
            print("Grade: A")
        elif percentage >= 75:
            print("Grade: B")
        elif percentage >= 60:
            print("Grade: C")
        else:
            print("Grade: D")
