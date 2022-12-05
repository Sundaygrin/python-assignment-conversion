today = int(input("Enter today's day: "))

if today == 0:
    print("\nSunday")
elif today == 1:
    print("\nMonday")
elif today == 2:
    print("\nTuesday")
elif today == 3:
    print("\nWednesday")
elif today == 4:
    print("\nThursday")
elif today == 5:
    print("\nFriday")
elif today == 6:
    print("\nSaturday")
else:
    "invalid"

future_days = int(input("Enter future_days: "))
future_days = (today + future_days) % 7

if future_days == 0:
    print("\nSunday")
elif future_days == 1:
    print("\nMonday")
elif future_days == 2:
    print("\nTuesday")
elif future_days == 3:
    print("\nWednesday")
elif future_days == 4:
    print("\nThursday")
elif future_days == 5:
    print("\nFriday")
elif future_days == 6:
    print("\nSaturday")
else:
    "invalid"

