
dictionary = {"cities":["madison","milwaukee","eau claire"]}

dictionary["cities"].append("Beloit")

dictionary["states"] = ["michigan", "Oklahoma", "Arkansas"]
for city in dictionary["cities"]:
    print(city)

for state in dictionary["states"]:
    print(state)
