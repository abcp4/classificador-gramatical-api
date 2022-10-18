from app.classification.classifier import get_classification
from app.tips import get_tip
from fastapi import FastAPI

app = FastAPI()


@app.get("/get_classification")
def classification(text: str):
    try:
        tagged_words, frase_morph, tokens = get_classification(text)
        return {
            "tagged_words": tagged_words,
            "frase_morph": frase_morph,
            "tokens": tokens
        }
    except:
        return {
            "tagged_words": [],
            "frase_morph": [],
            "tokens": []
        }

@app.get("/get_tip")
def tips():
    return {
        "tip": get_tip()
    }
