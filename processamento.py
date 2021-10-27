from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

LINGUAGEM = "portuguese"

def iniciar():
    global classificacoes
    global palavras_de_parada

    palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))
    
    classificacoes = []
    for (palavra, classificacao) in floresta.tagged_words():
        if "+" in classificacao:
            classificacao = classificacao[classificacao.index("+") + 1:]
        
        classificacoes.append((palavra.lower(), classificacao))
    

def obter_tokens(texto):
    tokens = word_tokenize(texto, LINGUAGEM)
    
    return tokens

def imprimir_tokens(tokens):
    for token in tokens:
        print(token)

def remover_palavras_de_parada(tokens):
    global palavras_de_parada
    
    tokens_filtrados = []
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)
    
    return tokens_filtrados

def classificar_gramaticamente(tokens):
    global classificacoes
    
    for token in tokens:
        for (palavra, classificacao) in classificacoes:
            if token == palavra:
                print("token '" + token + "' = ", classificacao)
                
                break

def estematizar(tokens):
    stemmer = RSLPStemmer()
    
    for token in tokens:
        print(stemmer.stem(token))

if __name__ == '__main__':
    iniciar()
    
    texto = "Você quer passar o resto da sua vida vendendo água com açúcar ou quer uma chance de mudar o mundo?" # Steve jobs


    #Obtendo os tokens
    print("obtendo o conteudo dos tokens...")
    tokens = obter_tokens(texto) 
    imprimir_tokens(tokens)
    
    #Removendo as palavras de parada
    print("removendo as palavras de parada...")
    tokens = remover_palavras_de_parada(tokens)
    imprimir_tokens(tokens)
    
    #Classificando gramaticamente
    print("classificando gramaticamente...")
    classificar_gramaticamente(tokens)
    
    #Estematizando 
    print("estematizando...")
    estematizar(tokens)
    