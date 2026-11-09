"""Q4: Test modular analytics, default/keyword parameters, higher-order function."""
import recycling_utils as utils

items = [
    {"category": "Smartphone", "quantity": 3},
    {"category": "Laptop", "quantity": 2},
    {"category": "Charger", "quantity": 2},
    {"category": "Keyboard", "quantity": 1},
]
weight = utils.generate_metric(items, utils.CATALOGUE, utils.total_weight)
print("===== RECYCLING ANALYTICS =====")
print(f"generate_metric(..., total_weight): {weight:.2f} kg")
print(f"reward() default bonus (10%)     : Rs.{utils.reward(items, utils.CATALOGUE):.2f}")
print(f"reward(bonus_rate=0.15)         : Rs.{utils.reward(items, utils.CATALOGUE, bonus_rate=0.15):.2f}")
print(f"reward(threshold_kg=6.0)        : Rs.{utils.reward(items, utils.CATALOGUE, threshold_kg=6.0):.2f}")
print("bins_required() default 5 kg    :", utils.bins_required(weight))
print("bins_required(capacity_kg=3.0)  :", utils.bins_required(weight, capacity_kg=3.0))
