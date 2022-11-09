from app.classification.classifier_sem_morph import get_classification
from app.tips import get_tip
from fastapi import FastAPI
import datetime


app = FastAPI()


@app.get("/get_classification")
def classification(text: str):
    date_str = str(datetime.date.today())
    try:
        tagged_words, tokens = get_classification(text)
        return {
            "tagged_words": tagged_words,
            "frase_morph": [],
            "tokens": tokens
        }
    except Exception as e:
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
        return d

@app.get("/get_tip")
def tips():
    return {
        "tip": get_tip()
    }
