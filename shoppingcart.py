
orders = []
prices =[]
total = 0

while True:
    order = input("Enter your order (q to quit): ")
    if order.lower()=="q":
        break

    else:
        price = int(input("Enter the price in $: "))
        prices.append(price) 
        order = order.capitalize()
        orders.append(order)
       

print("YOUR CART".center(30, "-"))

for order in orders:
     print(order, end=f" = ${price}\n")

for price in prices:
     total += price


print("+".rjust(30, "-"))
print(f"Your Total: ${total}")

     
        
