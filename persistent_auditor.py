def load_inventory():
    try:
        file = open("inventory.txt", "r")
    except FileNotFoundError:
        return 0, []
 
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    file.close()
 
    total = int(first_line) if first_line else 0
    history = [int(x) for x in second_line.split(",")] if second_line else []
    return total, history
 
 
def save_inventory(total, history):
    file = open("inventory.txt", "w")
    file.write(str(total) + "\n")
    file.write(",".join(str(x) for x in history) + "\n")
    file.close()
 
 
def get_valid_input():
    """Prompts for input. Returns a valid int quantity, 'quit', or None if invalid."""
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
 
    if user_input.lower() == "quit":
        return "quit"
 
    try:
        value = int(user_input)
    except ValueError:
        return None
 
    return value if value >= 0 else None
 
 
def process_delivery(current_total, new_value):
    """Adds new_value to current_total and returns the new total."""
    return current_total + new_value
 
 
def calculate_tax(amount):
    """Returns 10% tax on the given delivery amount."""
    return amount * 0.10
 
 
def generate_report(total_units, failed_attempts):
    """Prints the final summary."""
    print(f"Total Deliveries Processed: {total_units}.")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}.")
 
 
inventory, history = load_inventory()
failed_entries = 0
 
while True:
    result = get_valid_input()
 
    if result == "quit":
        break
 
    if result is None:
        print("Error: Invalid input. Please enter a valid whole number >= 0.")
        failed_entries += 1
        continue
 
    inventory = process_delivery(inventory, result)
    history.append(result)
    tax = calculate_tax(result)
    print(f"Delivery of {result} accepted. Tax on this delivery: {tax:.2f}")
 
    if inventory > 500:
        print("Overstock alert! Inventory exceeds 500 units.")
        break
 
save_inventory(inventory, history)
generate_report(inventory, failed_entries)