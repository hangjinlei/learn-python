import csv

with open(file="./data.csv", mode="r") as f:
    reader = csv.DictReader(f)
    items = list(reader)
    for item in items:
        print(item)
        print(f"{item.get('first')} {item.get('last')}")
