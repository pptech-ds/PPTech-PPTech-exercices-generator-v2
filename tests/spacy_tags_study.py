import argparse
import spacy
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--generate', 
                    help='type of exercise to generate \"conjugaison\" or \"fillblanks\" or \"scramble\"  or \"questions\" or \"all\"', 
                    type=str, 
                    default='NA')
parser.add_argument('--subtitle', 
                    help='source subtitle file to use to generate exercises"', 
                    type=str, 
                    default='NA')
parser.add_argument('--textfile', 
                    help='source text file to use to generate exercises"', 
                    type=str, 
                    default='NA')
args = parser.parse_args()


from modules.fonctions import Fonctions
F = Fonctions()

nlp = spacy.load('en')


def tokenize_sentences(paragraph):

    lemmatizer = WordNetLemmatizer()
    nlp.add_pipe(nlp.create_pipe('merge_noun_chunks'))
    doc = nlp(ensureUtf(paragraph))

    dict_sentences = {}
    dict_sentences['sent'] = []
    dict_sentences['sent_postags'] = []

    for sent in doc.sents:
        doc2 = nlp(sent.text.replace(u'\xa0', u'').replace('-', ' '))  
        dict_sentences['sent'].append(sent.text.replace(u'\xa0', u'').replace('-', ' '))

    return dict_sentences


texte = F.srt_to_text(args.subtitle)
dict_tokenize_sentences = tokenize_sentences(texte)

for i in range(len(dict_tokenize_sentences['sent'])):
    print(dict_tokenize_sentences['sent'][i])