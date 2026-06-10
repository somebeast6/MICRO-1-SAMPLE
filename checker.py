import json

products = []

with open("products.json", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            products.append(json.loads(line))

print("\n===== VALIDATION REPORT =====\n")

# Duplicate IDs
ids = []

for p in products:
    pid = p["_id"]

    if isinstance(pid, dict):
        pid = pid["$oid"]

    ids.append(pid)

duplicates = set(
    x for x in ids
    if ids.count(x) > 1
)

if duplicates:
    print("DUPLICATE IDS:")
    print(duplicates)

# Rating check
for p in products:

    rating = p.get("rating")

    if rating is not None:
        if rating < 0 or rating > 5:
            print(
                f"INVALID RATING: {p['name']}"
            )

# Typo field names
for p in products:

    for key in p.keys():

        if "tarriff" in key.lower():
            print(
                f"FIELD TYPO: {key}"
            )

# Typo values
def scan(obj):

    if isinstance(obj, dict):

        for v in obj.values():
            scan(v)

    elif isinstance(obj, list):

        for v in obj:
            scan(v)

    elif isinstance(obj, str):

        if "tarriff" in obj.lower():

            print(
                f"VALUE TYPO: {obj}"
            )

for p in products:
    scan(p)

# for field consistency
for p in products:

    if "for" in p:

        if not isinstance(
            p["for"],
            list
        ):

            print(
                f"TYPE ISSUE: {p['name']} -> for should be array"
            )

print("\n===== FINISHED =====")