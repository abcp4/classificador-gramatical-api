import pandas as pd

df= pd.read_csv('app/classification/morph_types.csv')

substituicoes_morfologicas={}
substituicoes_morfologicas_subtipos={}
substituicoes_morfologicas_subtipos={}
for i in range(len(df)):
    eng = df['English'].iloc[i]
    pt = df['Portugues'].iloc[i]
    if type(pt) is float:
        continue
    if eng.isupper():
        substituicoes_morfologicas_subtipos[eng]={}
        substituicoes_morfologicas[eng]={}

    # substituicoes_morfologicas[eng]=pt
last_topic=''
for i in range(len(df)):
    pt = df['Portugues'].iloc[i]
    eng = df['English'].iloc[i]
    if type(pt) is float:
        continue
    
    tipos_en = df['EnglishTypes'].iloc[i].split(',')
    tipos_pt = df['PortuguesTypes'].iloc[i].split(',')
    min_len=0
    if len(tipos_pt)<len(tipos_en):
        min_len=len(tipos_pt)
    else:
        min_len=len(tipos_en)

    if eng.isupper():
    	last_topic=eng
    	continue
    else:
        substituicoes_morfologicas[last_topic][eng]=pt
    if last_topic not in substituicoes_morfologicas_subtipos:
    	substituicoes_morfologicas_subtipos[last_topic]={tipos_en[j].strip():tipos_pt[j].strip() for j in range(min_len)}
    else:
    	substituicoes_morfologicas_subtipos[last_topic].update({tipos_en[j].strip():tipos_pt[j].strip() for j in range(min_len)})

    	
    # substituicoes_morfologicas_subtipos[pt]={tipos_en[j].strip():tipos_pt[j].strip() for j in range(min_len)}
    
print('substituicoes_morfologicas: ',substituicoes_morfologicas)
print('substituicoes_morfologicas_subtipos: ',substituicoes_morfologicas_subtipos)


def get_morph(frase_spacy_str,frase_spacy_d):
    frase_morph=[]
    print('frase_spacy_d: ',frase_spacy_d)
    c_type = frase_spacy_d.split('/')[1]
    sms=substituicoes_morfologicas_subtipos[c_type]
    sm=substituicoes_morfologicas[c_type]
    print('sms: ',sms)
    print('sm: ',sm)
    
    frase_spacy_str=frase_spacy_str.strip()

    for sent in frase_spacy_str.split(' '):
      print('sent: ',sent)
      word,word_morph = sent.split('/')
      if len(word_morph)>1:
        terms =word_morph.split('|')
        new_terms=[]

        if len(terms)>1:
          for term in terms :
            sub_terms = term.split('=')
            t1=''
            t2=''
            if len(sub_terms)>1:
              if sub_terms[0] in sm:
                  t1 = sm[sub_terms[0]]
                  if sub_terms[1] in sms:
                    t2 = sms[sub_terms[1]]
            new_terms.append((t1,t2))
              
          frase_morph.append(new_terms)
      else:
          frase_morph.append([('--', '--')])
    return frase_morph

#print(get_morph("eu/PRONOME gosto/VERBO de/PRONOME quem/PRONOME vem/VERBO ./PONTUAÇÃO"))
