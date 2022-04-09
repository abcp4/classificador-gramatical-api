from app.classification.classifier import get_classification

from fastapi import FastAPI

app = FastAPI()


@app.get("/get_classification/{text}")
def classification(text: str):
    tagged_words, frase_morph, tokens = get_classification(text)
    return {
        "tagged_words": tagged_words,
        "frase_morph": frase_morph,
        "tokens": tokens
    }