chai_order = dict(type="Masala Chai", size="medium", sugar=2)
print(f"Chai order: {chai_order}")

chai_receipe = {}
chai_receipe["base"] = "black tea"
chai_receipe["liquid"] = "milk"

print(f"Receipe Base: {chai_receipe['base']}")
print(f"Chai order: {chai_order}")
del chai_receipe["liquid"]
print(f"Receipe : {chai_receipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

# print(f"Order details (keys):{chai_order.keys()}")
# print(f"Order details (keys):{chai_order.values()}")
# print(f"Order details (keys):{chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"Cardamon":"crushed", "gigner":"sliced"}
chai_receipe.update(extra_spices)

print(f"Updated chai recipe: {chai_receipe}")

customer_Note = chai_order.get("size","No Note")

print(f"Chai size is : {customer_Note}")