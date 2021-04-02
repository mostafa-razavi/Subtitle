import json
import re
from dictionary import get_dictionary_meaning
import matplotlib.pyplot as plt
from wordcloud import WordCloud


import pandas as pd
import numpy as np
from srt_to_wordfreq import srt_to_frequency_dict
from dictionary import get_dictionary_meaning
import math
import nltk
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

sample_wiktionary_entry = {
    "ab off": [{
        "etymology": "Shortening of abseil + off.\n", 
        "definitions": [{
            "partOfSpeech": "verb", 
            "text": [
                "ab off (third-person singular simple present abs off, present participle abbing off, simple past and past participle abbed off)", 
                "(British, transitive, slang, mountaineering) To abseil down a mountain."
                ], 
            "relatedWords": [], 
            "examples": [
                "Synonym: rap down", 
                "Every one's up on a crag where he'd got stuck and had to ab off.", 
                "Two of them abbed off to leave enough for the other two."
            ]
        }], 
        "pronunciations": {"text": [], "audio": []}}
    ]
}

def find_wiktionary_ngrams_in_subtitle_from_corpus(imov, n_gram):
    with open("C:/myProjects/TDI/CapstoneProject/srt/Corpus/corpus.json") as json_file: 
        movies_corpus = json.load(json_file) 

    file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n_gram) + 'grams_JJNN.json'

    with open(file_path) as f:
        wiktionary_ngrams = json.load(f)   

    imov = str(imov)
    isub = list(movies_corpus[imov].keys())[0]
    movie_lines_list = movies_corpus[imov][isub]
    count = 0
    for ngram in wiktionary_ngrams:
        for text in movie_lines_list:
            if ngram in text:
                pattern = r'\b' + re.escape(ngram) + r'\b'
                if re.search(pattern, text):
                    count += 1
                    print(count, ngram, '  ---------->  ', text)

def find_wiktionary_ngrams_in_subtitle(movie_lines_list, n_gram_key, dictionary_dict):
    wiktionary_ngrams_file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_ngrams.json'
    with open(wiktionary_ngrams_file_path) as f:
        wiktionary_ngrams = json.load(f)[n_gram_key]   

    ngram_dict_with_meanings_and_usages = {}
    for ngram in wiktionary_ngrams:
        found_ngram = False
        list_of_lines_where_ngram_is_used = []
        for line in movie_lines_list:
            if ngram in line:
                pattern = r'\b' + re.escape(ngram) + r'\b'
                if re.search(pattern, line):
                    found_ngram = True
                    #print(ngram, '  ---------->  ', line)
                    list_of_lines_where_ngram_is_used.append(line)
        if found_ngram:
            meaning = get_dictionary_meaning(ngram, dictionary_dict) 
            if meaning != None and len(meaning) != 0:
                new_dict = meaning[0]
                new_dict['captions'] = list_of_lines_where_ngram_is_used
                ngram_dict_with_meanings_and_usages[ngram] = new_dict
    return ngram_dict_with_meanings_and_usages


def find_wiktionary_phrasal_verbs_in_subtitle(movie_lines_list, dictionary_dict):
    wiktionary_ngrams_file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_ngrams.json'
    with open(wiktionary_ngrams_file_path) as f:
        wiktionary_ngrams = json.load(f)['phrasal_verbs']

    ngram_dict_with_meanings_and_usages = {}
    for ngram, tenses in wiktionary_ngrams.items():
        tenses.append(ngram)

        found_ngram = False
        list_of_lines_where_ngram_is_used = []
        for line in movie_lines_list:
            for tense in tenses:
                if tense in line:
                    pattern = r'\b' + re.escape(tense) + r'\b'
                    if re.search(pattern, line):
                        found_ngram = True
                        #print(ngram, '  ---------->  ', line)
                        list_of_lines_where_ngram_is_used.append(line)
        if found_ngram:
            meaning = get_dictionary_meaning(ngram, dictionary_dict) 
            if meaning != None and len(meaning) != 0:
                new_dict = meaning[0]
                new_dict['captions'] = list_of_lines_where_ngram_is_used
                ngram_dict_with_meanings_and_usages[ngram] = new_dict
    return ngram_dict_with_meanings_and_usages

