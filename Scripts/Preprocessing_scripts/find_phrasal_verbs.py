import json
import nltk

def get_frequency_of_phrasal_verb_components():
    with open('C:/myProjects/SubtitlePro/Data/phrasal_verbs_meaning.json') as f:
        phrasal_verbs = json.load(f)

    words = []
    for phrasal_verb, meaning in phrasal_verbs.items():
        for word in phrasal_verb.split(" "):
            words.append(word)

    word_frequency_dict = {}
    freq = nltk.FreqDist(words)
    freq.plot(100, cumulative=False, )

    for word, frequency in freq.most_common():
            word_frequency_dict[word] = frequency
    print(word_frequency_dict)

def generate_phrasal_verbs_tenses():
    with open('C:/myProjects/SubtitlePro/Data/phrasal_verbs_meaning.json') as f:
        phrasal_verbs = json.load(f)

    phrasal_verbs_tenses = {}
    for phrasal_verb, meaning in phrasal_verbs.items():
        all_tenses = []
        #all_tenses.append(phrasal_verb)
        verb_tenses_string = meaning[0]['definitions'][0]['text'][0]
        verb_tenses_string = verb_tenses_string.replace(')', '')
        try:
            split_by_comma_list = verb_tenses_string.split('(')[1].split(',')
        except:
            pass
        else:
            for item in split_by_comma_list:
                verb = item.replace('third-person singular simple present ','')
                verb = verb.replace('simple past and past participle ','')
                verb = verb.replace('present participle ','')
                verb = verb.replace('past participle ','')
                verb = verb.replace('simple past ','')
                verb = verb.replace('plural ','')
                verb = verb.replace('comparative ','')
                verb = verb.replace('superlative ','')
                verb = verb.replace('countable and uncountable','')
                verb = verb.strip()
                for split_by_or_item in verb.split(' or '):
                    if len(split_by_or_item.split(" ")) >= 2:
                        all_tenses.append(split_by_or_item)
        phrasal_verbs_tenses[phrasal_verb] =  all_tenses       

    #print(phrasal_verbs_tenses)
    with open("C:/myProjects/SubtitlePro/Data/phrasal_verbs_tenses.json", 'w') as json_file: 
        json.dump(phrasal_verbs_tenses, json_file) 

def get_phrasal_verbs(imov):
    with open('C:/myProjects/SubtitlePro/Data/phrasal_verbs_meaning.json') as f:
        phrasal_verbs = json.load(f)

    with open('C:/myProjects/SubtitlePro/Data/phrasal_verbs_tenses.json') as f:
        phrasal_verbs_tenses = json.load(f)        

    with open("C:/myProjects/TDI/CapstoneProject/srt/Corpus/corpus.json") as json_file: 
        movies_corpus = json.load(json_file) 

    imov = str(imov)
    isub = list(movies_corpus[imov].keys())[0]
    movie_text_list = movies_corpus[imov][isub]

    for text in movie_text_list:
        for verb, tenses in phrasal_verbs_tenses.items():
            if " " + verb + " " in text:
                print(verb, '  ---------->  ', text)
            else:
                for tense in tenses:
                    if " " + tense + " " in text:
                        print(tense, '  ---------->  ', text)

    



if __name__ == '__main__':
    get_frequency_of_phrasal_verb_components()
    #generate_phrasal_verbs_tenses()
    #get_phrasal_verbs(200)