import json

# Define the input and output file paths
input_file = 'laptops.txt'  # Replace with your input file name
output_file = 'laptops.json'

# Initialize the list to hold the laptop descriptions
laptops = []

# Read the input file and process each line
with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line:  # Ensure the line is not empty
            laptop_entry = {
                "description": line
            }
            laptops.append(laptop_entry)

# Prepare the final JSON structure
data = {
    "laptops": laptops
}

# Write the JSON data to the output file
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data successfully written to {output_file}")
