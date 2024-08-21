import spacy
import json

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Read descriptions from JSON file
with open('laptops.json', 'r') as f:
    data = json.load(f)

descriptions = [item['description'] for item in data['laptops']]

# Process each description and extract entities using SpaCy's built-in NER
results = []
for desc in descriptions:
    doc = nlp(desc)
    entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    results.append([desc, {'entities': entities}])

# Save the output to a JSON file
output_file = 'laptop_entities_spacy.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)

print(f"Results saved to {output_file}")
