import string
import math

vocabulario = {}
idf = {}
vecDoc = {}

def addTerm(id,term):
    if term in vocabulario: # verifica se o termo esta no vocabulario
        listaInvertida = vocabulario[term] # se sim, recupera a lista invertida
        if id in listaInvertida:           # verifica se o termo ja foi mencionado no mesmo documento
            listaInvertida[id] += 1
        else:                              # se nao tiver na lista invertida, adiciona o termo com frequencia 1
            listaInvertida[id] = 1
    else:
        vocabulario[term] = {id:1}         # caso nao esteja no vocabulario, adiciona o termo e inicializa sua lista invertida

def criaVocabulario(id, terms):
    for term in terms:
        addTerm(id,term)

def calculaIdf(N):
    for term, listaInvertida in vocabulario.items():
        n = len(listaInvertida)
        termIdf = round(math.log10(N/float(n)), 2)
        idf[term] = termIdf

def calculaPesos(docs):
    for doc in docs:
        pass

def indexador():
    # colecao de documentos
    docs = {
                1: "To do is to be. To be is to do.",
                2: "To be or not to be. I am what I am.",
                3: "I think therefore I am. Do be do be do.",
                4: "Do do do, da da da. Let it be, let it be."
            }

    for id, doc in docs.items():
        doc = doc.lower() # todos os caracteres em minusculo
        doc = doc.translate(None, string.punctuation) #remove todas as pontuacoes
        terms = doc.split() # separar os termos do documentos
        criaVocabulario(id,terms) #adiciona vocabulario

    calculaIdf(len(docs))
    calculaPesos(docs)

def main():
    indexador()

if __name__ == '__main__':
    main()