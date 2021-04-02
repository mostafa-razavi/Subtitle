
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.collocations import *
import pickle
stop_words = stopwords.words('english')
import json


def get_good_trigrams_from_json(json_file_in, json_file_out, method):
    with open(json_file_in, 'rb') as fp:
        trigrams = json.load(fp)
    good_trigrams_dict = {}
    count = 0

    if method == 1:
        accepted_word_types = [ 'NN', 'JJ', 'CC', 'DT', 'IN', 'RB' ]
        unaccepted_words = ['i', 'na', 'wan', 'gon', 'don', 't', 'l', 'ha', 'huh', 'won', 'aren', 'air', 'oh', 'hey', 'okay', 'ok', 'fuck', 'shit', 'yeah', 'yea', 'ho', 'hi', 'good', 'hello', 'bye', 'yes', 'no', 'please', 'god', 'ya', 'thank', 'uh' ]
        unaccepted_first = ['of', 'and', 'or']
        unaccepted_third = ['of', 'and', 'or', 'if', 'not', 'for', 'an', 'a']

        for item in trigrams.items():
            pos = nltk.pos_tag(item[0].split(' '))
            first = pos[0][0]
            second = pos[1][0]
            third = pos[2][0]
            first_type = pos[0][1]
            second_type = pos[1][1]
            third_type = pos[2][1]

            if 'the' not in [first, second, third]:
                if first not in unaccepted_first:
                    if third not in unaccepted_third:
                        if any(x in [first, second, third] for x in unaccepted_words) == False:
                            if 'come on' not in item[0] and 'all right' not in item[0]:
                                if first_type in accepted_word_types and second_type in accepted_word_types  and third_type in accepted_word_types :
                                    if not (len(first) == 1 or len(second) == 1 or len(third) == 1):
                                        if len(set(item[0].split(' '))) == 3:
                                            good_trigrams_dict[ first + ' ' +  second + ' ' +  third ] = item[1]
                                            count += 1
                                            print(item, count)
                                                    
    if method == 2:
        with open('C:/myProjects/SubtitlePro/Data/wiktionary_3grams.json', 'rb') as fp:
            wiktionary_trigrams = json.load(fp)
        for item in trigrams.items():
            if item[0] in wiktionary_trigrams:
                good_trigrams_dict[ item[0] ] = item[1]
                count += 1
                print(item, count)


    with open(json_file_out, "w") as outfile:  
        json.dump(good_trigrams_dict, outfile)


def print_trigrams_from_json(json_file):
    with open (json_file, 'rb') as fp:
        trigrams = json.load(fp)

    exit()                
    count = 0
    for bigram in trigrams.items():
        print(bigram)
        count += 1
        if count % 50 == 0:
            print(count)
            input()


def get_trigrams_from_corpus(corpus_json):
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


    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    finder = TrigramCollocationFinder.from_words(filtered_words)

    # only trigrams that appear n+ times
    finder.apply_freq_filter(10)
    trigrams_ratio_list = finder.score_ngrams(trigram_measures.likelihood_ratio)

    good_trigrams = {}
    for item in trigrams_ratio_list:
        pos = nltk.pos_tag(item[0])
        first = pos[0][0]
        second = pos[1][0]
        third = pos[2][0]
        first_type = pos[0][1]
        second_type = pos[1][1]
        third_type = pos[2][1]
        if first != second and second != third:    
            good_trigrams[ first + ' ' +  second + ' ' + third ] = item[1]

    print(len(trigrams_ratio_list))    
    print(len(good_trigrams))    

    with open("C:/myProjects/SubtitlePro/Data/trigrams_minfreq-10.json", "w") as outfile:  
        json.dump(good_trigrams, outfile)



if __name__ == '__main__':

    #get_trigrams_from_corpus('C:/myProjects/TDI/CapstoneProject/srt/Corpus/clean_corpus.txt')
    #print_trigrams_from_json("C:/myProjects/SubtitlePro/Data/good_trigrams_minfreq-10.json")
    #get_good_trigrams_from_json(json_file_in='C:/myProjects/SubtitlePro/Data/trigrams_minfreq-10.json', json_file_out='C:/myProjects/SubtitlePro/Data/good-method-1_trigrams_minfreq-10.json', method=1)
    get_good_trigrams_from_json(json_file_in='C:/myProjects/SubtitlePro/Data/trigrams_minfreq-10.json', json_file_out='C:/myProjects/SubtitlePro/Data/good-method-2_trigrams_minfreq-10.json', method=2)