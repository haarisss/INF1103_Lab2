inventory = 0
failed_entries = 0

while (user_input := input("Enter stock quantity (or type 'quit' to exit): ")) != "quit":
    if not user_input.lstrip('-').isdigit():
        print("Error: Invalid input. Please enter a valid number.")
        failed_entries += 1
        continue

    elif int(user_input) < 0:
        print("Error: Quantity cannot be negative.")
        failed_entries += 1
        continue
    
    else:
        quantity = int(user_input)
        inventory += quantity

        if inventory > 500:
            print("Overstock alert! Inventory exceeds 500 units.")
            break
    

print(f"Total Units Processed: {inventory}.")
print(f"Number of Failed/Rejected Entries: {failed_entries}.")