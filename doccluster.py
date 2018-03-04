"""
Example document clustering for CorkAI Meetup
See: https://github.com/CorkAI/Meetup3

Author: NickGratan
Blog: https://nickgrattandatascience.wordpress.com/
Twitter: @NickGrattan
"""
import string
import os
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt


def getdocumentlist():
    """
    Returns the list of documents
    """
    return [
        'WD-frame-timing-20150120.html',
        'WD-frame-timing-20150206.html',
        'WD-frame-timing-20150424.html',
        'WD-frame-timing-20150624.html',
        'WD-frame-timing-20150717.html',
        'WD-frame-timing-20150916.html',
        'WD-frame-timing-20150924.html',
        'WD-hr-time-2-20150617.html',
        'WD-hr-time-2-20150714.html',
        'WD-hr-time-2-20150717.html',
        'WD-IMPLEMENTING-ATAG20-20150604.html',
        'WD-IMPLEMENTING-ATAG20-20150721.html',
    ]


def readdocs(doclist):
    """
    Tokensise the list of documents
    """
    textdict = {}
    for docfilename in doclist:
        with open("./Data/" + docfilename, 'r', encoding="UTF-8") as txtfile:
            html = txtfile.read()
        # extract text from html, leave tags behind
        soup = BeautifulSoup(html, 'lxml')
        text = soup.text
        textdict[docfilename] = text.lower()
    return textdict


def stemtokens(tokens):
    """
    Stems all tokens using the Porter stemmer, removes punctuation
    """
    stemmer = PorterStemmer()
    stemmed = []
    for token in tokens:
        if token not in string.punctuation:
            stemmed.append(stemmer.stem(token))
    return stemmed


def tokenize(text):
    """
    Tokenizes the given text
    """
    tokens = word_tokenize(text)
    stems = stemtokens(tokens)
    return stems


def vectorize(termsdict):
    """
    Vectorize each document with TF/IDF
    """
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(termsdict.values())
    # tfs is sparse, convert to regular array
    tfs = tfs.toarray()
    vocab = tfidf.get_feature_names()
    return (tfs, vocab)


def hiearchical_cluster(tfs, doclist):
    """
    Computes hiearchical cluster for the TF/IDF vectorization
    """
    linkageres = linkage(tfs, method="ward", metric="euclidean")
    dendrogram(linkageres, orientation="right", labels=doclist)
    plt.tight_layout()
    path = os.path.join(os.getcwd(), 'output_images')
    if not os.path.exists(path):
        os.makedirs(path)
    plt.savefig(os.path.join(path, 'docclust.png'))
    return linkageres


if __name__ == '__main__':
    doclist = getdocumentlist()
    print("Reading documents, tokenizing and vectorizing with TF/IDF")
    texts = readdocs(doclist)
    print("Document List:")
    print(list(texts.keys()))
    tfs, vocab = vectorize(texts)
    print("Vocab size:", len(vocab))
    # Note: Can pass tfs into this method, which will default to Euclidean distance
    linkageres = hiearchical_cluster(tfs, list(texts.keys()))
    print("Created hiearchical cluster plot. See ./output_images/docclust.png")
