
# Import functions from grocery.py
from grocery import show_items, add_item, print_bill

# Empty dictionary to store selected items
cart = {}


# Main menu function
def main():
    while True:
        print("\n====== GROCERY BILLING SYSTEM ======")
        print("1. View Grocery Items")
        print("2. Add Item to Cart")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_items()

        elif choice == "2":
            add_item(cart)

        elif choice == "3":
            print_bill(cart)

        elif choice == "4":
            print("\nThank you for using our system!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the main program
main()
