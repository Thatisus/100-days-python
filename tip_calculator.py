
print("Welcome to the tip calculator!")

total_bill = float(input("How much was the total bill?"))

tip_percent = float(input("How much would you like to tip as a percentage?")) / 100

ways_split = float(input("How many people are splitting the bill?"))

result = round((total_bill * (tip_percent + 1) / ways_split) , 2)

print(f"If splitting eqaully, each person will pay ${result}.")