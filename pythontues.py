days = [0, 1, 2, 3, 4, 5, 6]
day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
dict(zip([0, 1, 2, 3, 4, 5 ,6], ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Wednesday"]))

days_of_week = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

day = int(input('Day (0-6) '))

print(days_of_week[day])