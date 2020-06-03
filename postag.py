"Process by which grammatical properties are getting assigned to words"
"POS Tagging is done by .tag_ & .pos_ methods"
import spacy
nlp = spacy.load('en')
text = "who are you and how come you came as ram informed us."
docx = nlp(text)
pos_tag =[]
for word in docx:
  pos.tag.append((word,word.pos_,word.tag))
print(pos_tag)
