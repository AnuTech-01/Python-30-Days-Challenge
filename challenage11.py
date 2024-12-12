#CHALLENAGE 11

#Python String Formatting

# Example Data
name = "ANU JANGID"
age = 19
department = "Marketing"
salary = 27000.56
is_manager = True

# 1. Old style string formatting (using %):
print("Old style formatting:")
print("Employee Name: %s" % name)
print("Age: %d" % age)
print("Department: %s" % department)
print("Salary: %.2f" % salary)
print("Is Manager: %s" % ("Yes" if is_manager else "No"))
print()

# 2. Using str.format() method:
print("Using str.format() method:")
print("Employee Name: {}".format(name))
print("Age: {}".format(age))
print("Department: {}".format(department))
print("Salary: {:.2f}".format(salary))
print("Is Manager: {}".format("Yes" if is_manager else "No"))
print()

# 3. Using f-strings (formatted string literals):
print("Using f-strings:")
print(f"Employee Name: {name}")
print(f"Age: {age}")
print(f"Department: {department}")
print(f"Salary: {salary:.2f}")
print(f"Is Manager: {'Yes' if is_manager else 'No'}")
print()

# Extra: Formatting with alignment and width:
print("Formatted with alignment and width:")
print(f"{'Employee Name':<20}: {name}")
print(f"{'Age':<20}: {age}")
print(f"{'Department':<20}: {department}")
print(f"{'Salary':<20}: {salary:.2f}")
print(f"{'Is Manager':<20}: {'Yes' if is_manager else 'No'}")
