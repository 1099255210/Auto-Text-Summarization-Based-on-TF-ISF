from gensim.models.keyedvectors import BaseKeyedVectors
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from typing import Iterable, List
from sklearn.decomposition import PCA
import numpy as np
import datadef

reloaded_word_vectors = ''

Sentence = List[str]

def word_vec(wv: BaseKeyedVectors, s: str):
    try:
        return wv.get_vector(s)
    except KeyError:
        return np.zeros(wv.vector_size)


class SentenceVec:
    wv: BaseKeyedVectors
    u: np.array
    a: float

    def __init__(self, sentences: Iterable[Sentence], wv: BaseKeyedVectors, a: float = 1e-3):
        self.wv = wv
        self.a = a
        embedding_size = wv.vector_size
        sentence_set = []
        for sentence in sentences:
            vs = self.weighted_average(sentence)
            # add to our existing re-calculated set of sentences
            sentence_set.append(vs)

        # calculate PCA of this sentence set
        pca = PCA(n_components=embedding_size)
        pca.fit(np.array(sentence_set))
        u = pca.components_[0]  # the PCA vector
        u = np.multiply(u, np.transpose(u))  # u x uT

        # pad the vector?  (occurs if we have less sentences than embeddings_size)
        if len(u) < embedding_size:
            for _ in range(embedding_size - len(u)):
                # add needed extension for multiplication below
                u = np.append(u, 0)

        # resulting sentence vectors, vs = vs -u x uT x vs
        sentence_vecs = []
        for vs in sentence_set:
            sub = np.multiply(u, vs)
            sentence_vecs.append(np.subtract(vs, sub))

        self.u = u
        self.vec = sentence_vecs

    def feature(self, sentence: Sentence):
        vs = self.weighted_average(sentence)
        return vs - vs * self.u

    def get_word_frequency(self, s) -> float:
        vocab = self.wv.vocab.get(s)
        return vocab.count / 10000000 if vocab else 0

    def weighted_average(self, sentence: Sentence):
        dim = self.wv.vector_size
        a = self.a
        # add all word2vec values into one vector for the sentence
        vs = np.zeros(dim)
        for word in sentence:
            # smooth inverse frequency, SIF
            a_value = a / (a + self.get_word_frequency(word))
            # vs += sif * word_vector
            vs = np.add(vs, np.multiply(a_value, word_vec(self.wv, word)))

        vs = np.divide(vs, len(sentence))  # weighted average
        return vs
    
    
def traininit():
    global reloaded_word_vectors
    if reloaded_word_vectors == '':
        reloaded_word_vectors = KeyedVectors.load_word2vec_format('./glove.6B.50d.word2vec.txt', binary=False)


def train(senset:datadef.SentenseSet) -> List[np.ndarray]:
  
    r'''
    Do traininit() first.
    '''
    
    global reloaded_word_vectors
    trainlist = senset.getOriginWordlist()
    
    
    senten = trainlist
    allsen = []
    
    for sentense in senset.sentenselist:
        for word in sentense.wordlist:
            allsen.append(word)
    senten.append(allsen)

    vec = SentenceVec(senten, reloaded_word_vectors, 1e-3)
    
    return vec.vec


def gloveToGensim():
    from gensim.scripts.glove2word2vec import glove2word2vec

    glove_input_file = './glove.6B.50d.txt'
    word2vec_output_file = './glove.6B.50d.word2vec.txt'
    (count, dimensions) = glove2word2vec(glove_input_file, word2vec_output_file)
    print(count, '\n', dimensions)

if __name__ == '__main__':
    gloveToGensim()
    