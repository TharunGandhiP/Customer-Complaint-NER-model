import spacy

# Load your trained NER model
trained_nlp = spacy.load("output/model-best")

# Input text from the user
text = input("Enter input Text: ")

# Process the text with the trained NER model
doc = trained_nlp(text)

# Extract and print entities
for ent in doc.ents:
    print(ent.text, ent.label_)

# If no entities are found, print a message
if len(doc.ents) == 0:
    print("No entities found.")
