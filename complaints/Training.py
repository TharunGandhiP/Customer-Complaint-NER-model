import spacy
import re
import json

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Load complaints from JSON file
with open('laptop_complaints.json', 'r') as f:
    complaints = json.load(f)

# Define regex patterns for entities
patterns = {
    "BRAND": r"\b(Dell|Lenovo|HP|MacBook|Acer|Asus|MSI|Toshiba|Alienware|Samsung|Huawei|Sony|Gigabyte|Razer|Fujitsu|Panasonic|LG|Microsoft|Vaio|Clevo|Xiaomi|Chuwi|Gateway|Dynabook|Medion|Bmax|JUMPER|Voyo|iLife|Teclast|Onda|Fusion5|Smartbook|NuVision|Nextbook|Cube|Azpen|Ematic|RCA|Brydge|Venturer|Avita|Pinebook|Eve|Alldocube|T-bao|I-Life|Micromax|InFocus|Datawind)\b",
    "PROCESSOR": r"\b(Intel Core i[3579]|AMD Ryzen [3579]|M1 chip|NVIDIA GeForce RTX 3080)\b",
    "ISSUE": r"(screen flickers|battery life is terrible|overheating|touchpad is unresponsive|random shutdowns|keyboard has stopped working|fan is making a loud noise|Wi-Fi connection keeps dropping|graphics card issues|speakers are very low in volume|can't seem to get.*to charge properly|USB ports are not working|screen has dead pixels|issues with the 1080p webcam|Ethernet port is malfunctioning|broken hinge|keyboard is flickering|audio jack is not detecting headphones|trackpad is stuck|BIOS is corrupted|fingerprint sensor is unresponsive|screen is not turning on|DVD drive is not reading discs|SSD is failing|Bluetooth is not connecting|running very slow|hinge is loose|battery is draining too quickly|fan is making a grinding noise|keyboard is missing keys|screen is flickering|battery swelled up|webcam is not working|is not booting up|screen is cracked|touch screen is unresponsive|touchpad is not clicking|battery life is very short|charger is overheating|screen brightness is too low|speakers are crackling|screen resolution is poor|Wi-Fi is not working|keyboard is not connecting|USB-C port is loose|hinge is broken|backlight is flickering|touchpad is too sensitive|battery is not charging|screen has vertical lines)"
}

# Precompile regex patterns for performance
compiled_patterns = {label: re.compile(pattern, re.IGNORECASE) for label, pattern in patterns.items()}

# Function to extract entities
def extract_entities(text):
    doc = nlp(text)
    entities = []

    for label, pattern in compiled_patterns.items():
        for match in pattern.finditer(text):
            span = doc.char_span(match.start(), match.end(), label=label)
            if span is not None:
                entities.append([span.start_char, span.end_char, span.label_])
    
    return entities

# Process each complaint and extract entities
processed_complaints = []

for complaint in complaints:
    text = complaint["complaint"]
    entities = extract_entities(text)
    processed_complaints.append([
        text,
        {"entities": entities}
    ])

# Save the processed complaints to a JSON file
output_file = 'processed_laptop_complaints.json'
with open(output_file, 'w') as f:
    json.dump(processed_complaints, f, indent=4)

print(f"Processed complaints saved to {output_file}")
