import spacy
import re

from .constants import BK_COLOR_DICT, COLOR_DICT, TRANSLATION_DICT
from .constants import tag_redirect 
from .substituicoes import substituicoes
# from .morph import get_morph

#from .multiple_classification import predict

tags={"Bosque":0,"GSD":1, "Linguateca":2, "Macmorpho":3}
def a_classificacao(texto):

    # Carrega o modelo em português
    nlp = spacy.load("pt_core_news_md")

    # Coloca a primeira palavra em minúsculas
    # necessário para: briguei, dei, etc;
    # precisa corrigir: São, Clara, Santos, etc.
    # frase_low_1 = texto[0].lower() + texto[1:]

    # Criação do doc, objeto do Spacy
    doc = nlp(texto)

    # Fornece as informações que vamos usar em forma de tuplas em lista
    frase_spacy = [(token.orth_, token.pos_, token.morph, token.dep_)
                         for token in doc]

    # Transforma as informações em string (texto)
    frase_spacy_str = ''.join(str(e[0] + '/' + e[1] + '/' + e[3] + ' ') for e in frase_spacy)
    
    print('frase spacy: ',frase_spacy_str)

    # Aplica as substituições
    for k,v in substituicoes.items():
        frase_spacy_str = re.sub(v[0], v[1], frase_spacy_str)
    frase_classgram = re.sub(r'(?i)((\b\w+|[,.;?!])/\w+\b)/\w+', r'\1', frase_spacy_str)
    

    # Processar informações morfologicas
    #provisorio: duas chamadas no modelo, essa com lower pq uppercase ta atrapalhando na previsao
    doc = nlp(texto.lower())
    frase_spacy = [(token.orth_, token.pos_, token.morph, token.dep_)
                         for token in doc]
    frase_spacy_d = ''.join(str(e[0].lower() + '/' + e[1] + '/' + e[3] + ' ') for e in frase_spacy)
    frase_spacy_str = ''.join(str(e[0].lower() + '/' + str(e[2]) + ' ') for e in frase_spacy)
    # frase_morph=get_morph(frase_spacy_str,frase_spacy_d)

    # return frase_classgram,frase_morph
    return frase_classgram




def get_classification(text, tag_text='Spacy'):
    text = re.sub("\s+", " ", text)
    # annotated_text,frase_morph = a_classificacao(text)
    annotated_text = a_classificacao(text)

    if annotated_text:
        print('annotated words: ',annotated_text)
        # print('morph: ',frase_morph)
        annotated_words = annotated_text.strip().split(" ")
        tagged_words = []
        # frase_morph2 = []
        tokens = []
        for index, (word, tag) in enumerate([w.split("/") for w in annotated_words]):
            if tag in BK_COLOR_DICT:
                tagged_words.append((word, tag, BK_COLOR_DICT[tag], COLOR_DICT[tag])) 
            else:
                if tag in tag_redirect:
                    tag = tag_redirect[tag]
                    tagged_words.append((word, tag, BK_COLOR_DICT[tag], COLOR_DICT[tag])) 
                else:
                    tagged_words.append(word)
            tokens.append(word)
            tagged_words.append(" ")
            # frase_morph2.append(frase_morph[index])
            '''
            if "#" in tag:
                #nome_classificao, _ = frase_morph[-1]
                tipo = tag.title().replace("#", "+")
                #if nome_classificao == "Tipo":
                #    frase_morph2[index][-1] = ("Tipo", tipo)
                #else:
                frase_morph2[index].append(("Tipo", tipo))
            '''
        # return tagged_words, frase_morph2, tokens
        return tagged_words, tokens 

