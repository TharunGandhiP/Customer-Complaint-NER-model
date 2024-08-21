import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp=en_core_web_sm.load()
doc=nlp("Acer Predator Helios 300 (2024) - 13th Gen Intel Core i9-13900H, 90WHrs Battery - (32 GB/1 TB SSD/Windows 11 Home/8 GB Graphics/NVIDIA GeForce RTX 4070) Gaming Laptop (15.6 Inch, Abyssal Black, 2.50 Kg)")
print([(X.text,X.label_) for X in doc.ents])