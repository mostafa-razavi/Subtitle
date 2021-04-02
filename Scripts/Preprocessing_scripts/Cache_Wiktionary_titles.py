import argparse

from PyDictionary import PyDictionary
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

import json

from wiktionaryparser import WiktionaryParser
wik_parser = WiktionaryParser()

def get_all_meanings(from_index, to_index, batch_from):
    all_ngrams_list = []
    for n in range(10):
        with open('C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n+1) + 'grams.json') as f:
            ngrams = json.load(f)
        for item in ngrams:
            all_ngrams_list.append(item)
    with open('C:/myProjects/SubtitlePro/Data/unigram_meaning_Wiktionary.json') as f:
        old_wiktionary = json.load(f)

    i = batch_from - 1
    in_count = 0
    in_dict = {}
    is_arrived = False
    for index, word in enumerate(all_ngrams_list):
        if word == last_title:
            is_arrived = True
        else:
            if is_arrived == True:
                if index >= from_index and index < to_index:
                    if word in old_wiktionary:
                        in_dict[word] = old_wiktionary[word]
                        in_count += 1
                    else:

                        try:
                            meaning = wik_parser.fetch(word, 'English')
                        except:
                            pass
                        else:
                            if meaning != None:
                                in_dict[word] = meaning
                                in_count += 1
                    if in_count == 1000:
                        i += 1
                        out_jason_file_name = str(from_index) + '_' + str(to_index) + '_' + str(i) + ".json"
                        with open('C:/myProjects/TDI/CapstoneProject/Wiktionary/wiktionary_titles_meanings/json/' + out_jason_file_name, "w") as outfile:  
                            json.dump(in_dict, outfile)
                        print("Dumped in file: " + out_jason_file_name)
                        in_count = 0
                        in_dict = {}

    i += 1
    out_jason_file_name = str(from_index) + '_' + str(to_index) + '_' + str(i) + ".json"
    with open('C:/myProjects/TDI/CapstoneProject/Wiktionary/wiktionary_titles_meanings/json/' + out_jason_file_name, "w") as outfile:  
        json.dump(in_dict, outfile)
    print("Dumped in file: " + out_jason_file_name)

def concatenate_all_json_files_and_select_keys():
    concat_json_dict = {}
    for i in range(1, 334)            :
        json_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/wiktionary_titles_meanings/json/' + str(i) + '.json'

        with open(json_file) as f:
            data = json.load(f)
        for key, value in data.items():
            if len(value) != 0:
                meaning = value[0] 
                #etimology = meaning['etymology']
                definitions = meaning['definitions']
                #pronunciations = meaning['pronunciations']
                try:
                    examples = meaning['examples']
                except:
                    examples = []
                temp_dict = {}
                if len(definitions) != 0:
                    temp_dict['definitions'] = definitions[0]['text']
                    temp_dict['partOfSpeech'] = definitions[0]['partOfSpeech']
                    temp_dict['examples'] = examples
                    concat_json_dict[key] = temp_dict
    with open("unigram_meaning.json", "w") as outfile:  
        json.dump(concat_json_dict, outfile)

def concatenate_all_json_files():
    concat_json_dict = {}
    json_files = ["0_50000_1.json", "0_50000_2.json", "0_50000_3.json", "0_50000_4.json", "0_50000_5.json", "0_50000_6.json", "0_50000_7.json", "0_50000_8.json", "0_50000_9.json", "0_50000_10.json", "0_50000_11.json", "0_50000_12.json", "0_50000_13.json", "0_50000_14.json", "0_50000_15.json", "0_50000_16.json", "0_50000_17.json", "0_50000_18.json", "0_50000_19.json", "0_50000_20.json", "0_50000_21.json", "0_50000_22.json", "0_50000_23.json", "0_50000_24.json", "0_50000_25.json", "0_50000_26.json", "0_50000_27.json", "0_50000_28.json", "0_50000_29.json", "0_50000_30.json", "0_50000_31.json", "0_50000_32.json", "0_50000_33.json", "0_50000_34.json", "0_50000_35.json", "0_50000_36.json", "0_50000_37.json", "0_50000_38.json", "0_50000_39.json", "0_50000_40.json", "0_50000_41.json", "0_50000_42.json", "0_50000_43.json", "0_50000_44.json", "0_50000_45.json", "0_50000_46.json", "0_50000_47.json", "0_50000_48.json", "0_50000_49.json", "0_50000_50.json", "50000_100000_1.json", "50000_100000_2.json", "50000_100000_3.json", "50000_100000_4.json", "50000_100000_5.json", "50000_100000_6.json", "50000_100000_7.json", "50000_100000_8.json", "50000_100000_9.json", "50000_100000_10.json", "50000_100000_11.json", "50000_100000_12.json", "50000_100000_13.json", "50000_100000_14.json", "50000_100000_15.json", "50000_100000_16.json", "50000_100000_17.json", "50000_100000_18.json", "50000_100000_19.json", "50000_100000_20.json", "50000_100000_21.json", "50000_100000_22.json", "50000_100000_23.json", "50000_100000_24.json", "50000_100000_25.json", "50000_100000_26.json", "50000_100000_27.json", "50000_100000_28.json", "50000_100000_29.json", "50000_100000_30.json", "50000_100000_31.json", "50000_100000_32.json", "50000_100000_33.json", "50000_100000_34.json", "50000_100000_35.json", "50000_100000_36.json", "50000_100000_37.json", "50000_100000_38.json", "50000_100000_39.json", "50000_100000_40.json", "50000_100000_41.json", "50000_100000_42.json", "50000_100000_43.json", "50000_100000_44.json", "50000_100000_45.json", "50000_100000_46.json", "50000_100000_47.json", "50000_100000_48.json", "50000_100000_49.json", "50000_100000_50.json", "100000_150000_1.json", "100000_150000_2.json", "100000_150000_3.json", "100000_150000_4.json", "100000_150000_5.json", "100000_150000_6.json", "100000_150000_7.json", "100000_150000_8.json", "100000_150000_9.json", "100000_150000_10.json", "100000_150000_11.json", "100000_150000_12.json", "100000_150000_13.json", "100000_150000_14.json", "100000_150000_15.json", "100000_150000_16.json", "100000_150000_17.json", "100000_150000_18.json", "100000_150000_19.json", "100000_150000_20.json", "100000_150000_21.json", "100000_150000_22.json", "100000_150000_23.json", "100000_150000_24.json", "100000_150000_25.json", "100000_150000_26.json", "100000_150000_27.json", "100000_150000_28.json", "100000_150000_29.json", "100000_150000_30.json", "100000_150000_31.json", "100000_150000_32.json", "100000_150000_33.json", "100000_150000_34.json", "100000_150000_35.json", "100000_150000_36.json", "100000_150000_37.json", "100000_150000_38.json", "100000_150000_39.json", "100000_150000_40.json", "100000_150000_41.json", "100000_150000_42.json", "100000_150000_43.json", "100000_150000_44.json", "100000_150000_45.json", "100000_150000_46.json", "100000_150000_47.json", "100000_150000_48.json", "100000_150000_49.json", "100000_150000_50.json", "150000_200000_1.json", "150000_200000_2.json", "150000_200000_3.json", "150000_200000_4.json", "150000_200000_5.json", "150000_200000_6.json", "150000_200000_7.json", "150000_200000_8.json", "150000_200000_9.json", "150000_200000_10.json", "150000_200000_11.json", "150000_200000_12.json", "150000_200000_13.json", "150000_200000_14.json", "150000_200000_15.json", "150000_200000_16.json", "150000_200000_17.json", "150000_200000_18.json", "150000_200000_19.json", "150000_200000_20.json", "150000_200000_21.json", "150000_200000_22.json", "150000_200000_23.json", "150000_200000_24.json", "150000_200000_25.json", "150000_200000_26.json", "150000_200000_27.json", "150000_200000_28.json", "150000_200000_29.json", "150000_200000_30.json", "150000_200000_31.json", "150000_200000_32.json", "150000_200000_33.json", "150000_200000_34.json", "150000_200000_35.json", "150000_200000_36.json", "150000_200000_37.json", "150000_200000_38.json", "150000_200000_39.json", "150000_200000_40.json", "150000_200000_41.json", "150000_200000_42.json", "150000_200000_43.json", "150000_200000_44.json", "150000_200000_45.json", "150000_200000_46.json", "150000_200000_47.json", "150000_200000_48.json", "150000_200000_49.json", "150000_200000_50.json", "150000_200000_51.json", "150000_200000_52.json", "150000_200000_53.json", "150000_200000_54.json", "150000_200000_55.json", "150000_200000_56.json", "150000_200000_57.json", "150000_200000_58.json", "150000_200000_59.json", "150000_200000_60.json", "150000_200000_61.json", "150000_200000_62.json", "150000_200000_63.json", "150000_200000_64.json", "150000_200000_65.json", "150000_200000_66.json", "150000_200000_67.json", "150000_200000_68.json", "150000_200000_69.json", "150000_200000_70.json", "150000_200000_71.json", "150000_200000_72.json", "150000_200000_73.json", "150000_200000_74.json", "150000_200000_75.json", "150000_200000_76.json", "150000_200000_77.json", "150000_200000_78.json", "200000_250000_1.json", "200000_250000_2.json", "200000_250000_3.json", "200000_250000_4.json", "200000_250000_5.json", "200000_250000_6.json", "200000_250000_7.json", "200000_250000_8.json", "200000_250000_9.json", "200000_250000_10.json", "200000_250000_11.json", "200000_250000_12.json", "200000_250000_13.json", "200000_250000_14.json", "200000_250000_15.json", "200000_250000_16.json", "200000_250000_17.json", "200000_250000_18.json", "200000_250000_19.json", "200000_250000_20.json", "200000_250000_21.json", "200000_250000_22.json", "200000_250000_23.json", "200000_250000_24.json", "200000_250000_25.json", "200000_250000_26.json", "200000_250000_27.json", "200000_250000_28.json", "200000_250000_29.json", "200000_250000_30.json", "200000_250000_31.json", "200000_250000_32.json", "200000_250000_33.json", "200000_250000_34.json", "200000_250000_35.json", "200000_250000_36.json", "200000_250000_37.json", "200000_250000_38.json", "200000_250000_39.json", "200000_250000_40.json", "200000_250000_41.json", "200000_250000_42.json", "200000_250000_43.json", "200000_250000_44.json", "200000_250000_45.json", "250000_297662_1.json", "250000_297662_2.json", "250000_297662_3.json", "250000_297662_4.json", "250000_297662_5.json", "250000_297662_6.json", "250000_297662_7.json", "250000_297662_8.json", "250000_297662_9.json", "250000_297662_10.json", "250000_297662_11.json", "250000_297662_12.json", "250000_297662_13.json", "250000_297662_14.json", "250000_297662_15.json", "250000_297662_16.json", "250000_297662_17.json", "250000_297662_18.json", "250000_297662_19.json", "250000_297662_20.json", "250000_297662_21.json", "250000_297662_22.json", "250000_297662_23.json", "250000_297662_24.json", "250000_297662_25.json", "250000_297662_26.json", "250000_297662_27.json", "250000_297662_28.json", "250000_297662_29.json", "250000_297662_30.json", "250000_297662_31.json", "250000_297662_32.json", "250000_297662_33.json", "250000_297662_34.json", "250000_297662_35.json", "250000_297662_36.json", "250000_297662_37.json", "250000_297662_38.json", "250000_297662_39.json", "250000_297662_40.json", "250000_297662_41.json", "250000_297662_42.json", "250000_297662_43.json", "250000_297662_44.json", "250000_297662_45.json", "250000_297662_46.json", "250000_297662_47.json"]
    for json_file in json_files:
        json_file_path = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/wiktionary_titles_meanings/json/' + json_file

        with open(json_file_path) as f:
            data = json.load(f)
        for key, value in data.items():
            if key not in concat_json_dict and len(value) != 0:
                concat_json_dict[key] = value
    with open("C:/myProjects/TDI/CapstoneProject/Wiktionary/wiktionary_titles_meanings/concat_temp_repeat_allowed.json", "w") as outfile:  
        json.dump(concat_json_dict, outfile)

def final_run_get_meanings():
    json_file_path = "C:/myProjects/TDI/CapstoneProject/Wiktionary/wiktionary_titles_meanings/concat_temp.json"
    with open(json_file_path) as f:
        concat_temp = json.load(f)
    
    all_ngrams_list = []
    for n in range(10):
        with open('C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n+1) + 'grams.json') as f:
            ngrams = json.load(f)
        for item in ngrams:
            all_ngrams_list.append(item)        
    master_dict = {}

    list_of_words_with_error = []
    for index, title in enumerate(all_ngrams_list):
        if title not in master_dict.keys():
            if title in concat_temp.keys() and len(concat_temp[title]) != 0:
                master_dict[title] = concat_temp[title]
                #print(title, len(title.split()))
            else:
                try:
                    meaning = wik_parser.fetch(title, 'English')
                except:
                    list_of_words_with_error.append(title)
                else:
                    if len(meaning) != 0:
                        master_dict[title] = meaning
                        print(title, meaning)
    print(list_of_words_with_error)
    print(len(list_of_words_with_error))
    print(len(master_dict))
    with open("C:/myProjects/SubtitlePro/Data/wiktionary.json", "w") as outfile:  
        json.dump(master_dict, outfile)                        

def get_wiktionary_summary():
    '''get the summary of word meaning'''
    json_file_path = "C:/myProjects/SubtitlePro/Data/wiktionary.json"
    with open(json_file_path) as f:
        old_wiktionary = json.load(f)
    
    master_dict = {}
    for title, meaning in old_wiktionary.items():
        if isinstance(meaning, list):
            meaning = meaning[0]
            definitions = meaning['definitions']
            temp_dict = {}
            if len(definitions) != 0:
                temp_dict['definitions'] = definitions[0]['text']
                temp_dict['partOfSpeech'] = definitions[0]['partOfSpeech']
                #temp_dict['examples'] = examples
                master_dict[title] = temp_dict
        elif isinstance(meaning, dict):
            master_dict[title] = meaning
        else:
            print('Not list nor dict')


    with open("C:/myProjects/SubtitlePro/Data/wiktionary_summary.json", "w") as outfile:  
        json.dump(master_dict, outfile)

def get_wiktionary_detailed():
    '''get the detailed definitions of word meaning'''
    json_file_path = "C:/myProjects/SubtitlePro/Data/wiktionary.json"
    with open(json_file_path) as f:
        old_wiktionary = json.load(f)
    
    list_of_words_with_error = []
    master_dict = {}
    error_meaning_count = 0 
    new_meaning_count = 0 
    for title, meaning in old_wiktionary.items():
        if isinstance(meaning, list):
            master_dict[title] = meaning
        elif isinstance(meaning, dict):
                try:
                    new_meaning = wik_parser.fetch(title, 'English')
                except:
                    error_meaning_count += 1
                    list_of_words_with_error.append(title)
                    print(title, 'Error meaning count:' , error_meaning_count)
                else:
                    new_meaning_count += 1
                    master_dict[title] = new_meaning
                    print(title, 'New meaning count:' , new_meaning_count)
        else:
            print('Not list nor dict')


    with open("C:/myProjects/SubtitlePro/Data/wiktionary_detailed.json", "w") as outfile:  
        json.dump(master_dict, outfile)

    with open("C:/myProjects/SubtitlePro/Data/wiktionary_detailed_error.json", "w") as outfile:  
        json.dump(list_of_words_with_error, outfile)                






'''
Structure of meanings: 
"inheritors": [
                    {"etymology": "", 
                    "definitions": [
                                    {"partOfSpeech": "noun", "text": ["inheritors", "plural of inheritor"], "relatedWords": [], "examples": []}
                                   ], 
                    "pronunciations": {"text": [], 
                                       "audio": []
                                      }
                    }
              ]
'''


if __name__ == '__main__':

    #get_all_meanings(from_index=from_index, to_index=to_index, batch_from=batch_from)
    #concatenate_all_json_files()
    #final_run_get_meanings()
    #get_wiktionary_summary()
    get_wiktionary_detailed()

    json_file = "C:/myProjects/SubtitlePro/Data/wiktionary_detailed.json"
    with open(json_file) as json_file: 
        data = json.load(json_file)
    print(data['an eye for an eye makes the whole world blind'])   
    print()
    print(data['flight'])   
    print()
    print(data['one\'s'])  
    print()
    #print(data['have to try twice as hard just to stay standing']) 
    print()
    print(data['get'])           
    print(len(data))
    print()

    for i in range(1000):
        input()
        index = np.random.randint(1, len(data))
        word = list(data)[index]
        print(word)
        print(data[word])
        print()
        print(wik_parser.fetch(word, 'English'))
        print()
        print()
        print()
        print()
        