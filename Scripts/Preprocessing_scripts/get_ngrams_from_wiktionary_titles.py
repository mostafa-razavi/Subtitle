
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.collocations import *
from nltk.corpus import words
from nltk.corpus import wordnet

stop_words = stopwords.words('english')
import json
import pandas as pd
#nltk.download('words')
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
english_words = words.words()

def get_english_unigrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    unigrams = []
    for _, title in titles_df['page_title'].items():
        word = str(title)
        if len(word) > 0:
            if word[0].islower():
                stem = stemmer.stem(word)
                if stem in english_words: 
                    count += 1
                    unigrams.append(word)
                    if count % 1000 == 0:
                        print(title, count)

    with open(json_file_out, "w") as outfile:  
        json.dump(unigrams, outfile)

def get_english_bigrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    bigrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 2: 
            first = split_by_[0]
            second = split_by_[1]
            if len(first) > 0 and len(second) > 0:
                if first[0].islower() and second[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    if first in english_words and second in english_words: 
                        count += 1
                        print(title, count)
                        bigrams.append(split_by_[0] + ' ' + split_by_[1])

    with open(json_file_out, "w") as outfile:  
        json.dump(bigrams, outfile)        

def get_english_trigrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    trigrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 3: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            if len(first) > 0 and len(second) > 0 and len(third) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    if first in english_words and second in english_words and third in english_words: 
                        count += 1
                        print(title, count)
                        trigrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2])

    with open(json_file_out, "w") as outfile:  
        json.dump(trigrams, outfile)

def get_english_quadgrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    quadgrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 4: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            fourth = split_by_[3]
            if len(first) > 0 and len(second) > 0 and len(third) > 0 and len(fourth) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    fourth = stemmer.stem(fourth)                
                    if first in english_words and second in english_words and third in english_words and fourth in english_words: 
                        count += 1
                        print(title, count)
                        quadgrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2] + ' ' + split_by_[3])

    with open(json_file_out, "w") as outfile:  
        json.dump(quadgrams, outfile) 

def get_english_pentagrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    pentagrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 5: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            fourth = split_by_[3]
            fifth = split_by_[4]
            if len(first) > 0 and len(second) > 0 and len(third) > 0 and len(fourth) > 0 and len(fifth) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower() and fourth[0].islower() and fifth[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    fourth = stemmer.stem(fourth)                
                    fifth = stemmer.stem(fifth)                
                    if first in english_words and second in english_words and third in english_words and fourth in english_words and fifth in english_words: 
                        count += 1
                        print(title, count)
                        pentagrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2] + ' ' + split_by_[3] + ' ' + split_by_[4])

    with open(json_file_out, "w") as outfile:  
        json.dump(pentagrams, outfile)                

def get_english_hexagrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    hexagrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 6: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            fourth = split_by_[3]
            fifth = split_by_[4]
            sixth = split_by_[5]
            if len(first) > 0 and len(second) > 0 and len(third) > 0 and len(fourth) > 0 and len(fifth) > 0 and len(sixth) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower() and fourth[0].islower() and fifth[0].islower() and sixth[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    fourth = stemmer.stem(fourth)                
                    fifth = stemmer.stem(fifth)                
                    sixth = stemmer.stem(sixth)                
                    if first in english_words and second in english_words and third in english_words and fourth in english_words and fifth in english_words and sixth in english_words: 
                        count += 1
                        print(title, count)
                        hexagrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2] + ' ' + split_by_[3] + ' ' + split_by_[4] + ' ' + split_by_[5])

    with open(json_file_out, "w") as outfile:  
        json.dump(hexagrams, outfile)

def get_english_heptagrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    heptagrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 7: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            fourth = split_by_[3]
            fifth = split_by_[4]
            sixth = split_by_[5]
            seventh = split_by_[6]
            if len(first) > 0 and len(second) > 0 and len(third) > 0 and len(fourth) > 0 and len(fifth) > 0 and len(sixth) > 0 and len(seventh) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower() and fourth[0].islower() and fifth[0].islower() and sixth[0].islower() and seventh[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    fourth = stemmer.stem(fourth)                
                    fifth = stemmer.stem(fifth)                
                    sixth = stemmer.stem(sixth)                
                    seventh = stemmer.stem(seventh)                
                    if first in english_words and second in english_words and third in english_words and fourth in english_words and fifth in english_words and sixth in english_words and seventh in english_words: 
                        count += 1
                        print(title, count)
                        heptagrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2] + ' ' + split_by_[3] + ' ' + split_by_[4] + ' ' + split_by_[5] + ' ' + split_by_[6])

    with open(json_file_out, "w") as outfile:  
        json.dump(heptagrams, outfile)

