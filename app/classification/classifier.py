import spacy
import re

from .constants import COLORS_DICT
from .constants import tag_redirect 
from .substituicoes import substituicoes

def a_classificacao(texto):

    # Carrega o modelo em português
    nlp = spacy.load("pt_core_news_lg")

    # Coloca a primeira palavra em minúsculas
    # necessário para: briguei, dei, etc;
    # precisa corrigir: São, Clara, Santos, etc.
    frase_low_1 = texto[0].lower() + texto[1:]

    # Criação do doc, objeto do Spacy
    doc = nlp(frase_low_1)

    # Fornece as informações que vamos usar em forma de tuplas em lista
    frase_spacy = [(token.orth_, token.pos_, token.morph, token.dep_)
                         for token in doc]

    # Transforma as informações em string (texto)
    frase_spacy_str = ''.join(str(e[0] + '/' + e[1] + '/' + e[3] + ' ') for e in frase_spacy)

    # Aplica as substituições
    for k,v in substituicoes.items():
        frase_spacy_str = re.sub(v[0], v[1], frase_spacy_str)
    frase_classgram = re.sub(r'(?i)((\b\w+|[,.;?!])/\w+\b)/\w+', r'\1', frase_spacy_str)

    return frase_classgram



def get_classification(text, tagset=None):
    text = re.sub("\s+", " ", text)
    annotated_text = a_classificacao(text)
    if annotated_text:
        print('annotated words: ',annotated_text)
        annotated_words = annotated_text.strip().split(" ")
        tagged_words = []
        for word, tag in [w.split("/") for w in annotated_words]:
            if tag in COLORS_DICT:
                tagged_words.append((word, tag, COLORS_DICT[tag])) 
            else:
                if tag in tag_redirect:
                    tag = tag_redirect[tag]
                    tagged_words.append((word, tag, COLORS_DICT[tag])) 
                a=2/0
        return tagged_words      
