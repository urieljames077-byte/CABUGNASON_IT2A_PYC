from ordering import get_order, calculate_total, calculate_discount
from receipt import print_receipt


def main():
    print("========================================")
    print("       WELCOME TO CABUGNASON FAST FOOD")
    print("========================================")

    while True:
        start_order = input(
            "\nDo you want to place an order? (yes/no): "
        ).strip().lower()

        if start_order == "yes" or start_order == "no":
            break
        else:
            print("Please enter yes or no.")

    if start_order == "no":
        print("\nThank you! Have a nice day!")
        return

    orders = get_order()

    subtotal = calculate_total(orders)

    discount = calculate_discount(subtotal)

    total = subtotal - discount

    print_receipt(orders, subtotal, discount, total)


if __name__ == "__main__":
    main()