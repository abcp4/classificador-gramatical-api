
substituicoes_morfologicas={
    'Definite':'Artigo',
    'Gender':'Gênero',
    'Number':'Numeral',
    'Mood':'Modo Verbal',
    'PronType':'Tipo Pronome',
    'Person':'Pessoa',
    'Tense':'Tempo Verbal',
    'Polarity': 'Polaridade'
}
substituicoes_morfologicas_subtipos={'Artigo':{'Def': 'definido','Ind': 'Indefinido'},
                                     'Gênero':{'Fem':'Feminino','Masc':'Masculino'},
                                     'Numeral':{'Sing':'Singular','Plur':'Plural'},
                                     'Modo Verbal':{'Ind':'Indicativo','Sub':'Subjuntivo','Imp':'Imperativo'},
                                     'Tipo Pronome':{'Prs':'Pessoal/Posessivo', 'Dem':'Demonstrativo', 'Neg':'Indefinido','Int':'Interrogativo',
                                                     'Rel':'Relativo','Inf':'Infinitivo','Fin':'Finitivo','Art':'Artigo'},
                                     'Pessoa':{'1':'Primeira Pessoa','2':'Segunda Pessoa','3':'Terceira Pessoa'},
                                     'Tempo Verbal':{'Past':'Pretérito Perfeito','Pres':'Presente','Pqp':'Pretérito mais-que-perfeito',
                                                     'Imp':'Pretérito Imperfeito','Fut':'Futuro do Presente','Fin':'Futuro do Pretérito'},
                                     "Polaridade":{'Neg':'Negativo'},

}

def get_morph(frase_spacy_str):
    frase_morph=[]
    frase_spacy_str=frase_spacy_str.strip()
    for sent in frase_spacy_str.split(' '):
      # print('sent: ',sent)
      word,word_morph = sent.split('/')
      if len(word_morph)>1:
        terms =word_morph.split('|')
        new_terms=[]

        if len(terms)>1:
          for term in terms :
            sub_terms = term.split('=')
            if len(sub_terms)>1:
              if sub_terms[0] in substituicoes_morfologicas:
                  sub_terms[0] = substituicoes_morfologicas[sub_terms[0]]
                  if sub_terms[1] in substituicoes_morfologicas_subtipos[sub_terms[0]]:
                    sub_terms[1] = substituicoes_morfologicas_subtipos[sub_terms[0]][sub_terms[1]]
              new_terms.append((sub_terms[0],sub_terms[1]))
          frase_morph.append(new_terms)
      else:
          frase_morph.append('Desconhecido')
      return frase_morph
