def print_receipt(orders, subtotal, discount, total):
    print("\n\n==========================================")
    print("          CABUGNASON FAST FOOD")
    print("            OFFICIAL RECEIPT")
    print("==========================================")

    print(f"{'ITEM':<15}{'QTY':>5}{'PRICE':>10}{'TOTAL':>12}")
    print("------------------------------------------")

    for order in orders:
        print(
            f"{order['item']:<15}"
            f"{order['quantity']:>5}"
            f"₱{order['price']:>9.2f}"
            f"₱{order['total']:>11.2f}"
        )

    print("------------------------------------------")
    print(f"{'SUBTOTAL':<30}₱{subtotal:>10.2f}")
    print(f"{'DISCOUNT':<30}₱{discount:>10.2f}")
    print(f"{'TOTAL':<30}₱{total:>10.2f}")
    print("==========================================")
    print("        THANK YOU FOR ORDERING!")
    print("          PLEASE COME AGAIN!")
    print("==========================================")