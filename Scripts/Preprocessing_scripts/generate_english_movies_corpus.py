import zipfile
import os
from pathlib import Path
import pysrt
import glob
import json

import re 
import pickle
import time
import random

def generate_text_of_all_movies():
    encodings = [ "ascii", "big5", "big5hkscs", "cp037", "cp424", "cp437", "cp500", "cp720", "cp737", "cp775", "cp850", "cp852", "cp855", "cp856", "cp857", "cp858", "cp860", "cp861", "cp862", "cp863", "cp864", "cp865", "cp866", "cp869", "cp874", "cp875", "cp932", "cp949", "cp950", "cp1006", "cp1026", "cp1140", "cp1250", "cp1251", "cp1252", "cp1253", "cp1254", "cp1255", "cp1256", "cp1257", "cp1258", "euc_jp", "euc_jis_2004", "euc_jisx0213", "euc_kr", "gb2312", "gbk", "gb18030", "hz", "iso2022_jp", "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_2004", "iso2022_jp_3", "iso2022_jp_ext", "iso2022_kr", "latin_1", "iso8859_2", "iso8859_3", "iso8859_4", "iso8859_5", "iso8859_6", "iso8859_7", "iso8859_8", "iso8859_9", "iso8859_10", "iso8859_13", "iso8859_14", "iso8859_15", "iso8859_16", "johab", "koi8_r", "koi8_u", "mac_cyrillic", "mac_greek", "mac_iceland", "mac_latin2", "mac_roman", "mac_turkish", "ptcp154", "shift_jis", "shift_jis_2004", "shift_jisx0213", "utf_32", "utf_32_be", "utf_32_le", "utf_16", "utf_16_be", "utf_16_le", "utf_7", "utf_8", "utf_8_sig"]
    word_dir = 'C:/myProjects/TDI/CapstoneProject/srt/Corpus/'
    zip_srt_files = glob.glob("C:/myProjects/TDI/CapstoneProject/srt/MSO_subtitles/*.zip")

    corpus_dictionary = {}
    for zip_srt_file in zip_srt_files:
        file_name = os.path.basename(zip_srt_file)
        imov, isub = file_name[:-4].split('-')
        imov = int(imov[5:])
        isub = int(isub[5:])
        print(imov, isub)
        try:
            with zipfile.ZipFile(zip_srt_file, 'r') as zip_ref:
                zip_ref.extractall(word_dir + 'temp_srt/')
        except:
            pass
        else:
            movie_subtitle_list = []
            srt_files = [x for x in Path(r'C:/myProjects/TDI/CapstoneProject/srt/Corpus/temp_srt').glob('**/*') if x.is_file()]
            for srt_file in srt_files:
                is_encode = False
                for encode in encodings:
                    try:
                        subs = pysrt.open(srt_file, encoding=encode)
                    except:
                        is_encode = False
                        pass
                    else:
                        is_encode = True
                        for sub in subs:
                            sub_newline_split = sub.text.split('\n')
                            for i in range(len(sub_newline_split)):
                                if sub_newline_split[i][0:2] == '- ':
                                    sub_newline_split[i] = sub_newline_split[i][2:]
                            movie_subtitle_list.append(' '.join(sub_newline_split))

                    if is_encode == True:
                        #print('Info: the first accepted encoding for this srt file is', encode, '(', srt_file, ')')
                        break
                os.remove(srt_file)
            corpus_dictionary[imov] = {isub : movie_subtitle_list}

    with open("corpus.json", "w") as outfile:  
        json.dump(corpus_dictionary, outfile)

def clean_up_corpus():
    with open("C:/myProjects/TDI/CapstoneProject/srt/Corpus/corpus.json") as json_file: 
        data = json.load(json_file)   
    clean_corpus = []
    for imov, value in data.items():
            isub = list(data[imov].keys())[0]
            text_list = value[isub]
            for line in text_list:

                line = line.replace('- ', '')
                line = line.replace(' -', '')
                line = line.replace('....', ' ')
                line = line.replace('...', ' ')
                line = line.replace('..', ' ')
                line = line.replace('#', '')
                line = line.replace('www.moviesubtitles.org', '')
                line = re.sub("[\[\(\<\{].*?[\]\)\>\}]", "", line)
                try:
                    first_char = line[0]
                except:
                    pass
                else:
                    if first_char == '-':
                        line = line[1:]
                if line.isspace() == False:
                    clean_corpus.append(line)
    with open('C:/myProjects/TDI/CapstoneProject/srt/Corpus/clean_corpus.txt', 'wb') as fp:
        pickle.dump(clean_corpus, fp)


def examine_corpus():
    with open ('C:/myProjects/TDI/CapstoneProject/srt/Corpus/clean_corpus.txt', 'rb') as fp:
        corpus_list = pickle.load(fp)

    while True:
        time.sleep(0.5)
        i = int(random.randint(0,len(corpus_list)))
        print(corpus_list[i])
        print()
        #inp = input()

     

if __name__ == '__main__':        
    #generate_text_of_all_movies()
    #clean_up_corpus()
    #examine_corpus()
    print(get_movie_lines_list('C:/myProjects/TDI/CapstoneProject/srt/other/12AngryMen.srt'))
    exit()

    with open("C:/myProjects/TDI/CapstoneProject/srt/Corpus/corpus.json") as json_file: 
        data = json.load(json_file)   

    while True:
        imov = input()
        if imov == '':
            imov = str(random.randint(0,len(data)))
        else:
            imov = str(imov)
        try:
            isub = list(data[imov].keys())[0]
            text_list = data[imov][isub]
            rand = random.randint(0,len(text_list))
            print(text_list[rand])
            print()
        except:
            pass