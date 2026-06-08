total = 0

while True:
    expense = input("Enter expense amount (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    total += float(expense)

print("\n----- Expense Summary -----")
print("Total Spent: ₹", total)

