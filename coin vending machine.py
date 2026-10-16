def calculate_change(paid,price):
    change = paid - price
    return change

snack_price = 25
print("===Snack vending machine===")
print(f"This snack costs ₦{snack_price} units")
print(f"Accepted coins: 1, 5, 10, 25")

total_inserted = 0
coins_inserted = 0

while True:
 coin = int(input("Insert a coin (1, 5, 10, 25): "))
 if coin != 1 and coin != 5 and coin != 10 and coin != 25:
     print("Invalid coin. Please insert a valid coin.")
     continue

 total_inserted += coin
 coins_inserted += 1
 print(f"inserted coins: {coins_inserted}. Total so far: ₦{total_inserted}\n")

 if total_inserted >= snack_price:
    print("Enough money inserted\n")
    break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing snack...")
if change_due == 0:
   pass
else:
   print(f"This is your change: ₦{change_due}")

print("\n===== PURCHASE SUMMARY =====")   
print(f"Snack price: ₦{snack_price}")
print(f"Total PAID: ₦{total_inserted}")
print(f"Change due: ₦{change_due}")
print(f"Change given: ₦{change_due}")
print("================================")
print("Thank you for your purchase!")
