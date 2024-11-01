child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adult = int(input("How many adults are there? "))

children_price = child_meal * children
adult_price = adult_meal * adult
subtotal = children_price + adult_price

print(f"Subtotal: ${subtotal:.2f}")

tax = float(input("What is the sales tax rate? "))
tax_rate = subtotal * tax/100
print(f"Sales Tax: ${tax_rate}")

amount = subtotal + tax_rate
print(f"Amount: ${amount:.2f}")

#Added tip to restaurant receipt
tip = float(input("Would you like to add a tip? "))
total = amount + tip
print(f"Total: ${total}")

payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")
