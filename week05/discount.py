# --- Self-Assessment Questions ---

#1) For an order total of $350, the program skips the $500 tier, sees that it is at least $200, stops there, and applies the 10% discount.
#2) "and" requires both conditions to be true at the same time, while separate "if" statements check each condition independently and if they could both run. 
#3) I'm not exactly sure if it has any specific use in my current day-to-day life, but i'm sure that within businesses being able to run a specific order through a bunch of conditions to see the exact bonuses or discounts applicable is extremely useful and time saving compared to having to run it manually. 

# --- Exercise 1 --- 

total = float(input("Enter cart total: $"))
discount = 0
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# --- Exercise 2 --- 
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")

# --- Exercise 3 --- 
region = input("Enter region: ")
if region == "South" and total >= 200:
    discount += 0.02
    print("Region bonus applied: additional 2% off")
final = total * (1 - discount)
print(f"Final discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# --- Exercise 4 ---
customer_type = input("Enter customer type: ")

#Flat condition is easier to read because everything is visible in one line.
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# --- Exercise 5 --- 
amount = float(input("Enter transaction amount: "))

if amount <= 0:
    print("SUSPICIOUS")
elif amount >= 10000:
    print("LARGE - REVIEW REQUIRED")
else:
    print("NORMAL")

# --- Exercise 6 --- 
spent = float(input("Enter yearly spending: $"))
orders = int(input("Enter number of orders: "))
outstanding_balance = input("Outstanding balance? (yes/no): ")

if (spent > 2000 or orders > 10) and not outstanding_balance == "yes":
    print("VIP upgrade")
else:
    print("No VIP upgrade")
