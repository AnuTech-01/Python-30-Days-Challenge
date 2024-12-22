#CHALLENAGE 21

#Python Boolean

# Boolean logic with 'and', 'or', and 'not'
is_anu = True
is_divya = False

# 'and' operator: Both conditions must be True
if is_anu and is_divya:
    print("Perfect weather for a walk!")
else:
    print("Not perfect for a walk.")

# 'or' operator: At least one condition must be True
if is_anu or is_divya:
    print("Good weather for outdoor activities.")

# 'not' operator: Reverses the boolean value
if not is_divya:
    print("It’s a bit chilly!")
