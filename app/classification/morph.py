import pandas as pd

df= pd.read_csv('morph_types.csv')

substituicoes_morfologicas={}
substituicoes_morfologicas_subtipos={}
for i in range(len(df)):
    eng = df['English'].iloc[i]
    pt = df['Portugues'].iloc[i]
    substituicoes_morfologicas[eng]=pt
print(substituicoes_morfologicas)

for i in range(len(df)):
    pt = df['Portugues'].iloc[i]
    if type(pt) is float:
        continue
    tipos_en = df['EnglishTypes'].iloc[i].split(',')
    tipos_pt = df['PortuguesTypes'].iloc[i].split(',')
    min_len=0
    if len(tipos_pt)<len(tipos_en):
        min_len=len(tipos_pt)
    else:
        min_len=len(tipos_en)
    substituicoes_morfologicas_subtipos[pt]={tipos_en[j]:tipos_pt[j] for j in range(min_len)}

# substituicoes_morfologicas={
#     'Case': 'Caso',
#     'Voice': 'Voz',
#     'VerbForm': 'Forma Verbal',
#     'Definite':'Definitude',
#     'Gender':'Gênero',
#     'Number':'Número',
#     'Mood':'Modo Verbal',
#     'PronType':'Tipo de Pronome',
#     'Person':'Pessoa',
#     'Tense':'Tempo Verbal',
#     'Polarity': 'Polaridade',
#     'Degree': 'Grau',
#     'Foreign': 'Estrangeira',
#     'Reflex': 'Reflexivo',
#     'NumType': 'Tipo de Numeral',
# }
# substituicoes_morfologicas_subtipos={'Caso': {'Nom': 'Nominativo', 'Acc': 'Acusativo', 'Dat': 'Dativo'},
#                                      'Voz': {'Pass': 'Passiva'},
#                                      'Forma Verbal': {'Fin': 'Finito', 'Ger': 'Gerúndio', 'Inf': 'Infinitivo', 'Part': 'Particípio'},
#                                      'Definitude':{'Def': 'Definido','Ind': 'Indefinido'},
#                                      'Gênero':{'Fem':'Feminino','Masc':'Masculino', 'Unsp': 'Não Especificado'},
#                                      'Número':{'Sing':'Singular','Plur':'Plural', 'Unsp': 'Não Especificado'},
#                                      'Modo Verbal':{'Ind':'Indicativo','Sub':'Subjuntivo','Imp':'Imperativo', 'Cnd': 'Condicional'},
#                                      'Tipo de Pronome':{'Prs':'Pessoal ou Possessivo', 'Dem':'Demonstrativo', 'Ind':'Indefinido','Int':'Interrogativo',
#                                                      'Rel':'Relativo','Art':'Artigo', 'Neg': 'Negativo', 'Emp': 'Enfático', 'Tot': 'Coletivo'},
#                                      'Pessoa':{'1':'Primeira Pessoa','2':'Segunda Pessoa','3':'Terceira Pessoa'},
#                                      'Tempo Verbal':{'Past':'Pretérito Perfeito','Pres':'Presente','Pqp':'Pretérito Mais-que-perfeito',
#                                                      'Imp':'Pretérito Imperfeito','Fut':'Futuro do Presente'},
#                                      'Polaridade':{'Neg':'Negativa'},
#                                      'Grau': {'Cmp': 'Comparativo'},
#                                      'Estrangeira': {'Yes': 'Sim'},
#                                      'Reflexivo': {'Yes': 'Sim'},
#                                      'Tipo de Numeral': {'Card': 'Cardinal', 'Frac': 'Fração', 'Mult': 'Multiplicativo', 'Ord': 'Ordinal',
#                                                          'Range': 'Amplo', 'Sets': 'Conjunto'}

# }

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
          frase_morph.append([('--', '--')])
    return frase_morph

print(get_morph("eu/PRONOME gosto/VERBO de/PRONOME quem/PRONOME vem/VERBO ./PONTUAÇÃO"))
