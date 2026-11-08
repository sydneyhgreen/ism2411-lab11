# 1. I would use bracket notation when a key must exist, like a customer ID or price that the rest of the program depends on, because a KeyError tells me right away that the data is broken. I would use .get() when a field is optional or might be missing, like an email or phone number, so the program keeps running with a default value. My rule of thumb is that bracket notation is for required data and .get() is for optional data.
# 2. The summary dictionary in Exercise 8 reminds me of a PivotTable or a SUMIF in Excel, where you total sales for each region. The Python version is more useful for large datasets because the same short loop works on 10 rows or 10 million rows. It also doesn't need manual refreshing or formulas copied down a sheet, and Excel can slow down or hit its row limit on huge files.

print("--- Exercise 1: One Customer ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2: Update and Add ---")
customer["phone"] = "555-0101"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

print("--- Exercise 3: Safe Lookup ---")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError caught: {error}")

print("--- Exercise 4: Iterate ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over the dict directly (without .items()) only gives the keys, so
# I'd have to look up each value myself with customer[key]. .items() gives
# me the key and its value together on every pass.
for key in customer:
    print(key)

print("--- Exercise 5: Lookup Table ---")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)
print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")

print("--- Exercise 6: List of Dicts ---")
customers = [
    {"name": "Alice", "email": "alice@example.com", "tier": "platinum", "ytd_spend": 5200.00},
    {"name": "Bob", "email": "bob@example.com", "tier": "silver", "ytd_spend": 840.25},
    {"name": "Carmen", "email": "carmen@example.com", "tier": "gold", "ytd_spend": 2300.75},
    {"name": "Dev", "email": "dev@example.com", "tier": "bronze", "ytd_spend": 120.00},
]

for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    amount_off = 300 * rate
    print(f"{c['name']} | {c['tier']} | discount on $300: ${amount_off:.2f}")

print("--- Exercise 7: Nested Catalog ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")

print("--- Exercise 8: Sales by Region ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
