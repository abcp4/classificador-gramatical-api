from math import sqrt
import re
import datetime
import random
import sys

import numpy as np

import torch

from .pos_tagger.test import accuracy, tagged_samples
from .pos_tagger.train import train
from .pos_tagger.utils import send_output, load_datasets
from .pos_tagger.Dataset import build_char_dict
from .pos_tagger.parameters import *

from .models.ModelCharBiLSTM import CharBILSTM
from .models.ModelWordBiLSTM import WordBILSTM
from .models.ModelPOSTagger import POSTagger

#from .substitution import substituicoes
from .substituicoes import substituicoes

torch.set_printoptions(threshold=10000)

# Seting device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# dataset building
datasets = load_datasets()

# builds char-id table
char2id, id2char = build_char_dict(datasets)

# converts text to id from chars
for dataset in datasets:
    dataset.prepare(char2id)

# prints the datasets details
for dataset in datasets:
  send_output(str(dataset), 1)

WORD_EMBEDDING_DIM = 350
CHAR_EMBEDDING_DIM = 70
BILSTM_SIZE = 200

# building model
pos_model = POSTagger(CharBILSTM(CHAR_EMBEDDING_DIM, WORD_EMBEDDING_DIM, char2id),
                      WordBILSTM(WORD_EMBEDDING_DIM),
                      WordBILSTM(WORD_EMBEDDING_DIM),
                      BILSTM_SIZE, datasets)
pos_model.to(device)

# prints model
send_output(str(pos_model), 1)

# Loading the model with best loss on the validation
# try:
pos_model.load_state_dict(torch.load('/home/ubuntu/classificador-gramatical-st/app/classification/model.pt', map_location=device))


def predict(s,dataset_id):
    data=[s.split(' ')]
    inputs = [[torch.LongTensor([char2id.get(c, 1) for c in token]) for token in sample] for sample in data]
    # # Setting the input and the target (seding to GPU if needed)
    # inputs = [[word.to(device) for word in sample] for sample in inputs]
    output = pos_model(inputs)

    # convert output probabilities to predicted class
    dataset_name=['Macmorpho','Bosque','GSD','Linguateca']#Linguateca,Macmorpho,GSD,Bosque
    _, pred = torch.max(output[dataset_name[dataset_id]], 2)

    # Formatando vetor
    pred = pred.view(1, -1).cpu().numpy()
    for p in pred[0]:
      print(datasets[dataset_id].id2tag[p])


    frase_tags=''
    for frase in data:
      for i in range(len(frase)):
        frase_tags+=frase[i]+'/'+datasets[dataset_id].id2tag[pred[0][i]]+' '
    frase_tags=frase_tags[:-1]

    for k,v in substituicoes.items():
        frase_tags = re.sub(v[0], v[1], frase_tags)
    frase_classgram = re.sub(r'(?i)((\b\w+|[,.;?!])/\w+\b)/\w+', r'\1', frase_tags)
    print(frase_classgram)
    return frase_classgram

