def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not us_cup_clean():
        was_cup()
    add_to_cup("tea_leaves") 
    add_to_cup("sugar")
    pour("boiled water")
    stie("cup")
    serve("chai")        


make_chai()