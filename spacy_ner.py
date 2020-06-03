"Entities is piece of information such as persons, locations, organizations about a word or group of words. Identified entities can access by .ents method."
import spacy
nlp = spacy.load('en')
text = "Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[21] Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[22] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago"
docx = nlp(text)
for i in docx.ents:
  print(i.text, i.label_)
