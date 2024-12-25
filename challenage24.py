#CHALLENAGE 24

#Python JSON

import json

# Create a Python dictionary (data)
data = {
    "name": "Anu",
    "age": 19,
    "city": "Sikar",
    "is_student": True,
    "courses": ["BCA"]
}

# Convert Python dictionary to JSON (serialization)
json_data = json.dumps(data, indent=4)
print("JSON Data:")
print(json_data)

# Convert JSON back to Python dictionary (deserialization)
parsed_data = json.loads(json_data)

# Access data from parsed JSON
print("\nParsed Data:")
print(f"Name: {parsed_data['name']}")
print(f"Age: {parsed_data['age']}")
print(f"City: {parsed_data['city']}")

# Modify a value in the dictionary and serialize it again
parsed_data['age'] = 19
modified_json_data = json.dumps(parsed_data, indent=4)

print("\nModified JSON Data:")
print(modified_json_data)

# Saving the JSON to a file
with open("data.json", "w") as json_file:
    json.dump(parsed_data, json_file, indent=4)

print("\nJSON data has been saved to 'data.json'.")
