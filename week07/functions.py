# --- Self Reflection Comments ---
#1) The first bug I spotted was bug 2, aka the missing colon. This is because I ran the code and that was the first error it produced. I think this demonstrates I'm ok with trusting the python Error Messages, but maybe that I need to be more aware of the finer details. 
#2) apply_discount(price, tier) is a function that will apply a given discount based off a pre-set tier list. If you input a specific price, and the tier that it is matched to, it will verify a specific discount amount and apply it. If the colleague knew a little bit of python, they might be able to use it. It's relatively self evident. 
#3) AI Disclosure: I used ChatGPT as a debugging and learning aid to help interpret error messages, clarify Python concepts, guide my reasoning through problems, and write my disclosure statement because I didn't know what it'd need to look like. I wrote and implemented the code fixes myself.
#3, pt.2) I think as the class has progressed, I have used AI less and less. I still use it often because it does give me confidence when, after writing code, ChatGPT lets me know it looks good, but I try to do all the work and troubleshooting on my own. I mainly use it for revision and when I really have no idea what to do. I do really think it's been a useful tool for me, and has not prevented me from learning. 

# --- Exercise 1 --- 
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100,0.07):,.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250,0.08):,.2f}")

# --- Exercise 2 --- 
def apply_discount(price, tier):
    tier = tier.lower()
    if tier == "gold":
        return price * (1-0.15)
    elif tier == "silver":
        return price * (1-0.10)
    elif tier == "bronze":
        return price * (1-0.05)
    else:
        return price * (1-0)

price_1 = float(input(f"Enter Price: $"))
tier_1 = (input(f"Enter Price: "))

print(f"Price ${price_1:,.2f}, Tier: {tier_1.capitalize()}, Discounted Price: ${apply_discount(price_1, tier_1):,.2f}") 
#I know this isn't what the lab specifically asked for but come on you can't tell me this isn't nifty... 

# --- Exercise 2 (How the Lab Actually Wants it) --- 
def apply_discount(price, tier):
    if tier == "gold":
        return price * (1-0.15)
    elif tier == "silver":
        return price * (1-0.10)
    elif tier == "bronze":
        return price * (1-0.05)
    else:
        return price * (1-0)

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):,.2f}")
#so as to not write 4 individual print statements. 

# --- Exercise 3 --- 

def final_price(price, tier, tax_rate):
    return apply_discount(price,tier) * (1 + tax_rate)

print(f"After Gold Discount: ${apply_discount(200, 'gold'):,.2f}")
print(f"After Tax: ${final_price(200,'gold',0.07):,.2f}")
print(f"final_price(200, 'gold', 0.07) = ${final_price(200,'gold',0.07):,.2f}")

# --- Exercise 4 --- 

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
#is the starter code just... a complete solution already? 

# --- Exercise 5 --- 

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale 
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales [i])
    i+= 1 

#Pre-Fix Comments: 
#1) total cannot = sale. it has to be += if not it will just replace and not add. this one won't produce an error message which is annoying
#2) the second 'for sale in sales' needs a colon. if not it will produce a SyntaxError. 
#3) this one was hard but i'm pretty sure that since it's a while loop, it won't stop. this means i will continue counting up into 5 because this code doesn't give it a stopping condition. and since there is no 5th value, it'll produce an IndexError? 

#AI-Helper Results:
#I didn't need help at all with error 2. Syntax error is easy to identify. Error 1 was a bit odd because I really didn't catch it at first. Error 3 was honestly confusing. ChatGPT helped me understand that when it returns an Index Error, it's because i is counting up too high. This is the main risk with the 'while' loops, since you need to manage the index yourself.

#Fixes:
#1) replaced = in line 71 with += 
#2) added : at the end of sales in line 75
#3) I was originally gonna do an if statement with a break. I asked AI if it agreed with my fix, and it pointed out that it can also be fixed by just removing the = in the <= of the while loop. 

#Debrief:
#I feel like in these situations, AI is a good rubber duck, because it talks back. If you specifically tell it not to give you the solution, it'll ask guiding questions that point you in the right direction. In my case, AI was able to explain the error to me in human words. Not that the errors are hard to understand, but it's still useful.

# --- Exercise 6 --- 

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?

#Predictions: 
#1) The first line will print 100
#2) The second line will print 1998
#3) No, nothing will have changed. Since the x that = 999 is local, the outside code simply cannot recognize it. 

#Results:
#My predictions were correct! The reason for this is because of scope. As I previously said, x only = 999 inside def double_it. Because of this, python will not read x as 999 in any case ouside double_it. This is because x is 999 to a local extent. Since this is the case, print(x) will result in 100 no matter what. 
#I do remember reading somewhere that when python is done with a local variable, it "throws it away" until it needs to reuse it. 

#Scope is the area of the code where a variable can be accessed. A local variable only exists within its functions and does not change a global one with the same name. 