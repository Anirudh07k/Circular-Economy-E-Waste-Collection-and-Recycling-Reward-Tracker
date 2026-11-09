"""Class model shared by Milestones 3-5."""
import recycling_utils as utils


class EWasteCollection:
    centre_name = "MIET Circular Economy Recycling Centre"

    def __init__(self, collection_id, participant_name, items=None):
        self.collection_id = collection_id.strip().upper()
        self.participant_name = participant_name.strip().title()
        self.items = []
        for entry in (items or []):
            self.add_item(entry["category"], entry["quantity"])

    def add_item(self, category, quantity):
        match = next((name for name in utils.CATALOGUE
                      if name.lower() == category.strip().lower()), None)
        if match is None:
            raise KeyError(category)
        quantity = int(quantity)  # May raise ValueError for non-numeric input.
        if quantity <= 0:
            raise ValueError("Quantity must be a positive whole number.")
        self.items.append({"category": match, "quantity": quantity})

    def total_weight(self):
        return utils.total_weight(self.items, utils.CATALOGUE)

    def total_reward(self):
        return utils.reward(self.items, utils.CATALOGUE)

    def __len__(self):
        return sum(entry["quantity"] for entry in self.items)

    def display_summary(self):
        weight = self.total_weight()
        base = utils.reward(self.items, utils.CATALOGUE, bonus_rate=0.0)
        print(f"\n===== COLLECTION {self.collection_id} =====")
        print("Centre       :", self.centre_name)
        print("Participant  :", self.participant_name)
        for entry in self.items:
            print(f"  {entry['category']:<12} x {entry['quantity']}")
        print("Device count :", len(self))
        print(f"Total weight : {weight:.2f} kg")
        print("Size         :", utils.size_label(weight))
        print(f"Base reward  : Rs.{base:.2f}")
        print("Bonus        :", "10%" if weight >= 5.0 else "0%")
        print(f"Final reward : Rs.{self.total_reward():.2f}")

    def to_record(self):
        """One pipe-delimited persistent summary."""
        item_text = ",".join(f"{x['category']}:{x['quantity']}" for x in self.items)
        return (f"{self.collection_id}|{self.participant_name}|{item_text}|"
                f"{len(self)}|{self.total_weight():.2f}|"
                f"{utils.size_label(self.total_weight())}|{self.total_reward():.2f}")
