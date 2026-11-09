# COM-501 Group 7: Circular Economy E-Waste Collection and Recycling Reward Tracker

**Student:** Anirudh Kapoor | **Roll No.:** 2024A1R036 | **Semester:** 5th

This is a Python 3 console application. No external packages are required.

## Run the final application

```bash
python main.py
```

Use menu option 1 to add a collection. `recycling_records.txt` is updated (appended) when a collection is completed. Use option 2 to view history, option 3 for modular analytics, option 4 to demonstrate the corrected type-conversion bug, and option 5 to exit.

## Other milestone evidence

Run `python milestone1.py`, `python milestone2.py`, `python milestone3.py`, or `python milestone4.py` to see the incrementally developed requirements. Milestones 3-5 share `collection.py`, and Milestones 2-5 share `recycling_utils.py`. `main.py` is the final application.

Run tests: `python -m unittest discover -s tests -v`.

### Calculation assumptions

Milestone 1 uses the supplied 80% recovery percentage when estimating *recyclable* weight and reward. Milestones 2-5 have a fixed catalogue specifying gross unit weights and reward rates, but no per-device recovery percentages; their rewards are therefore computed as `sum(quantity * unit_weight * rate)`, then increased by 10% if total weight is at least 5 kg. The 5-kg bonus threshold is inclusive. Size labels: SMALL below 3 kg, MEDIUM from 3 to 8 kg inclusive, and LARGE above 8 kg.

`recycling_records.txt` is an example of persisted data and can be cleared to begin a new session. The file's seven `|`-separated fields are: ID, participant, item counts, total devices, weight (kg), size, reward (Rs.).

**GitHub repository:** Add the individual student's repository link to the submitted report after uploading the complete source folder; the assignment requires each group member's own link.
