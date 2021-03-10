import re
import math
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    vetor_assinatura = [(i - j) for i, j in zip(as_a, as_b)]
    grau_similaridade = 0
    for i in range(len(vetor_assinatura)):
        grau_similaridade += abs(vetor_assinatura[i])
    
    return grau_similaridade / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    tot_frases = [] # Array que mostra o tatal de frases
    tot_palavras = [] # Array que mostra o total de palavras
    tot_caracteres = 0 
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        tot_frases.extend(novas_frases)
        
    for fr in tot_frases:
        novas_palavras = separa_palavras(fr)
        tot_palavras.extend(novas_palavras)
        
    #Total de caracteres no texto
    for i in tot_palavras:
        tot_caracteres += len(i)
        
    #1-Tamanho médio das palavras
    tamanho_medio_palavras = tot_caracteres / len(tot_palavras)
    
    #2-Relação Type-Token
    relação_type_token = n_palavras_diferentes(tot_palavras) / len(tot_palavras)

    #3-Razão Hapax Legomana
    razao_hapax_legomana = n_palavras_unicas(tot_palavras) / len(tot_palavras)

    #4-Tamanho médio de sentença
    tamanho_medio_sentenca = len(texto) / len(sentencas) -1

    #5-Complexidade de sentença
    complexidade_sentenca = len(tot_frases) / len(sentencas)

    #6-Tamanho médio de frase
    tamanho_medio_frase = len(texto) / len(tot_frases) - 1
    
    return [tamanho_medio_palavras, relação_type_token, razao_hapax_legomana,
           tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]       
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_novo = 9999999
    for i in range(len(textos)):
        assinatura = calcula_assinatura(textos[i])
        grau_similariedade = compara_assinatura(assinatura, ass_cp)
        if (grau_similariedade < grau_novo):
            grau_novo = grau_similariedade
            infectado = i + 1
            
    return infectado

ass_cp = le_assinatura()
textos = le_textos()
print("O autor do texto", avalia_textos(textos, ass_cp), "está infectado com COH-PIAH")