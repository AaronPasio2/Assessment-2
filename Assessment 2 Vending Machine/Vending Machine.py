def vending_machine():
    # Display Available Products
    print("\nAvailable Products:")
    products = {
        "I1": ("Pringles Chips", 1.50 ),
        "I2": ("Pepsi", 3.00 ),
        "I3": ("Hersehey's Chocolate", 3.50 ),
        "I4": ("Orange Juice", 2.00 ),
    }
     # For Loop to Display Available Products
    while True:
        for code, (name, price) in products.items():
            print(f"{code}: {name} - {price:.2f} AED")
     # Input Product Code
        code = input("\nEnter the product code: ").strip()
        if code not in products:
            print("Error, Invalid Code .")
            continue
     #  Product Details
        name, price = products[code]
        print(f"\nYou selected {name} - {price:.2f} AED")
     # Payment Transaction
        try:
            amount = float(input(f"Input {price:.2f} AED: "))
            if amount < price:
                print("Ivalid cash. Transaction canceled.")
            elif amount > price:
                print(f"Returning change: {amount - price:.2f} AED")
        except ValueError:
            print("Invalid cash. Transaction canceled.")
            continue
     # Dispense Product
        print(f"Dispensing {name}...")
     # Another Transaction
        if input("Another transaction? (yes/no): ").strip().lower() != "yes":
            print("\nThank you for using the vending machine")
            break

if __name__ == "__main__":
    vending_machine()