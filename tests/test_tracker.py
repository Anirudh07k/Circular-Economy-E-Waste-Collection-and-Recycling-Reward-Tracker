"""Run from project folder: python -m unittest discover -s tests -v"""
import unittest
import recycling_utils as u
from collection import EWasteCollection


class TrackerTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            {"category": "Smartphone", "quantity": 3},
            {"category": "Laptop", "quantity": 2},
            {"category": "Charger", "quantity": 2},
            {"category": "Keyboard", "quantity": 1},
        ]

    def test_q1_calculation(self):
        self.assertAlmostEqual(3 * .18 * .80 * 40, 17.28)

    def test_q2_weight_reward_bonus(self):
        self.assertAlmostEqual(u.total_weight(self.items, u.CATALOGUE), 5.83)
        self.assertAlmostEqual(u.reward(self.items, u.CATALOGUE, 0), 278.15)
        self.assertAlmostEqual(u.reward(self.items, u.CATALOGUE), 305.965)
        self.assertEqual(u.size_label(5.83), "MEDIUM")

    def test_boundary_classification(self):
        self.assertEqual(u.size_label(2.99), "SMALL")
        self.assertEqual(u.size_label(3), "MEDIUM")
        self.assertEqual(u.size_label(8), "MEDIUM")
        self.assertEqual(u.size_label(8.01), "LARGE")

    def test_q3_device_count(self):
        c = EWasteCollection("x1", "aarav", self.items)
        self.assertEqual(len(c), 8)

    def test_rejections(self):
        c = EWasteCollection("x1", "aarav")
        with self.assertRaises(KeyError):
            c.add_item("Tablet", 1)
        with self.assertRaises(ValueError):
            c.add_item("Laptop", "abc")
        with self.assertRaises(ValueError):
            c.add_item("Laptop", 0)

    def test_q4_bins_callback(self):
        w = u.generate_metric(self.items, u.CATALOGUE, u.total_weight)
        self.assertEqual(u.bins_required(w), 2)
        self.assertEqual(u.bins_required(0), 0)
        with self.assertRaises(ValueError):
            u.bins_required(5, capacity_kg=0)

    def test_persistence_line(self):
        c = EWasteCollection("aarSm", "aarav", self.items)
        self.assertEqual(len(c.to_record().split("|")), 7)
        self.assertIn("AARSM|Aarav|", c.to_record())


if __name__ == "__main__":
    unittest.main()
