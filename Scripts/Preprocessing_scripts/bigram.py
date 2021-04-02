
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.collocations import *
import pickle
stop_words = stopwords.words('english')
import json


def print_bigrams_from_json(bigrams_json):
    with open (bigrams_json, 'rb') as fp:
        bigrams = json.load(fp)
    count = 0
    for bigram in bigrams.items():
        print(bigram)
        count += 1
        if count % 10 == 0:
                input()

def get_bigrams_from_corpus(corpus_json):
    with open(corpus_json, 'rb') as fp:
        corpus_list = pickle.load(fp)

    filtered_words = []
    for sentence in corpus_list[0:]:
        tokens = nltk.tokenize.word_tokenize(sentence)
        tokens = nltk.pos_tag(tokens)
        for token in tokens:
            word = token[0]
            word_type = token[1]
            if word.isalpha():
                filtered_words.append(word.lower()) 


    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(filtered_words)

    # only bigrams that appear n+ times
    finder.apply_freq_filter(10)
    bigrams_ratio_list = finder.score_ngrams(bigram_measures.likelihood_ratio)

    bigrams = {}
    for item in bigrams_ratio_list:
        pos = nltk.pos_tag(item[0])
        first = pos[0][0]
        second = pos[1][0]
        first_type = pos[0][1]
        second_type = pos[1][1]
        if (first_type == 'JJ' and second_type == 'NN') or (first_type == 'NN' and second_type == 'NN') or (first_type == 'JJ' and second_type == 'JJ'):
            if first != 'i' and second != 'i':
                if first != second:    
                    bigrams[ first + ' ' +  second ] = item[1]


    print(len(bigrams_ratio_list))    
    print(len(bigrams))    

    with open("bigrams_minfreq-10.json", "w") as outfile:  
        json.dump(bigrams, outfile)

if __name__ == '__main__':
    #get_bigrams_from_corpus('C:/myProjects/TDI/CapstoneProject/srt/Corpus/clean_corpus.txt')
    print_bigrams_from_json('C:/myProjects/SubtitlePro/Data/bigrams_minfreq-10.json')