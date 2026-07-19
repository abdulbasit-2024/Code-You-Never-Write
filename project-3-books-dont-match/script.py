# 1. The Known Rules and Expectations
expected_total = 60000
target_per_person = 15000

# Everyone who is supposed to pay
expected_people = ["Anas Rafique", "Abdul Basit", "Abu Huraira", "Noman Habib"]

# 2. The Messy Digital Records
messy_records = [
    {"memo": "Anas Transfer", "amount": 15000},
    {"memo": "Basit Trip", "amount": 15000},
    {"memo": "Abu H. partial", "amount": 10000}
]

# 3. Personal Rules for Interpreting Ambiguous Memos
memo_to_name = {
    "Anas Transfer": "Anas Rafique",
    "Basit Trip": "Abdul Basit",
    "Abu H. partial": "Abu Huraira"
}

# 4. Process the Books
amounts_paid = {name: 0 for name in expected_people}
total_received = 0

for record in messy_records:
    memo = record["memo"]
    amount = record["amount"]
    
    # Translate the messy memo to the real name
    if memo in memo_to_name:
        real_name = memo_to_name[memo]
        amounts_paid[real_name] += amount
        total_received += amount

# Calculate the gaps
total_gap = expected_total - total_received

# 5. Print the Reconciled Books
print("--- KASHMIR TOUR RECONCILIATION ---")
print(f"Expected Total: {expected_total}")
print(f"Total Received: {total_received}")
print(f"TOTAL GAP: {total_gap}\n")

print("--- WHO TO FOLLOW UP WITH ---")
for person in expected_people:
    paid = amounts_paid[person]
    if paid < target_per_person:
        owed = target_per_person - paid
        print(f"WARNING: {person} owes {owed}")
