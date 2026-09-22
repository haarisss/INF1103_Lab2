def get_valid_input():
    """Prompts for input. Returns a valid int quantity, or the string 'quit'."""
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    if user_input == "quit":
        return "quit"

    if not user_input.lstrip('-').isdigit():
        return None  # signals invalid input

    if int(user_input) < 0:
        return None  # signals invalid input

    return int(user_input)

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

inventory = 0
failed_entries = 0

while True:
    result = get_valid_input()

    if result == "quit":
        break

    if result is None:
        print("Error: Invalid input. Please enter a valid whole number ≥ 0.")
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, result)
    tax = calculate_tax(result)
    print(f"Delivery of {result} accepted. Tax on this delivery: {tax:.2f}")

    if inventory > 500:
        print("Overstock alert! Inventory exceeds 500 units.")
        break

generate_report(inventory, failed_entries)