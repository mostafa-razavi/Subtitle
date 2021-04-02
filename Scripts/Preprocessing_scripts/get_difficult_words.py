import pandas as pd
import numpy as np
from srt_to_wordfreq import srt_to_frequency_dict
from dictionary import get_dictionary_meaning
import math
import json

def get_top_n_difficult_words(movie_lines_list, top_n, dictionary_dict, word_freq_file):
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



if __name__ == '__main__':
    srt_file_name = "C:/myProjects/TDI/CapstoneProject/srt/Other/Inception.srt"

    with open(work_dir + 'Data/Wiktionary.json') as json_file: 
        wiktionary = json.load(json_file)

    words = get_top_n_difficult_words(srt_file_name, 5, wiktionary)
