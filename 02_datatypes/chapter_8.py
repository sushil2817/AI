ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")
spice_options = ["ginger","cardamom"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"Chai: {chai_ingredients}")
last_added = chai_ingredients.pop()
print(f"Last: {last_added}")
chai_ingredients.reverse()
print(f"Chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai: {chai_ingredients}")
sugar_level = [0,1,2,3,4,5,6]
print(f"Maximum sugar level: {max(sugar_level)}")
print(f"Maximum sugar level: {min(sugar_level)}")

# operator overloading

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor

print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea","water"]*3
print(f"String brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data.replace(b"Cinna",b"CARD")
print(f"raw data {raw_spice_data}")
