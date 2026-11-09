"""Q2: Interactive mixed collection using a dictionary, list, set and loops."""
import recycling_utils as utils

catalogue = utils.CATALOGUE
items = []
unique_categories = set()
print("Available categories:", ", ".join(catalogue))

while True:
    entered = input("Device category (or DONE): ").strip()
    if entered.upper() == "DONE":
        break
    category = next((name for name in catalogue
                     if name.lower() == entered.lower()), None)
    if category is None:
        print("Rejected: Unsupported category.")
        continue
    quantity_text = input("Quantity: ").strip()
    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Rejected: Quantity must be a whole number.")
        continue
    if quantity <= 0:
        print("Rejected: Quantity must be greater than zero.")
        continue
    items.append({"category": category, "quantity": quantity})
    unique_categories.add(category)
    print("Accepted:", category, "x", quantity)

weight = utils.total_weight(items, catalogue)
base = utils.reward(items, catalogue, bonus_rate=0.0)
final = utils.reward(items, catalogue)
print("\n===== MIXED COLLECTION SUMMARY =====")
for item in items:
    print(f"{item['category']:<12} x {item['quantity']}")
print("Unique categories:", ", ".join(sorted(unique_categories)) if items else "None")
print(f"Total weight     : {weight:.2f} kg")
print("Classification   :", utils.size_label(weight))
print(f"Base reward      : Rs.{base:.2f}")
print("Bonus            :", "10%" if weight >= 5 else "0%")
print(f"Final reward     : Rs.{final:.2f}")
