from sklearn.model_selection import train_test_split
import json

# Load the labeled data
with open('processed_laptop_complaints.json', 'r') as f:
    labeled_data = json.load(f)

# Split the data into training and validation sets
train_data, val_data = train_test_split(labeled_data, test_size=0.3, random_state=42)

# Save the split datasets
with open('data/train.json', 'w') as f:
    json.dump(train_data, f, indent=4)

with open('data/valid.json', 'w') as f:
    json.dump(val_data, f, indent=4)
