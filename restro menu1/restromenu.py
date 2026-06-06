menu = {
    'coffe': 50,
    'pasta': 60,
    'pizza': 80,
    'burger': 50,
    'maggi': 60,
    'coldcoffe': 90,
    'rice': 50,
    'Manchurian': 60,
    'kabab paratha': 40,
    'chicken Biryani': 90,
    'mutton biryani': 180,
    'kabab': 40,
    'roti palne': 10,
    'Butter roti': 15,
    'tanduri roti': 12,
    'kabab tikka': 80,
    'chicken fry': 90,
    'chicken gravi': 280,
    'mutton gravi': 350,
    'mutton fry': 400,
    'salat extra': 10,
    'minral water': 20,
    'thumsup': 20,
    'sprit': 20,
    'thumpsup 2litter': 90,
    'sprit 2litter': 90,
    'limlka 2litter': 90
}

# Greeting
print("Welcome to the Faisal Ali Restaurant")

# Display menu
print("\nMenu:")
for item, price in menu.items():
    print(f"{item} : Rs{price}")

order_total = 0

# First order
item_1 = input("\nEnter your order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, '{item_1}' is not available in the menu.")

# Second order
another_order = input("Do you want to order another item? (yes/no): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' added to the order.")
    else:
        print(f"Sorry, '{item_2}' is not available.")

# Final bill
print(f"\nYour total amount to pay is Rs{order_total}")
print("Thank you for visiting my restaurant!")