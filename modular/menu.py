menu = {
    "Burger": 50.00,
    "Fries": 35.00,
    "Chicken": 85.00,
    "Spaghetti": 65.00,
    "Coke": 25.00
}


def display_menu():
    print("\n========================================")
    print("          CABUGNASON FAST FOOD")
    print("========================================")
    print(f"{'ITEM':<20}{'PRICE':>10}")
    print("----------------------------------------")

    for item, price in menu.items():
        print(f"{item:<20}₱{price:>8.2f}")

    print("========================================")