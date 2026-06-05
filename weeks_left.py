def life_in_weeks(age):
    life_left = 90 - age
    weeks_left = life_left * 52
    print(f"You have {weeks_left} weeks left")

age = int(input("What is your age? "))
life_in_weeks(age)