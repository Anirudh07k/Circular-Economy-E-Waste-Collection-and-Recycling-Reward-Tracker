"""Q3: Two objects and the special __len__ method."""
from collection import EWasteCollection

first = EWasteCollection("AARSM", "aarav", [
    {"category": "Smartphone", "quantity": 3},
    {"category": "Laptop", "quantity": 2},
    {"category": "Charger", "quantity": 2},
    {"category": "Keyboard", "quantity": 1},
])
second = EWasteCollection("DIYKE", "diya")
second.add_item("Smartphone", 2)
second.add_item("Keyboard", 2)

first.display_summary()
print("len(first) =", len(first))
second.display_summary()
print("len(second) =", len(second))
