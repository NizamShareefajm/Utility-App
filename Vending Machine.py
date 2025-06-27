import sys

# Define the vending machine stock
vending_stock = {
    "Drinks": {
        "Cola": 1.50,
        "Pepsi": 1.80,
        "Dr.Pepper": 2.35,
        "Beer": 5.40
    },
    "Snacks": {
        "Chips": 1.00,
        "Candy": 0.75,
        "Kitkat": 0.89,
        "Small Cake": 3.12
    },
    "Burgers": {
        "Double Smash Cheese Burger": 10.20,
        "Cheese Burger": 9.50,
        "Mac Donald Burger": 13.45
    }
}

def show_menu():
    print("\n--- VENDING MACHINE MENU ---")
    for i, category in enumerate(vending_stock.keys(), 1):
        print(f"{i}. {category}")
    print("0. Exit")

def show_category_items(category):
    print(f"\nItems in {category}:")
    for i, (item, price) in enumerate(vending_stock[category].items(), 1):
        print(f"{i}. {item} - ${price:.2f}")
    print("0. Go Back")

def process_purchase(item_name, price):
    print(f"\nSelected item: {item_name} - ${price:.2f}")
    try:
        payment = float(input("Enter your payment: $"))
    except ValueError:
        print("Invalid input. Returning to menu.")
        return

    if payment >= price:
        change = payment - price
        print(f"Purchase successful! Here is your {item_name}. Change: ${change:.2f}")
    else:
        print("Not enough payment. Transaction cancelled.")

def vending_machine_interface():
    while True:
        show_menu()
        try:
            choice = int(input("Select a category: "))
        except ValueError:
            print("Invalid input. Please choose a number.")
            continue

        if choice == 0:
            print("Thank you for using the vending machine!")
            sys.exit()

        categories = list(vending_stock.keys())
        if 1 <= choice <= len(categories):
            category = categories[choice - 1]
            while True:
                show_category_items(category)
                try:
                    item_choice = int(input("Choose an item to purchase: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                if item_choice == 0:
                    break

                items = list(vending_stock[category].items())
                if 1 <= item_choice <= len(items):
                    item_name, price = items[item_choice - 1]
                    process_purchase(item_name, price)
                else:
                    print("Invalid item choice.")
        else:
            print("Invalid category selection.")

# Start the vending machine
vending_machine_interface()