def get_unique_words(movie_lines_list):
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    filtered_words = []
    for line in movie_lines_list:
        words = nltk.tokenize.word_tokenize(line)
        for word in words:
            if word not in stop_words:
                if word.isalpha():
                    word = word.lower()
                    filtered_words.append(stemmer.stem(word))              
                    #filtered_words.append(word)

    return (list(set(filtered_words)))

def get_top_n_difficult_words(movie_lines_list, top_n, dictionary_dict, word_freq_file):
    def get_word_difficulty_index(word, word_freq_dict):
            try:
                freq = float(word_freq_dict[word])
                return 691.3199662 / math.log10(freq)**3 # 1000 / math.log10(freq)**3 / 14.465082*10
            except:
                    return 0      

    with open(word_freq_file) as f:
        word_freq_dict = json.load(f)        

    unique_words = get_unique_words(movie_lines_list)
    new_unique_words = {}
    count = 0
    for word in unique_words:
        difficulty = get_word_difficulty_index(word, word_freq_dict)
        meaning = get_dictionary_meaning(word, dictionary_dict)
        if meaning != None and len(meaning) != 0:
            new_unique_words[word] = difficulty

        
    sorted_word_difficulty = dict(sorted(new_unique_words.items(), key=lambda item: item[1], reverse=True))        


    movie_word_frequency_dict = srt_to_frequency_dict(movie_lines_list)
    fig,ax = plt.subplots(1)
    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=500,relative_scaling=0.1,normalize_plurals=False).generate_from_frequencies(movie_word_frequency_dict)
    ax.axis('off')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.imshow(wc, interpolation="bilinear")
    plt.savefig( 'static/word_freq.png')
    #plt.show()
       
    fig,ax = plt.subplots(1)
    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=500,relative_scaling=0.1,normalize_plurals=False).generate_from_frequencies(new_unique_words)
    ax.axis('off')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.imshow(wc, interpolation="bilinear")
    plt.savefig( 'static/word_difficulty.png')
    #plt.show()
    


    meaningful_words = {}
    count = 0
    for word in sorted_word_difficulty:
        meaning = get_dictionary_meaning(word, dictionary_dict)
        if meaning != None:
            count += 1
            meaningful_words[word] = meaning
        if count == int(top_n):
            break
        

    ngram_dict_with_meanings_and_usages = {}
    for ngram, meaning in meaningful_words.items():
        found_ngram = False
        list_of_lines_where_ngram_is_used = []
        for line in movie_lines_list:
            if ngram in line:
                pattern = r'\b' + re.escape(ngram) + r'\b'
                if re.search(pattern, line):
                    found_ngram = True
                    #print(ngram, '  ---------->  ', line)
                    list_of_lines_where_ngram_is_used.append(line)
        if found_ngram:
            if meaning != None and len(meaning) != 0:
                new_dict = meaning[0]
                new_dict['captions'] = list_of_lines_where_ngram_is_used
                ngram_dict_with_meanings_and_usages[ngram] = new_dict
    return ngram_dict_with_meanings_and_usages

