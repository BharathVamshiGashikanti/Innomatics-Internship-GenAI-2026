# List of names with extra spaces and different letter cases
names = [" Alice ", "bob", " CHARLIE "]

# Create an empty list to store cleaned names
cleaned_names = []

# Loop through each name in the list
for name in names:
    # Remove extra spaces using strip()
    name = name.strip()
    
    # Convert the name to lowercase using lower()
    name = name.lower()
    
    # Add the cleaned name to the new list
    cleaned_names.append(name)

# Print the cleaned list
print("Cleaned Names List:", cleaned_names)
