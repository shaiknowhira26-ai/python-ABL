
marks = []

for i in range(3):
    mark = float(input("Enter examination mark: "))
    marks.append(mark)

valid = True

for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid marks")
else:
    average = sum(marks) / len(marks)

    print("Examination marks:", marks)
    print("Average marks:", round(average, 2))

    if marks[2] > marks[0]:
        print("Performance: Improved")
    elif marks[2] < marks[0]:
        print("Performance: Declined")
    else:
        print("Performance: Unchanged")
