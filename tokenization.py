"Tokenization : One of the steps of NLP in which text is getting splits into words, symbols, punctuations, spaces and others elements too."

Import spacy
nlp = spacy.load(‘en’)
Text = "Ram is going to london"
doc = nlp(Text)
tokens = [token.text for token in docx]
print(Tokens)
