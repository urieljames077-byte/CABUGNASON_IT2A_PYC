class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, food_item, quantity):
        self.food_item = food_item
        self.quantity = quantity

    def get_total(self):
        return self.food_item.price * self.quantity


class Restaurant:
    def __init__(self):
        self.menu = [
            FoodItem("Burger", 50.00),
            FoodItem("Fries", 35.00),
            FoodItem("Chicken", 85.00),
            FoodItem("Spaghetti", 65.00),
            FoodItem("Coke", 25.00)
        ]

        self.orders = []

    def display_menu(self):
        print("\n========================================")
        print("          CABUGNASON FAST FOOD")
        print("========================================")
        print(f"{'ITEM':<20}{'PRICE':>10}")
        print("----------------------------------------")

        for food in self.menu:
            print(f"{food.name:<20}₱{food.price:>8.2f}")

        print("========================================")

    def find_food(self, item_name):
        for food in self.menu:
            if food.name.lower() == item_name.lower():
                return food

        return None

    def take_order(self):
        while True:
            self.display_menu()

            while True:
                item_name = input(
                    "\nEnter menu item: "
                ).strip().title()

                food = self.find_food(item_name)

                if food is not None:
                    break
                else:
                    print(
                        "Invalid item. Please choose from the menu."
                    )

            while True:
                try:
                    quantity = int(
                        input("Enter quantity: ")
                    )

                    if quantity > 0:
                        break
                    else:
                        print(
                            "Quantity must be greater than 0."
                        )

                except ValueError:
                    print("Please enter a valid number.")

            order = OrderItem(food, quantity)

            self.orders.append(order)

            print(
                f"\nAdded: {quantity} x "
                f"{food.name} = "
                f"₱{order.get_total():.2f}"
            )

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

    def calculate_subtotal(self):
        subtotal = 0

        for order in self.orders:
            subtotal += order.get_total()

        return subtotal

    def calculate_discount(self, subtotal):
        if subtotal >= 500:
            return subtotal * 0.10

        return 0

    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        total = subtotal - discount

        print("\n\n==========================================")
        print("          CABUGNASON FAST FOOD")
        print("            OFFICIAL RECEIPT")
        print("==========================================")

        print(
            f"{'ITEM':<15}"
            f"{'QTY':>5}"
            f"{'PRICE':>10}"
            f"{'TOTAL':>12}"
        )

        print("------------------------------------------")

        for order in self.orders:
            print(
                f"{order.food_item.name:<15}"
                f"{order.quantity:>5}"
                f"₱{order.food_item.price:>9.2f}"
                f"₱{order.get_total():>11.2f}"
            )

        print("------------------------------------------")

        print(
            f"{'SUBTOTAL':<30}"
            f"₱{subtotal:>10.2f}"
        )

        print(
            f"{'DISCOUNT':<30}"
            f"₱{discount:>10.2f}"
        )

        print(
            f"{'TOTAL':<30}"
            f"₱{total:>10.2f}"
        )

        print("==========================================")
        print("        THANK YOU FOR ORDERING!")
        print("          PLEASE COME AGAIN!")
        print("========================================")


def main():
    restaurant = Restaurant()

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

    restaurant.take_order()
    restaurant.print_receipt()


if __name__ == "__main__":
    main()