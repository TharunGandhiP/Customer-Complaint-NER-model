import spacy
import re
import json
from spacy.tokens import Doc, Span, Token

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Read descriptions from JSON file
with open('laptops.json', 'r') as f:
    data = json.load(f)

descriptions = [item['description'] for item in data['laptops']]

# Define regex patterns
brand_pattern = r"^\b(?:Dell|HP|HCL|Apple|Lenovo|Acer|Asus|MSI)\b"
product_line_pattern = r"^\b(?:Dell Inspiron|Dell XPS|HCL ME|Apple MacBook|Lenovo ThinkPad|Lenovo Yoga|HP Pavilion|HP Spectre|Acer Swift|Acer Predator|Asus ZenBook|Asus VivoBook|Lenovo IdeaPad|Lenovo LOQ|Dell G|HP Victus|HP Omen|Asus ROG|Acer Nitro|Asus TUF|MSI Pulse)\b"
processor_pattern = r"((?:Intel|AMD|Apple)\s(?:Core|Ryzen|M\d+|Xeon)\s\w+-\w+)"
os_pattern = r"(Windows\s\d{2}|macOS|Chrome\sOS)"
model_pattern = r"\((\d{4})\)"
product_type_pattern = r"(Ultrabook|Laptop|2-in-1|Gaming Laptop|Chromebook)"
size_pattern = r"(\d{1,2}\.\d{1,2}\sInch)"
color_pattern = r"\b(?:Black|Silver|Grey|Space Grey|Gold|Natural Silver|Indie Black|Shadow Black|Storm Grey|Nightfall Black|Pure Silver|Pine Grey|Abyssal Black|Slate Grey|Eclipse Gray|Off White|Dark Shadow Grey|Blue)\b"
weight_pattern = r"(\d+\.\d+\sKg)"
ram_pattern = r"(\d+\sGB\sRAM)"
storage_pattern = r"(\d+\s(?:GB|TB)\sSSD)"
graphics_pattern = r"((?:\d+\sGB\sGraphics|NVIDIA\s(?:GeForce|RTX|GTX)\s\w+|AMD\s(?:Radeon|RX)\s\w+|Integrated\sGraphics))"

def extract_entities(text):
    entities = []
    
    # Match and extract entities using regex patterns
    brand_match = re.search(brand_pattern, text, re.IGNORECASE)
    if brand_match:
        entities.append([brand_match.start(), brand_match.end(), 'BRAND'])
    
    product_line_match = re.search(product_line_pattern, text, re.IGNORECASE)
    if product_line_match:
        entities.append([product_line_match.start(), product_line_match.end(), 'PRODUCT_LINE'])
    
    processor_match = re.search(processor_pattern, text, re.IGNORECASE)
    if processor_match:
        entities.append([processor_match.start(), processor_match.end(), 'PROCESSOR'])
    
    os_match = re.search(os_pattern, text, re.IGNORECASE)
    if os_match:
        entities.append([os_match.start(), os_match.end(), 'OS'])
    
    model_match = re.search(model_pattern, text, re.IGNORECASE)
    if model_match:
        year_match = re.search(r'\(\d{4}\)', text, re.IGNORECASE)
        if year_match and year_match.start() == model_match.start():
            entities.append([model_match.start(), model_match.end(), 'YEAR'])
        else:
            entities.append([model_match.start(), model_match.end(), 'MODEL'])
    
    product_type_match = re.search(product_type_pattern, text, re.IGNORECASE)
    if product_type_match:
        entities.append([product_type_match.start(), product_type_match.end(), 'PRODUCT_TYPE'])
    
    size_match = re.search(size_pattern, text, re.IGNORECASE)
    if size_match:
        entities.append([size_match.start(), size_match.end(), 'SIZE'])
    
    color_match = re.search(color_pattern, text, re.IGNORECASE)
    if color_match:
        entities.append([color_match.start(), color_match.end(), 'COLOR'])
    
    weight_match = re.search(weight_pattern, text, re.IGNORECASE)
    if weight_match:
        entities.append([weight_match.start(), weight_match.end(), 'WEIGHT'])
    
    ram_match = re.search(ram_pattern, text, re.IGNORECASE)
    if ram_match:
        entities.append([ram_match.start(), ram_match.end(), 'RAM'])
    
    storage_match = re.search(storage_pattern, text, re.IGNORECASE)
    if storage_match:
        entities.append([storage_match.start(), storage_match.end(), 'STORAGE'])
    
    graphics_match = re.search(graphics_pattern, text, re.IGNORECASE)
    if graphics_match:
        entities.append([graphics_match.start(), graphics_match.end(), 'GRAPHICS'])

    return entities

# Process each description and extract entities
results = []
for desc in descriptions:
    doc = nlp(desc)
    entities = extract_entities(desc)
    results.append([desc, {'entities': entities}])

# Save the output to a JSON file
output_file = 'laptop_entities.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)

print(f"Results saved to {output_file}")
