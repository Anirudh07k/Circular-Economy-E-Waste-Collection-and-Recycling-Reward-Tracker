"""Q1: One device collection, types, formatting and slicing."""
participant = input("Participant: ").strip().title()
device = input("Device category: ").strip().title()
quantity = int(input("Quantity: "))
unit_weight = float(input("Unit weight (kg): "))
recovery = float(input("Recovery (%): "))
rate = float(input("Reward rate (Rs./recyclable kg): "))

total_weight = quantity * unit_weight
recyclable_weight = total_weight * recovery / 100
estimated_reward = recyclable_weight * rate
code = participant.replace(" ", "")[:3].upper() + device.replace(" ", "")[:2].upper()

print("\n===== SINGLE COLLECTION ESTIMATE =====")
print("Participant      :", participant)
print("Device           :", device)
print("Collection code  :", code)
print("Quantity type    :", type(quantity))
print("Unit weight type :", type(unit_weight))
print(f"Total weight     : {total_weight:.2f} kg")
print(f"Recyclable weight: {recyclable_weight:.3f} kg")
print(f"Estimated reward : Rs.{estimated_reward:.2f}")
