import spacy
import re

from .constants import BK_COLOR_DICT, COLOR_DICT, TRANSLATION_DICT
from .constants import tag_redirect 
from .substituicoes import substituicoes

from .multiple_classification import predict

tags={"Bosque":0,"GSD":1, "Linguateca":2, "Macmorpho":3}
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
    print('frase spacy: ',frase_spacy_str)

    # Aplica as substituições
    for k,v in substituicoes.items():
        frase_spacy_str = re.sub(v[0], v[1], frase_spacy_str)
    frase_classgram = re.sub(r'(?i)((\b\w+|[,.;?!])/\w+\b)/\w+', r'\1', frase_spacy_str)

    return frase_classgram



def get_classification(text, tag_text='Spacy'):
    text = re.sub("\s+", " ", text)
    if tag_text == 'Spacy' :
        print('spacy')
        annotated_text = a_classificacao(text)
    else:
        print('outras anotacoes')
        tag_id = tags[tag_text]
        annotated_text = predict(text,tag_id)
    if annotated_text:
        print('annotated words: ',annotated_text)
        annotated_words = annotated_text.strip().split(" ")
        tagged_words = []
        for word, tag in [w.split("/")[:2] for w in annotated_words]:
            if tag in TRANSLATION_DICT:
                tag = TRANSLATION_DICT[tag]

            if tag in BK_COLOR_DICT:
                tagged_words.append((word, tag, BK_COLOR_DICT[tag], COLOR_DICT[tag])) 
            else:
                if tag in tag_redirect:
                    tag = tag_redirect[tag]
                    tagged_words.append((word, tag, BK_COLOR_DICT[tag], COLOR_DICT[tag])) 
                else:
                    tagged_words.append(word)
            tagged_words.append(" ")
        return tagged_words      
