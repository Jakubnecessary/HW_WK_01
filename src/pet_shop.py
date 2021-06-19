# WRITE YOUR FUNCTIONS HERE

# 1 Function pet_shop name      22

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2 Function total cash      21

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#   Function add cash  += adds equal    20

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# # Function remove cash 
# doesnt return just changes     19

def add_or_remove_cash(pet_shop, cash_remove):
    pet_shop["admin"]["total_cash"] += cash_remove

# Function get pets sold   18

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Function to increse pets
#  sold by 2 += adds equal  17

def increase_pets_sold(pet_sold, add_pet):
    pet_sold["admin"]["pets_sold"] += add_pet

# function to get stock count = 6 use len()
#  to return number of 
# characters in the string    16

def get_stock_count(pets_count):
    return len(pets_count["pets"])

# function to get  1 pet by breed British Shorthair
#  make a for loop
# python already understands that this is an object pet
#  loop pet_shop"pets" pet"breed" 
#  and .append to empty list 15

def get_pets_by_breed(pet_shop, pet_breed):
    pet_im_looking_for = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pet_im_looking_for.append(pet)
    return pet_im_looking_for

# 







