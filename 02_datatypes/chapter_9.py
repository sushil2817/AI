essential_spices = {"Cardamon", "ginger","cinnamon"}

optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices

print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices

print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"onlu in essential spices: {only_in_essential}")


print(f"IS 'cloves' in essesntial spices? {'cloves' in optional_spices}")
