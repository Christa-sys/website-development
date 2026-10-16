# Art Supplies Billing Tool

def calculate_total(price, quantity):
    total = price * quantity
    return total


def print_bill(item1, price1, quantity1,
               item2, price2, quantity2,
               item3, price3, quantity3):

    total1 = calculate_total(price1, quantity1)
    total2 = calculate_total(price2, quantity2)
    total3 = calculate_total(price3, quantity3)

    grand_total = total1 + total2 + total3

    print("===== ART SUPPLIES BILL =====")
    print(f"{'Item':<15}{'Price':<12}{'Quantity':<10}{'Total'}")
    print("-" * 47)

    print(f"{item1:<15}₦{price1:<11}{quantity1:<10}₦{total1}")
    print(f"{item2:<15}₦{price2:<11}{quantity2:<10}₦{total2}")
    print(f"{item3:<15}₦{price3:<11}{quantity3:<10}₦{total3}")

    print("-" * 47)
    print(f"Grand Total: ₦{grand_total:,}")


# Call the function to print the bill
print_bill(
    "Paint", 2500, 2,
    "Brush", 1000, 3,
    "Canvas", 5000, 1
)