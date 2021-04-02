

def get_dictionary_meaning(words, dictionary_dictionary):
    if words in dictionary_dictionary.keys():
        meaning_dict = dictionary_dictionary[words]
        return meaning_dict
    else:
        return None
