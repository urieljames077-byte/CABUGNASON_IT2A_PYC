from menu import menu, display_menu


def get_order():
    orders = []

    while True:
        display_menu()

        while True:
            item = input("\nEnter menu item: ").strip().title()

            if item in menu:
                break
            else:
                print("Invalid item. Please choose from the menu.")

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        price = menu[item]
        item_total = price * quantity

        order = {
            "item": item,
            "quantity": quantity,
            "price": price,
            "total": item_total
        }

        orders.append(order)

        print(f"\nAdded: {quantity} x {item} = ₱{item_total:.2f}")

        while True:
            another = input(
                "\nDo you want to order another item? (yes/no): "
            ).strip().lower()

            if another == "yes" or another == "no":
                break
            else:
                print("Please enter yes or no.")

        if another == "no":
            break

    return orders


def calculate_total(orders):
    grand_total = 0

    for order in orders:
        grand_total += order["total"]

    return grand_total


def calculate_discount(grand_total):
    if grand_total >= 500:
        discount = grand_total * 0.10
    else:
        discount = 0

    return discount