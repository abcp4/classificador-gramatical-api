import pandas as pd
import re

df= pd.read_csv('app/classification/morph_types.csv')
df_excepcionais= pd.read_csv('app/classification/morph_excepcionais.csv')


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

def tratar(sent):
  word,  word_morph = sent.split('/')
  if word.lower() in ["voce", "você"]:
    word_morph = word_morph.replace("Person=3", "Person=2")
  return word, word_morph


def get_morph(frase_spacy_str,frase_spacy_d):
    frase_morph=[]
    print('frase_spacy_str: ',frase_spacy_str)
    print('frase_spacy_d: ',frase_spacy_d)
    word_classes=frase_spacy_d.split(' ')
    frase_spacy_str=frase_spacy_str.strip()
    c=0
    for sent in frase_spacy_str.split(' '):
      print('sent: ',sent)
      c_type = word_classes[c].split('/')[1]
      print('c_type: ',c_type)
      c+=1
      sms=substituicoes_morfologicas_subtipos[c_type]
      sm=substituicoes_morfologicas[c_type]
      print('sms: ',sms)
      print('sm: ',sm)
      
      word,word_morph = tratar(sent)
      #caso transformar
      if c_type =='VERB' or c_type== 'AUX': 
          r_trans = re.search(r'(\b\w+[aei](ria[sm]?\b|rí(eis|amos)\b))',word)
          #adicionar Model verbal como futuro do preterito. Ela geralmente n vem, entao colocar o tense com FutPre
          if r_trans!=None: 
            #adicionar Model verbal como futuro do preterito. Ela geralmente n vem, entao colocar o tense com FutPre
            word_morph+='|Tense=FutPre'


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

                  #Casos excepcionais
                  #caso ocultar
                  if c_type =='PRON' or c_type== 'DET':
                    if sub_terms[0]  == 'Gender':
                      #otimizar, usando dicionario o(1) ao inves de buscas no pandas
                      m=df_excepcionais[(df_excepcionais['String']==word) & (df_excepcionais['CondicaoSub']=='Gender')]
                      print('m: ',m)
                      if len(m)>0:
                        continue
                  
                  #caso transformar
                  if c_type =='VERB' or c_type== 'AUX': 
                    if r_trans!=None:
                      print('Transformar: ',  word)
                      if sub_terms[0]=='Mood':
                        sub_terms[1]='Ind'
                        



                  #caso atribuir
                  m=df_excepcionais[(df_excepcionais['String']==word) & (df_excepcionais['CondicaoSub']==term)]
                  print(m)
                  if len(m)>0:
                      m=m['Atribuir'].iloc[0].split('=')
                      new_terms.append((m[0],m[1]))
                      # if word in df_excepcionais['String']:
                      #   if term in df_excepcionais['Condição']:
                      #       new_terms.append((t1,t2))
                      continue


                  t1 = sm[sub_terms[0]]
                  if sub_terms[1] in sms:
                    t2 = sms[sub_terms[1]]
            new_terms.append((t1,t2))
              
          frase_morph.append(new_terms)
      elif c_type == "PUNCT":
        frase_morph.append([('Sinal de pontuação', '')])
      else:
          frase_morph.append([('Essa palavra não tem detalhamento morfológico.', '')])

    return frase_morph

#print(get_morph("eu/PRONOME gosto/VERBO de/PRONOME quem/PRONOME vem/VERBO ./PONTUAÇÃO"))
