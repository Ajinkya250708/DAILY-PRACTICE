from datetime import date

def calculate_age():
    print("Enter your birth date:")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    birthday = date(year, month, day)
    today = date.today()

    years = today.year - birthday.year
    months = today.month - birthday.month
    days = today.day - birthday.day

    if days < 0:
        months -= 1
        if today.month == 1:
            previous_month = 12
            previous_year = today.year - 1
        else:
            previous_month = today.month - 1
            previous_year = today.year

        if previous_month == 12:
            days_in_previous_month = 31
        else:
            days_in_previous_month = (date(previous_year, previous_month + 1, 1) - date(previous_year, previous_month, 1)).days

        days += days_in_previous_month

    if months < 0:
        years -= 1
        months += 12

    total_days_alive = (today - birthday).days

    print(f"\nYou are {years} years, {months} months, and {days} days old.")
    print(f"That's a total of {total_days_alive} days since you were born!")

calculate_age()