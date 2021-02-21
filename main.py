# Course: CS 30
# Period: 1
# Date created: 29/01/21
# Date last modified: 20/02/21
# Name: Boyd Guo
# Description: RPG Nested Dictionaries


characters = {
    "Ryan": {
        "rank": "Private",
        "age": 17,
        "characteristics": "Naive"
    },
    "Blaine": {
        "rank": "Sergeant",
        "age": 34,
        "characteristics": "Cynical"
    }
}

# Prints the info for each character
print("Characters:")
for character, data in characters.items():
    print(f"""\
{character}:
    Rank: {data["rank"]}
    Age: {data["age"]}
    Characteristics: {data["characteristics"]}
    """)

# Inventory items held by each character
inventories = {
    "Soldier": ["Rifle", "Pistol", "Canteen Bottle", "Grenade"],
    "Sergeant": ["Rifle", "Knife", "Canteen Bottle", "Map"]
}

# Print the inventory items as a comma separated list
print("Inventories:")
for inventory, data in inventories.items():
    print(f"""\
{inventory}:
    {', '.join(data)}
    """)

# Descriptions of each location
locations = {
    "Beaches": "A heavily fortified beach held by enemy troops and artillery",
    "Plains": "A seemingly peaceful plain with hidden enemy machine gun",
    "Village": "A once beautiful village now ridden with entrenched enemy forces",
    "Windmill": "A safe haven for tired soliders seeking shelter",
    "Bridge": "A hotly contested objective that could pave to road for victory"
}

# Prints each location with its description
print("Locations:")
for location, data in locations.items():
    print(f"{location}: {data}")