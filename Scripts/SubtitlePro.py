from pretty_table import generate_html_from_dictionary
from get_subtitle import get_movie_index_info, download_one_movie_subtitle, get_movie_lines_list
from find_ngrams_in_subtitle import find_wiktionary_ngrams_in_subtitle, find_wiktionary_phrasal_verbs_in_subtitle, get_top_n_difficult_words
from srt_to_wordfreq import srt_to_frequency_dict

from flask import Flask, render_template, request
import shutil
import os
import zipfile
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud


work_dir = 'C:/myProjects/SubtitlePro/'

with zipfile.ZipFile(work_dir + 'Data/wiktionary.zip', 'r') as zip_ref:
    zip_ref.extractall(work_dir + 'Data/')

with open(work_dir + 'Data/wiktionary.json') as json_file: 
    wiktionary = json.load(json_file)

def get_srt_file(movie_name):
    subtitle_index, movie_index, movie_name, movie_year =  get_movie_index_info(movie_name)
    subtitle_zip = work_dir + 'Srt/imov_' + str(movie_index) + '-isub_' + str(subtitle_index) + '.zip'
    download_one_movie_subtitle(movie_index, 'English', subtitle_zip)

    try: 
        os.mkdir(work_dir + 'temp_srt/') 
    except:
        shutil.rmtree(work_dir + 'temp_srt/')
        os.mkdir(work_dir + 'temp_srt/') 

    with zipfile.ZipFile(subtitle_zip, 'r') as zip_ref:
        zip_ref.extractall(work_dir + 'temp_srt/')
    srt_file_name = work_dir + 'temp_srt/' + os.listdir(work_dir + 'temp_srt/')[0]    

    return srt_file_name


def replace_pattern_in_file(template_file, output_file, pattern, replace_with):
    shutil.copy(template_file, output_file)
    with open(output_file, 'r') as file :
        filedata = file.read()

    for i, word in enumerate(pattern):
        filedata = filedata.replace(pattern[i], replace_with[i])

    with open(output_file, 'w') as file:
        file.write(filedata)    

def merge_files(file1, file2, output_file):
    data = data2 = ""
    
    with open(file1, encoding="utf-8") as fp:
        data = fp.read()
    
    with open(file2, encoding="utf-8") as fp:
        data2 = fp.read()
    
    data += "\n"
    data += data2
    
    with open (output_file, 'w', encoding="utf-8") as fp:
        fp.write(data)    

app = Flask(__name__)

@app.route('/')
def submit_form():
    return render_template('input_form.html')


@app.route('/', methods=['POST'])
def home():
    movie_name = request.form['movie_name']
    srt_file_name = get_srt_file(movie_name)
    movie_lines = get_movie_lines_list(srt_file_name)
    print(movie_name)
    print(srt_file_name)

    word_freq_file = work_dir + 'Data/word_freq.json'
    difficult_words = get_top_n_difficult_words(movie_lines_list=movie_lines, top_n=20, dictionary_dict=wiktionary, word_freq_file=word_freq_file)
    phrasal_verbs = find_wiktionary_phrasal_verbs_in_subtitle(movie_lines_list=movie_lines, dictionary_dict=wiktionary)
    bigrams = find_wiktionary_ngrams_in_subtitle(movie_lines_list=movie_lines, n_gram_key="2_NNJJ", dictionary_dict=wiktionary)
    trigrams = find_wiktionary_ngrams_in_subtitle(movie_lines_list=movie_lines, n_gram_key="3_AllButVB", dictionary_dict=wiktionary)
    quadgrams = find_wiktionary_ngrams_in_subtitle(movie_lines_list=movie_lines, n_gram_key="4", dictionary_dict=wiktionary)
    pentagrams = find_wiktionary_ngrams_in_subtitle(movie_lines_list=movie_lines, n_gram_key="5", dictionary_dict=wiktionary)
    hexagrams = find_wiktionary_ngrams_in_subtitle(movie_lines_list=movie_lines, n_gram_key="6", dictionary_dict=wiktionary)
    heptagrams = find_wiktionary_ngrams_in_subtitle(movie_lines_list=movie_lines, n_gram_key="7", dictionary_dict=wiktionary)

    master_output_dict = {}
    '''    
    master_output_dict['Difficult Words'] = difficult_words
    master_output_dict['Phrasal Verbs'] = phrasal_verbs
    master_output_dict['Bigrams'] = bigrams
    master_output_dict['Trigrams'] = trigrams
    master_output_dict['4-grams'] = quadgrams
    master_output_dict['5-grams'] = pentagrams
    master_output_dict['6-grams'] = hexagrams
    master_output_dict['7-grams'] = heptagrams
    '''
    difficult_words_list = []
    for item in difficult_words:
        difficult_words_list.append(item)
    master_output_dict['Difficult Words'] = difficult_words_list

    phrasal_verbs_list = []
    for item in phrasal_verbs:
        phrasal_verbs_list.append(item)
    master_output_dict['Phrasal Verbs'] = phrasal_verbs_list

    collocations_list = []
    for item in [bigrams, trigrams, quadgrams, pentagrams, hexagrams, heptagrams]:
        for collocation in item:
            collocations_list.append(collocation)
    master_output_dict['Collocations'] = collocations_list    
    
        
    for item in [difficult_words, phrasal_verbs, bigrams, trigrams, quadgrams, pentagrams, hexagrams, heptagrams]:
        for ngram, meaning in item.items():
            master_output_dict[ngram] = meaning

    out_html_path = work_dir + 'Scripts/templates/' + '_'.join(movie_name.split()) + '.html'
    html_file = generate_html_from_dictionary(master_output_dict, out_html_path)


    subtitle_index, movie_index, movie_name, movie_year =  get_movie_index_info(movie_name)
    template_file = work_dir + 'Scripts/templates/template_head.html'
    output_file = work_dir + 'Scripts/templates/head.html'
    pattern = ['some_movie_name', 'some_year']
    replace_with = [movie_name, str(int(movie_year))]
    replace_pattern_in_file(template_file, output_file, pattern, replace_with)

    merge_files(output_file, out_html_path, out_html_path)

    return render_template(html_file)


if __name__ == '__main__':
   app.run()