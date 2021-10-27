import nltk

tokens = nltk.word_tokenize(“yullo fazendo testes e configurando o nltk”, “portuguese”)
for token in tokens:
    print(“token:”, token)