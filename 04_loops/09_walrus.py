# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not Divisible, remainder is {remainder}")

value = 13

if(remainder := value % 5):
    print(f"Not Divisible, remainder is {remainder}")

available_sizes = ["small","medium","large"]

if(requesr_size := input(f"Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requesr_size} chai")
else:
    print(f"Size is unavailable - {requesr_size}")

flavors = ["masala","ginger","lemon","mint"]
print("available flavors: ",flavors)

while(flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")
    
print(f"You choose {flavor} chai")