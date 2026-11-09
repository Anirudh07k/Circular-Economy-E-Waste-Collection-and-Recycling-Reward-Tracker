"""Reusable calculations for the COM-501 e-waste reward tracker."""
import math

CATALOGUE = {
    "Smartphone": {"unit_weight": 0.18, "rate": 40.0},
    "Laptop": {"unit_weight": 2.20, "rate": 55.0},
    "Charger": {"unit_weight": 0.12, "rate": 20.0},
    "Keyboard": {"unit_weight": 0.65, "rate": 15.0},
}


def total_weight(items, catalogue):
    """Return gross weight in kg from a list of category/quantity dictionaries."""
    return sum(catalogue[item["category"]]["unit_weight"] * item["quantity"]
               for item in items)


def reward(items, catalogue, bonus_rate=0.10, threshold_kg=5.0):
    """Return base recycling reward plus bonus if collection meets threshold."""
    amount = sum(catalogue[item["category"]]["unit_weight"]
                 * catalogue[item["category"]]["rate"] * item["quantity"]
                 for item in items)
    if total_weight(items, catalogue) >= threshold_kg:
        amount *= (1 + bonus_rate)
    return amount


def bins_required(weight, capacity_kg=5.0):
    """Estimate whole bins needed (empty collections need zero bins)."""
    if capacity_kg <= 0:
        raise ValueError("Bin capacity must be positive.")
    if weight < 0:
        raise ValueError("Weight cannot be negative.")
    return math.ceil(weight / capacity_kg)


def generate_metric(items, catalogue, metric_function):
    """Call an analytics function passed as an argument."""
    return metric_function(items, catalogue)


def size_label(weight):
    if weight < 3:
        return "SMALL"
    if weight <= 8:
        return "MEDIUM"
    return "LARGE"
