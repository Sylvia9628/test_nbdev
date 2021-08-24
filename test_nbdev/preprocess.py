# AUTOGENERATED! DO NOT EDIT! File to edit: 00_preprocess.ipynb (unless otherwise specified).

__all__ = ['Preprocess']

# Cell
import spacy
import nltk
import re
from fastcore.test import test_eq
from nltk.corpus import stopwords
from nbdev.showdoc import *

# Cell
class Preprocess:

    def __init__(self, documents): self.documents = documents

    def lemmatize(self):

        "`Returns lemmatized documents with punctuation and stopwords removed`"

        preprocessed_documents = []
        nlp = spacy.load('en_core_web_sm')

        for document in self.documents:
            preprocessed_text = []
            document = re.sub(r'[^\w\d\s\']+', '', document)
            doc = nlp(document)

            for token in doc:
                if token.text not in stopwords.words('english'):
                    preprocessed_text.append(token.lemma_)
            preprocessed_documents.append(preprocessed_text)

        return preprocessed_documents

    def stemming(self):

        "`Returns stemmed documents with punctuation and stopwords removed`"

        preprocessed_documents = []
        stemmer = nltk.stem.SnowballStemmer("english")
        nlp = spacy.load('en_core_web_sm')

        for document in self.documents:
            preprocessed_text = []
            document = re.sub(r'[^\w\d\s\']+', '', document)
            doc = nlp(document)

            for token in doc:
                if token.text not in stopwords.words("english"):
                    preprocessed_text.append(stemmer.stem(token.text))

            preprocessed_documents.append(preprocessed_text)

        return preprocessed_documents

show_doc(Preprocess.lemmatize)
show_doc(Preprocess.stemming)