names = ["sushil","sushil1","sushil2","sushil3"]
bills = [50,70,100,3000]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")