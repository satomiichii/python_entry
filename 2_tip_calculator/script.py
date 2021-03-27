print('Welcome to the Tip Calculator!')

total_bill = int(input('What was the total bill? \n'))
tip_rate = int(input('What percentage tip whould you give? 10, 12, or 15? \n'))
num_people = int(input('How many people to split the bill?\n'))

split_amount = total_bill * (100 + tip_rate) / 100 / num_people
rounded_amount = round(split_amount,2)

print(f"Each person should pay: ${rounded_amount}")