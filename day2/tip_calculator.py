
# intro and inputs
print("Welcome to the tip calculator!")
bill = float(input('what was the total bill amount?'))
tip = int(input('what was the tip percentage?'))
split = int(input('how many people are splitting the bill?'))

# calculations
tip_percentage = tip / 100
tip_amount = bill * tip_percentage
# results
total_amount = round(bill + tip_amount, 2)
split_amount = round(total_amount / split, 2)

print(f"\nTotal bill amount: ${total_amount}")
if split > 1:
    print(f"{split} people is paying ${split_amount} each.")




