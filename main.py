"""Q5 and final runnable program. Start with: python main.py"""
from pathlib import Path
from collection import EWasteCollection
import recycling_utils as utils

RECORDS_FILE = Path(__file__).with_name("recycling_records.txt")


def display_records():
    try:
        with open(RECORDS_FILE, "r", encoding="utf-8") as file:
            print("\n===== SAVED COLLECTION HISTORY =====")
            print("ID | Participant | Items | Count | Weight kg | Size | Reward Rs.")
            found = False
            for line in file:
                if line.strip():
                    found = True
                    print(" | ".join(line.rstrip("\n").split("|")))
            if not found:
                print("No records saved yet.")
    except FileNotFoundError:
        print("FileNotFoundError: recycling_records.txt is not available yet.")


def save_collection(collection):
    with open(RECORDS_FILE, "a", encoding="utf-8") as file:
        file.write(collection.to_record() + "\n")


def enter_collection():
    collection_id = input("Collection ID: ").strip()
    participant = input("Participant name: ").strip()
    collection = EWasteCollection(collection_id, participant)
    print("Device catalogue:", ", ".join(utils.CATALOGUE))
    while True:
        category = input("Device category (or DONE): ").strip()
        if category.upper() == "DONE":
            break
        quantity = input("Quantity: ").strip()
        try:
            collection.add_item(category, quantity)
            print("Item added.")
        except ValueError as error:
            print("ValueError:", error)
        except KeyError:
            print(f"KeyError: Unsupported category '{category}'.")
    if len(collection) == 0:
        print("Empty collection not saved.")
        return None
    collection.display_summary()
    save_collection(collection)
    print("Collection appended to recycling_records.txt")
    return collection


def show_analytics(collection):
    if collection is None:
        print("Create a collection in this session to view analytics.")
        return
    weight = utils.generate_metric(collection.items, utils.CATALOGUE, utils.total_weight)
    print(f"Function-as-argument weight : {weight:.2f} kg")
    print(f"Default reward              : Rs.{utils.reward(collection.items, utils.CATALOGUE):.2f}")
    print("5-kg recycling bins needed  :", utils.bins_required(weight))


def debug_demo():
    print("\n===== DEBUGGING TYPE CONVERSION =====")
    quantity = "3"          # input() always produces a string.
    unit_weight = 0.18
    try:
        wrong_total = quantity * unit_weight
        print(wrong_total)
    except TypeError as error:
        print("TypeError:", error)
    correct_total = int(quantity) * unit_weight
    print(f"After int(quantity): {correct_total:.2f} kg")


def main():
    print("===== CIRCULAR ECONOMY E-WASTE REWARD TRACKER =====")
    display_records()
    last_collection = None
    while True:
        print("\n1. Add collection  2. View history  3. Analytics  4. Debug demo  5. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            new_collection = enter_collection()
            if new_collection is not None:
                last_collection = new_collection
        elif choice == "2":
            display_records()
        elif choice == "3":
            show_analytics(last_collection)
        elif choice == "4":
            debug_demo()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid menu option. Choose 1-5.")


if __name__ == "__main__":
    main()