def get_english_ngrams_from_wiktioary_titles(n, json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    ngrams = []
    for _, title in titles_df['page_title'].items():
        words_list = str(title).split('_')
        N_words = len(words_list)
        if N_words == n: 
            for word in words_list:
                if len(word) > 0 and word[0].islower() and stemmer.stem(word.lower()) in english_words:
                    is_ngram_good = True
                    pass
                else:
                    is_ngram_good = False
                    break
            if is_ngram_good == True:
                count += 1
                print(title, count)
                ngrams.append(' '.join(words_list))

    with open(json_file_out, "w") as outfile:  
        json.dump(ngrams, outfile)

def get_non_phrasal_verb_3grams():
    n = 3
    n_gram_file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n) + 'grams.json'
    with open(n_gram_file_path) as f:
        wiktionary_ngrams = json.load(f) 
    accptable_word_types = [ 'NN', 'JJ' ] 
    #accptable_word_types = ['LS', 'TO', 'VBN', "''", 'WP', 'UH', 'VBG', 'JJ', 'VBZ', '--', 'VBP', 'NN', 'DT', 'PRP', ':', 'WP$', 'NNPS', 'PRP$', 'WDT', '(', ')', '.', ',', '``', '$', 'RB', 'RBR', 'RBS', 'VBD', 'IN', 'FW', 'RP', 'JJR', 'JJS', 'PDT', 'MD', 'VB', 'WRB', 'NNP', 'EX', 'NNS', 'SYM', 'CC', 'CD', 'POS']
    #accptable_word_types = ['LS', 'TO', "''", 'WP', 'UH', 'JJ', '--', 'NN', 'DT', 'PRP', ':', 'WP$', 'NNPS', 'PRP$', 'WDT', '(', ')', '.', ',', '``', '$', 'RB', 'RBR', 'RBS', 'IN', 'FW', 'RP', 'JJR', 'JJS', 'PDT', 'MD', 'WRB', 'NNP', 'EX', 'NNS', 'SYM', 'CC', 'CD', 'POS']

    filtered_ngrams = []
    for item in wiktionary_ngrams:
        pos = nltk.pos_tag(item.split())
        first = pos[0][0]
        second = pos[1][0]
        third = pos[2][0]
        first_type = pos[0][1]
        second_type = pos[1][1]
        third_type = pos[2][1]

        if first_type[0:2] in accptable_word_types and second_type[0:2] in accptable_word_types and third_type[0:2] in accptable_word_types:
            filtered_ngrams.append(item)
            print(item, first_type, second_type, third_type)
    json_file_out = 'C:/myProjects/SubtitlePro/Data/wiktionary_3grams_JJNN.json'
    with open(json_file_out, "w") as outfile:  
        json.dump(filtered_ngrams, outfile)

def get_non_phrasal_verb_2grams():
    n = 2
    n_gram_file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n) + 'grams.json'
    with open(n_gram_file_path) as f:
        wiktionary_ngrams = json.load(f) 
    #accptable_word_types = [ 'NN', 'JJ'  ] 
    #accptable_word_types = ['LS', 'TO', 'VBN', "''", 'WP', 'UH', 'VBG', 'JJ', 'VBZ', '--', 'VBP', 'NN', 'DT', 'PRP', ':', 'WP$', 'NNPS', 'PRP$', 'WDT', '(', ')', '.', ',', '``', '$', 'RB', 'RBR', 'RBS', 'VBD', 'IN', 'FW', 'RP', 'JJR', 'JJS', 'PDT', 'MD', 'VB', 'WRB', 'NNP', 'EX', 'NNS', 'SYM', 'CC', 'CD', 'POS']
    accptable_word_types = ['LS', 'TO', "''", 'WP', 'UH', 'JJ', '--', 'NN', 'DT', 'PRP', ':', 'WP$', 'NNPS', 'PRP$', 'WDT', '(', ')', '.', ',', '``', '$', 'RB', 'RBR', 'RBS', 'IN', 'FW', 'RP', 'JJR', 'JJS', 'PDT', 'MD', 'WRB', 'NNP', 'EX', 'NNS', 'SYM', 'CC', 'CD', 'POS']

    filtered_ngrams = []
    for item in wiktionary_ngrams:
        pos = nltk.pos_tag(item.split())
        first = pos[0][0]
        second = pos[1][0]
        first_type = pos[0][1]
        second_type = pos[1][1]

        if first_type in accptable_word_types and second_type in accptable_word_types:
        #if first_type[0:2] in accptable_word_types and second_type[0:2] in accptable_word_types:
            filtered_ngrams.append(item)
            print(item, first_type, second_type)
    json_file_out = 'C:/myProjects/SubtitlePro/Data/wiktionary_2grams_AllButVB.json'
    with open(json_file_out, "w") as outfile:  
        json.dump(filtered_ngrams, outfile)        


if __name__ == '__main__':

    #get_english_unigrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_unigrams.json')
    #get_english_bigrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_bigrams.json')
    #get_english_trigrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_trigrams.json')
    #get_english_quadgrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_quadgrams.json')
    #get_english_pentagrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_pentagrams.json')
    #get_english_hexagrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_hexagrams.json')
    #get_english_heptagrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_heptagrams.json')
    get_english_ngrams_from_wiktioary_titles(n=8, json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_octagrams.json')
    get_english_ngrams_from_wiktioary_titles(n=9, json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_nonagrams.json')
    get_english_ngrams_from_wiktioary_titles(n=10, json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_decagrams.json')
    #get_non_phrasal_verb_2grams()