def get_top_n_difficult_words_2(movie_lines_list, top_n, dictionary_dict, word_freq_file):
    def get_word_difficulty_index(word, word_freq_dict):
            try:
                freq = float(word_freq_dict[word])
                return 691.3199662 / math.log10(freq)**3 # 1000 / math.log10(freq)**3 / 14.465082*10
            except:
                    return np.nan      

    with open(word_freq_file) as f:
        word_freq_dict = json.load(f)        

    movie_word_frequency_dict = srt_to_frequency_dict(movie_lines_list)

    new_movie_word_frequency_dict = {}
    count = 0
    for key, value in movie_word_frequency_dict.items():
        count += 1
        new_movie_word_frequency_dict[key] = (value, get_word_difficulty_index(key, word_freq_dict))
        
    df_freq_diff = pd.DataFrame.from_dict(data=new_movie_word_frequency_dict, orient='index', columns=[ 'freq', 'difficulty'])
    df_freq_diff = df_freq_diff.sort_values(by=['difficulty'], ascending=False)

    meaningful_words = {}
    count = 0
    difficulty_top_n = []
    most_difficult_words = df_freq_diff.index.tolist()
    for word in most_difficult_words:
        meaning = get_dictionary_meaning(word, dictionary_dict)
        if meaning != None:
            count += 1
            meaningful_words[word] = meaning
        if count == int(top_n):
            break
        
    return meaningful_words


def combine_wiktionary_ngrams_into_one_json():
    wiktionary_ngrams_dict = {}

    for i in range(10):
        ngram = i+1
        with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_' + str(ngram) + 'grams.json') as f:
            wiktionary_ngrams = json.load(f)
        wiktionary_ngrams_dict[ngram] = wiktionary_ngrams

    with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_2grams_JJNN.json') as f:
        wiktionary_ngrams = json.load(f)    
    wiktionary_ngrams_dict['2_NNJJ'] =  wiktionary_ngrams  

    with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_phrasal_verbs.json') as f:
        wiktionary_ngrams = json.load(f)    
    wiktionary_ngrams_dict['phrasal_verbs'] =  wiktionary_ngrams      

    with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_2grams_AllButVB.json') as f:
        wiktionary_ngrams = json.load(f)    
    wiktionary_ngrams_dict['2_AllButVB'] =  wiktionary_ngrams   

    with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_3grams_JJNN.json') as f:
        wiktionary_ngrams = json.load(f)    
    wiktionary_ngrams_dict['3_NNJJ'] =  wiktionary_ngrams  

    with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_3grams_AllButVB.json') as f:
        wiktionary_ngrams = json.load(f)    
    wiktionary_ngrams_dict['3_AllButVB'] =  wiktionary_ngrams           

    with open('C:/myProjects/SubtitlePro/Other_data/wiktionary_ngrams.json', 'w') as f:
        json.dump(wiktionary_ngrams_dict, f)



if __name__ == '__main__':
    #combine_wiktionary_ngrams_into_one_json()
    #find_wiktionary_ngrams_in_subtitle_from_corpus(imov, 2)



    work_dir = 'C:/myProjects/SubtitlePro/'
    with open(work_dir + 'Data/wiktionary.json') as json_file: 
        wiktionary = json.load(json_file)
        
    from get_subtitle import get_movie_lines_list
    movie_lines = get_movie_lines_list('C:/myProjects/TDI/CapstoneProject/srt/other/Inception.srt')

    word_freq_file = work_dir + 'Data/word_freq.json'
    difficult_words = get_top_n_difficult_words(movie_lines_list=movie_lines, top_n=5, dictionary_dict=wiktionary, word_freq_file=word_freq_file)
    print(difficult_words)
    exit()
    phrasal_verbs = find_wiktionary_phrasal_verbs_in_subtitle(movie_lines, wiktionary)

    bigrams = find_wiktionary_ngrams_in_subtitle(movie_lines, 2, wiktionary)
    trigrams = find_wiktionary_ngrams_in_subtitle(movie_lines, 3, wiktionary)
    quadgrams = find_wiktionary_ngrams_in_subtitle(movie_lines, 4, wiktionary)
    pentagrams = find_wiktionary_ngrams_in_subtitle(movie_lines, 5, wiktionary)
    hexagrams = find_wiktionary_ngrams_in_subtitle(movie_lines, 6, wiktionary)

    for ngrams in [phrasal_verbs, bigrams, trigrams, quadgrams, pentagrams, hexagrams]:
        for ngram, meaning in ngrams.items():
            print(ngram, meaning)

