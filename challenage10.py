# CHALLENAGE 10

# python scope

# 1. Local Scope:
def local_scope_example():
    x = 24  # local variable
    print("Inside function, x:", x)

local_scope_example()
# print(x)  # This would cause an error because x is not defined in the global scope

'''# 2. Globle Scope:
x = 20  # global variable

def global_scope_example():
    print("Inside function, x:", x)

global_scope_example()
print("Outside function, x:", x)

# 3. Nonscole Scope:
def outer_function():
    x = 100  # local to outer_function

    def inner_function():
        nonlocal x  # Refers to x from the outer_function
        x = 200  # Modify x in the nonlocal scope
        print("Inside inner_function, x:", x)

    inner_function()
    print("Inside outer_function, x:", x)

outer_function()'''

