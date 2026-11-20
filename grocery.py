
# Grocery items and their prices
items = {
    1: ["Rice (1 kg)", 5.00],
    2: ["Milk (1 L)", 7.00],
    3: ["Bread (1 loaf)", 3.50],
    4: ["Eggs (10 pcs)", 6.00],
    5: ["Sugar (1 kg)", 4.00]
}


# Function to display grocery items
def show_items():
    print("\n------ AVAILABLE GROCERY ITEMS ------")
    for number in items:
        print(number, ".", items[number][0],
              "- RM", format(items[number][1], ".2f"))


# Function to add items to the cart
def add_item(cart):
    show_items()

    try:
        number = int(input("\nEnter item number: "))

        if number not in items:
            print("Invalid item number!")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        if number in cart:
            cart[number] += quantity
        else:
            cart[number] = quantity

        print("Item added successfully!")

    except ValueError:
        print("Please enter a valid number!")


# Function to calculate and display the bill
def print_bill(cart):
    if len(cart) == 0:
        print("\nYour cart is empty!")
        return

    total = 0

    print("\n========== GROCERY BILL ==========")
    print("Item\t\tQty\tPrice\tTotal")

    for number in cart:
        name = items[number][0]
        price = items[number][1]
        quantity = cart[number]

        amount = price * quantity
        total += amount

        print(name, "\t", quantity, "\t",
              format(price, ".2f"), "\t",
              format(amount, ".2f"))

    print("----------------------------------")
    print("Total Amount: RM", format(total, ".2f"))
    print("Thank you for shopping!")
    print("==================================")
