# ## ==========/////////--- IT'S CALCULATOR ----/////////===============

principle = 0
rate = 0
time = 0

while True" ":
    # while principle <= 0:
    principle =float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero!")
    else:
        break

# while rate <= 0:
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero!")
    else:
        break
# while time <= 0:
while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero!")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")


# for i in range(1, 11):
#     print(i)