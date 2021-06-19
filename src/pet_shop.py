# WRITE YOUR FUNCTIONS HERE

# 1 Function pet_shop name 22

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2 Function total cash 21

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#   Function add cash  20 += adds equal

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# # Function remove cash 19

def add_or_remove_cash(pet_shop, cash_remove):
    pet_shop["admin"]["total_cash"] += cash_remove

# Function get pets sold 18

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Function to increse pets sold by 2 += adds equal

def increase_pets_sold(pet_sold, add_pet):
    pet_sold["admin"]["pets_sold"] += add_pet

# function to get stock count = 6 use len()
#  to return number of characters in the string

def get_stock_count(pets_count):
    return len(pets_count["pets"])






