from app.classification.classifier import get_classification
from app.tips import get_tip
from fastapi import FastAPI
import datetime
from .sintatico_simples.analise_sintatica import processa


app = FastAPI()
# base_path='/home/ubuntu/logs_classificador/'
base_path='/home/miu/Projects/NLP/gramatica/'


@app.get("/get_sintatico") 
def sintatico(text: str):
    print('get_sintatico:',text)
    result = processa(text)
    print('result:',result)
    return result

@app.get("/get_classification")
def classification(text: str):
    date_str = str(datetime.date.today())
    # try:
    #    o=open(base_path+date_str+'.txt','a')
    # except FileNotFoundError:
    #    o=open(base_path+date_str+'.txt','w')
    # o.write(str(text)+'\n')
    try:
        tagged_words, frase_morph, tokens = get_classification(text)
        # o.write('class: '+str(tagged_words)+'\n')
        # o.close()
        return {
            "tagged_words": tagged_words,
            "frase_morph": frase_morph,
            "tokens": tokens
        }
    except Exception as e:
        print('ERROR: ',e)
        # o.write('ERROR: '+str(e)+'\n')
        d={
              "tagged_words": [
                [
                  "erro","SUBSTANTIVO","#fd2c2c","white"
                ],
                " "
              ],
              "frase_morph": [
                [
                  ["Gênero","Masculino"],
                  ["Número","Singular"
                  ]
                ]
              ],
              "tokens": [
                "erro"
              ]
            }
        # o.close()
        return d


 
@app.get("/get_tip")
def  tips():
    return {}
    # return {
    #     "tip": get_tip()
    # }
