"Reducing the form of present word to its root form for example: playing will go to play.
lemma_ attribute is getting used in Spacy to perform Lemmatization 
"
import spacy
nlp = spacy.load('en)
text = "Apple is a going to be wordlwide famous"
docx = nlp(text)
lemma =[word.lemma_ for word in docx]
print(lemma)

#OR
import spacy
nlp = spacy.load('en)
text = "Apple is a going to be wordlwide famous"
docx= nlp(text)
lemma =[]
for word in docx:
  lemma.append(word.lemma_)
print(lemma)

