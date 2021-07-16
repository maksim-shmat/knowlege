"""Basic usage of Walrus Operator."""

sample_data = [
        {"id": 1, "name": "Amol", "project": False},
        {"id": 2, "name": "Kiku", "priject": False},
        {"id": 3, "name": None, "project": False},
        {"id": 4, "name": "Lini", "project": True},
        {"id": 4, "name": None, "project": True},
]

print("With Python 3.8 Walrus Operator\n---------------------------")
for entry in sample_data:
    if name := entry.get("name"):
        print('Found Person:', name)

print("\nWithout Walrus Operator\n-----------------------------")
for entry in sample_data:
    name = entry.get("name")
    if name:
        print('Found Person:', name)
