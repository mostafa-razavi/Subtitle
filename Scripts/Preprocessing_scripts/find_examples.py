
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.collocations import *
import pickle
stop_words = stopwords.words('english')
import json

trigrams_json = 'C:/myProjects/SubtitlePro/Data/wiktionary_3grams.json'
with open(trigrams_json, 'rb') as fp:
    trigrams = json.load(fp)

 

def find_examples_of_ngrams(n, movies_corpus):
    n_gram_file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n) + 'grams.json'
    with open(n_gram_file_path) as f:
        wiktionary_ngrams = json.load(f)  

    count = 0
    for movie, subtitle_text_dict in movies_corpus.items():
        for subtitle in list(movies_corpus[movie].keys()):
            for n_gram in wiktionary_ngrams: #['pony up']:
                movie_text_list = subtitle_text_dict[subtitle]
                for index, sentence in enumerate(movie_text_list):
                    if n_gram in sentence:
                        count += 1
                        print(count, '-------->', n_gram, '-------->', movie, subtitle, index, '-------->', sentence)

if __name__ == '__main__':
    with open("C:/myProjects/TDI/CapstoneProject/srt/Corpus/corpus.json") as json_file: 
        movies_corpus = json.load(json_file)  

    find_examples_of_ngrams(n=3, movies_corpus=movies_corpus)                