seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()
match seat_type:
    case "sleeper":
        print("Sleeper - No Ac, beds avaliable")
    case "ac":
        print("AV - Air Conditioned, comfy ride")
    case "general":
        print("General - cheapest, no reservaiton")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")            