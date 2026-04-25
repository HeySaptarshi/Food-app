import json
import random
import datetime

def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def register():
    users = load_data("users.json")
    username = input("Enter username: ")
    password = input("Enter password: ")

    users.append({"username": username, "password": password})
    save_data("users.json", users)

    print("Registered successfully!")

def login():
    users = load_data("users.json")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return username

    print("Invalid credentials")
    return None

def show_menu(menu):
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def view_cart(menu, cart):
    if not cart:
        print("Cart is empty")
        return

    print("\n--- YOUR CART ---")
    total = 0

    for item, qty in cart.items():
        price = menu[item] * qty
        print(f"{item} x{qty} = ₹{price}")
        total += price

    print("Current Total:", total)

def add_to_cart(menu, cart):
    item = input("Enter item: ")
    if item in menu:
        try:
            qty = int(input("Enter quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print("Added to cart")
        except:
            print("Invalid quantity")
    else:
        print("Item not found")

def calculate_bill(menu, cart):
    total = 0

    print("\n--- BILL ---")
    for item, qty in cart.items():
        price = menu[item] * qty
        print(f"{item} x{qty} = ₹{price}")
        total += price

    # Discount
    if total > 500:
        print("Discount applied: 10%")
        total *= 0.9

    # Delivery charge
    delivery = 40
    print("Delivery charge: ₹40")
    total += delivery

    print("Final Total:", int(total))
    return int(total)

def save_order(username, cart, total):
    orders = load_data("orders.json")

    order_id = random.randint(1000, 9999)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    orders.append({
        "order_id": order_id,
        "user": username,
        "cart": cart,
        "total": total,
        "time": time
    })

    print(f"Order ID: {order_id}")
    print(f"Time: {time}")

    save_data("orders.json", orders)
    print("Order placed successfully!")

def user_flow(username):
    menu = load_data("menu.json")
    cart = {}

    while True:
        print("\n1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")

        choice = input("Choice: ")

        if choice == "1":
            show_menu(menu)

        elif choice == "2":
            show_menu(menu)
            add_to_cart(menu, cart)

        elif choice == "3":
            view_cart(menu, cart)

        elif choice == "4":
            if not cart:
                print("Cart is empty!")
            else:
                total = calculate_bill(menu, cart)
                save_order(username, cart, total)
                break

        else:
            print("Invalid option")

def admin_panel():
    menu = load_data("menu.json")

    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            show_menu(menu)

        elif choice == "2":
            item = input("Item name: ")
            try:
                price = int(input("Price: "))
                menu[item] = price
                save_data("menu.json", menu)
                print("Item added!")
            except:
                print("Invalid price")

        elif choice == "3":
            item = input("Item to remove: ")
            if item in menu:
                del menu[item]
                save_data("menu.json", menu)
                print("Item removed!")
            else:
                print("Item not found")

        elif choice == "4":
            break

        else:
            print("Invalid option")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Admin")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                user_flow(user)

        elif choice == "3":
            admin_panel()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

main()