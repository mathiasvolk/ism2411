# --- Self-Assessment Questions --- 

#The accumulator pattern consists of 3 steps: initialize, loop, update. Start a variable, go through each value, and update it each time to get a final result.
#The "while" loop is longer because you have to track the index manually. "For" is simpler, but "While" gives you more control.
#I actually found this'd be useful in my accounting class's homework because it could help me keep track of sales transactions and give me a total sales count. 

# --- Exercise 1 ---
sales = [120,80,250,175,90,410,60,215]
total = 0
for sale in sales: 
    total += sale

print(f"Total: ${total}")

# --- Exercise 2 --- 
total = 0 
count = 0

for sale in sales:
    total += sale
    count += 1

average = total / count

print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# --- Exercise 3 --- 
current_max = 0

for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

# --- Exercise 4 ---
count_over_100 = 0
total_over_100 = 0

for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

# --- Exercise 5 ---
for sale in sales: 
    if sale > 400: 
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break

    if sale <= 100:
        continue
    
    print(f"${sale}")

# --- Exercise 6 --- 
total = 0
i = 0

while i < len(sales):
    total+= sales [i]
    i += 1
    
print(f"Total: ${total}")

# I'd use the for loop version since it's easier to read and doesn't require you to manually track an index.

# --- Exercise 7 ---

for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    print(f"${sale} -> {discount:.0%} discount -> ${discounted_price:.2f}")
