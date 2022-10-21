from app.classification.classifier import get_classification
from app.tips import get_tip
from fastapi import FastAPI
import datetime


app = FastAPI()


@app.get("/get_classification")
def classification(text: str):
    date_str = str(datetime.date.today())
    try:
        o=open('/home/ubuntu/logs_classificador/'+date_str+'.txt','r')
    except FileNotFoundError:
        o=open('/home/ubuntu/logs_classificador/'+date_str+'.txt','w')
    o.write(text+'\n')
    try:
        tagged_words, frase_morph, tokens = get_classification(text)
        o.write('class: '+str(tagged_words)+'\n')
        o.close()
        return {
            "tagged_words": tagged_words,
            "frase_morph": frase_morph,
            "tokens": tokens
        }
    except Exception as e:
        o.write('ERROR: '+str(e)+'\n')
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
        o.close()
        return d

@app.get("/get_tip")
def tips():
    return {
        "tip": get_tip()
    }
