import pandas as pd
from srt_to_wordfreq import srt_to_frequency_dict2
from word_difficulty import get_word_difficulty_index
from get_subtitle import get_movie_index_info, download_one_movie_subtitle
from dictionary import get_dictionary_meaning
from PyDictionary import PyDictionary
import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import os
import shutil
from os import path
import csv
import numpy as np
import sys

from PyDictionary import PyDictionary

import argparse
from pathlib import Path
from wordfreq import word_frequency


import matplotlib.pyplot as plt
from wordcloud import WordCloud


import json



word_dir = 'C:/myProjects/SubtitlePro/'


######### Get arguments ############
parser = argparse.ArgumentParser(description='This program evaluates the difficulty of a movie for language learners and provides the definitions for the most difficult words.')

parser.add_argument('-title', metavar="title", type=str, help="Title of the movie")
parser.add_argument('-top', metavar="top", type=str, help="Title of the movie")
parser.add_argument('-dict', metavar="dict", type=str, help="Dictionary type: PyDictionary or Wiktionary")
args = parser.parse_args()
movie_name = args.title
top_n = args.top
dictionary_type = args.dict

def load_jason(json_file):
    with open(json_file) as json_file: 
        data = json.load(json_file)
    return data

if dictionary_type == 'PyDictionary':
    dictionary_dict = load_jason(word_dir + 'Other_data/unigram_meaning_PyDictionary.json')
elif dictionary_type == 'Wiktionary':
    dictionary_dict = load_jason(word_dir + 'Other_data/unigram_meaning_Wiktionary.json')


subtitle_index, movie_index, movie_name, movie_year =  get_movie_index_info(movie_name)
subtitle_zip = word_dir + 'Srt/imov_' + str(movie_index) + '-isub_' + str(subtitle_index) + '.zip'
download_one_movie_subtitle(movie_index, 'English', subtitle_zip)

try: 
    os.mkdir(word_dir + 'temp_srt/') 
except:
    shutil.rmtree(word_dir + 'temp_srt/')
    os.mkdir(word_dir + 'temp_srt/') 

import zipfile
with zipfile.ZipFile(subtitle_zip, 'r') as zip_ref:
    zip_ref.extractall(word_dir + 'temp_srt/')
srt_file_name = word_dir + 'temp_srt/' + os.listdir(word_dir + 'temp_srt/')[0]


profanity_list_file = word_dir + 'Other_data/profane_list_less.txt'
web_word_freq_csv = word_dir + 'Other_data/unigram_freq.csv'
df = pd.read_csv(web_word_freq_csv)
df_profane = pd.read_csv(profanity_list_file)

movie_word_frequency_dict = srt_to_frequency_dict(srt_file_name)

fig,ax = plt.subplots(1)
wc = WordCloud(background_color="white",width=1000,height=1000, max_words=500,relative_scaling=0.1,normalize_plurals=False).generate_from_frequencies(movie_word_frequency_dict)

ax.axis('off')

ax.set_xticklabels([])
ax.set_yticklabels([])
plt.imshow(wc, interpolation="bilinear")
plt.show()

diff_csv_file = word_dir + 'difficulty/' + str(movie_index) + '.csv'
if path.exists(diff_csv_file):
    df_freq_diff = pd.read_csv(diff_csv_file)  
else:
    index = -1
    new_movie_word_frequency_dict = {}
    for key, value in movie_word_frequency_dict.items():
        index += 1
        if key not in df_profane.values:
            new_movie_word_frequency_dict[index] = (key, value, get_word_difficulty_index(key, df))
            #new_movie_word_frequency_dict[index] = (key, value, word_frequency(key, 'en'))

    df_freq_diff = pd.DataFrame.from_dict(data=new_movie_word_frequency_dict, orient='index', columns=['word', 'freq', 'difficulty'])
    df_freq_diff = df_freq_diff.sort_values(by=['difficulty'], ascending=False)
    df_freq_diff.to_csv(diff_csv_file)


#print(df_freq_diff)


meaningful_words = {}
count = 0
difficulty_top_n = []
most_difficult_words = df_freq_diff['word']
for index, word in most_difficult_words.iteritems():
    meaning = get_dictionary_meaning(word, dictionary_dict)
    if meaning != None:
        count += 1
        meaningful_words[word] = meaning
        difficulty_top_n.append(df_freq_diff.loc[df_freq_diff['word'] == word, 'difficulty'].iloc[0])
    if count == int(top_n):
        break

mean_difficulty_top_n = round(np.mean(np.array(difficulty_top_n)), 2)

print()
print()
print('============================================================')
print("Title: ", movie_name, '(' + str(int(movie_year)) + ')')
print('Difficulty Score: ', mean_difficulty_top_n)
print("Movie ID: ", movie_index)
print("Subtitle ID: ", subtitle_index)
print()
print()
print("==================== Most difficult words ================= ")
print()
print()

def print_meanings(meaningful_words, dictionary_type, df_freq_diff):
    if dictionary_type == 'PyDictionary':
        for key, value in meaningful_words.items():
            key_difficulty = df_freq_diff.loc[df_freq_diff['word'] == key, 'difficulty'].iloc[0]
            key_difficulty = str(round(key_difficulty, 2))
            print(key, '(' + key_difficulty + ')' )
            for word_type, word_meaning in value.items():
                print( '\t\t\t' , word_type, ' | ' ,  " ".join(word_meaning[:2]))
            print()
            print()
    elif dictionary_type == 'Wiktionary':
        for key, value in meaningful_words.items():
            key_difficulty = df_freq_diff.loc[df_freq_diff['word'] == key, 'difficulty'].iloc[0]
            key_difficulty = str(round(key_difficulty, 2))
            print(key, '(' + key_difficulty + ')' )
            for item, word_meaning in value.items():
                if item == 'partOfSpeech':
                    print( '\t\t\t' , 'Word Type:')
                    print('\t\t\t', '\t\t\t', word_meaning)                    
                if item == 'definitions':
                    print( '\t\t\t' , 'Definitions:')
                    for def_item in word_meaning[1:]:
                        print('\t\t\t', '\t\t\t', def_item)  
                if item == 'examples':
                    if len(word_meaning) != 0:
                        print( '\t\t\t' , 'Examples:')
                        for def_item in word_meaning:
                            print('\t\t\t', '\t\t\t', def_item)                                            
            print()
            print()        

print_meanings(meaningful_words, dictionary_type, df_freq_diff)                