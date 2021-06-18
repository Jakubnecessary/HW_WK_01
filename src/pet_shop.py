# WRITE YOUR FUNCTIONS HERE

# 1 Function pet_shop name 22

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2 Function total cash 21

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#   Function add cash  20

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# # Function remove cash 19

def add_or_remove_cash(pet_shop, cash_remove):
    pet_shop["admin"]["total_cash"] += cash_remove

# Function fet pefs sold 18

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]





