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
#  and .append to empty list 15/14 both passed

def get_pets_by_breed(pet_shop, pet_breed):
    pet_breed_im_looking_for = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pet_breed_im_looking_for.append(pet)
    return pet_breed_im_looking_for

# funnction find pet 
# by name "Arthur" in 
# pet_shop["pets"]["name"]      13/12 works for both

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# function  remove by name
#  should remove "Arthur"
# .remove           11

def remove_pet_by_name(pet_shop, pet_name):
    pet_to_remove = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(pet_to_remove)
    

# function to add pet to stock
# should add new one
# same as before
# but this time .append        10

def add_pet_to_stock(pet_shop, new_pet):
    pet_to_add = find_pet_by_name(pet_shop, new_pet)
    pet_shop["pets"].append(pet_to_add)


#  function to get customer cash 
# (just return value of 100 for 1 customer)    9

def get_customer_cash(customers):
    return customers["cash"]


# function to remove customer cash 
# by 100/from1000 to 900     8

def remove_customer_cash(customers, remove_cash):
    customers["cash"] -= remove_cash

# function to get customer pet count
# this one will return 0 
# as lists of "pets" are empty 
# just return len of        7

def get_customer_pet_count(customers):
    return len(customers["pets"])

