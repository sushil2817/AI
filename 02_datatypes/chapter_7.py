masala_spices = ("Cardamom","cloves","cinnamon",)

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
ginger_ratio,cardmom_ratio = 2,1

print(f"Ratio is G: {ginger_ratio} and C: {cardmom_ratio}")
ginger_ratio, cardmom_ratio = cardmom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cardmom_ratio}")

# membership

print(f"Is ginger in masala spices ? {'cinnamon' in masala_spices}")