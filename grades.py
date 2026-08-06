def grades():
    n = int(input("Enter number of subjects: "))
    subjects = []
    total = 0

    for i in range(n):
        name = input(f"Enter name of subject {i+1}: ")
        marks = float(input(f"Enter marks for {name} (out of 100): "))
        subjects.append({"name": name, "marks": marks})
        total += marks

    avg = total / n

    if avg >= 90:
        g = "A+"
    elif avg >= 80:
        g = "A"
    elif avg >= 70:
        g = "B"
    elif avg >= 60:
        g = "C"
    elif avg >= 50:
        g = "D"
    else:
        g = "F"

    print("\n===== RESULT =====")
    for sub in subjects:
        print(f"{sub['name']}: {sub['marks']}")
    print("\nTotal Marks:", "total")
    print(f"Average: {avg:.2f}")
    print("Grade:", {g})

    if g == "F":
        print("Status: FAIL")
    else:
        print("Status: PASS")

grades()