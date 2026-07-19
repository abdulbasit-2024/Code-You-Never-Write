# Your transaction data
transactions = [
    {"date": "2026-07-01", "desc": "Meta Ads Campaign", "amount": 30000},
    {"date": "2026-07-03", "desc": "News Website Domain", "amount": 3500},
    {"date": "2026-07-05", "desc": "Grocery (Chicken)", "amount": 800},
    {"date": "2026-07-08", "desc": "Phone VPN Subscription", "amount": 1500},
    {"date": "2026-07-08", "desc": "Phone VPN Subscription", "amount": 1500},
    {"date": "2026-07-12", "desc": "Meta Ads Campaign", "amount": 30000},
    {"date": "2026-07-15", "desc": "Kashmir Tour Deposit", "amount": 15000},
]

# 1. Calculate the total amount spent
total_spent = sum(t["amount"] for t in transactions)

# 2. Find exact duplicate payments
seen_payments = set()
duplicates = []

for t in transactions:
    # We create a unique "fingerprint" for every row
    payment_fingerprint = (t["date"], t["desc"], t["amount"])
    
    if payment_fingerprint in seen_payments:
        duplicates.append(t)
    else:
        seen_payments.add(payment_fingerprint)

# 3. Print the results clearly
print(f"Total Amount Spent: {total_spent}")
print("\n--- Duplicate Check Results ---")

if duplicates:
    print("WARNING: Found the following duplicate payments:")
    for d in duplicates:
        print(f"- {d['date']}: {d['desc']} (Cost: {d['amount']})")
else:
    print("Good news: No exact duplicate payments found.")
