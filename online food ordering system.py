# Online Food Ordering System

menu = {
    1: ("Pizza", 250),
    2: ("Burger", 120),
    3: ("Biryani", 180),
    4: ("Fried Rice", 150),
    5: ("Sandwich", 100),
    6: ("Soft Drink", 50)
}

print("================================")
print("     ONLINE FOOD ORDERING")
print("================================")

print("\nMenu:")
for number, (food, price) in menu.items():
    print(f"{number}. {food} - Rs.{price}")

total = 0
order = []

while True:
    choice = int(input("\nEnter food number (0 to finish): "))

    if choice == 0:
        break

    if choice in menu:
        quantity = int(input("Enter quantity: "))

        food, price = menu[choice]
        amount = price * quantity

        order.append((food, quantity, price, amount))
        total += amount

        print(f"{food} added to your order.")
    else:
        print("Invalid food number.")

print("\n================================")
print("          BILL")
print("================================")

if len(order) == 0:
    print("No items ordered.")
else:
    for food, quantity, price, amount in order:
        print(f"{food} x {quantity} = Rs.{amount}")

    delivery_charge = 40

    print("--------------------------------")
    print(f"Food Total       : Rs.{total}")
    print(f"Delivery Charge  : Rs.{delivery_charge}")

    grand_total = total + delivery_charge

    print(f"Grand Total      : Rs.{grand_total}")
    print("================================")
    print("Thank you for your order!")
