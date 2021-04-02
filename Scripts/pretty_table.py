import ntpath

def are_dict_elements_empty(dictionary):
    count_element = 0
    for key, value in dictionary.items():
        count_element += len(dictionary[key])
    if count_element == 0:
        return True
    else:
        return False

def prettyTable(dictionary, cssClass=''):
    ''' pretty prints a dictionary into an HTML table(s) '''
    if isinstance(dictionary, str):
        return '<td>' + dictionary + '</td>'
    s = []
    s.append('<hr>')
    s.append('<table ')
    if cssClass != '':
        s.append('class="%s"' % (cssClass))
    s.append('>\n')
    for key, value in dictionary.items():
        if value != None and len(value) != 0:
            s.append('<tr>\n  <td valign="top"><strong>  %s                 </strong></td>\n' % str(key))
            if isinstance(value, dict):
                if are_dict_elements_empty(value) == False:
                    if key == 'picture' or key == 'icon':
                        s.append('  <td valign="top"><img src="%s"></td>\n' % prettyTable(value, cssClass))
                    else:
                        s.append('  <td valign="top">%s</td>\n' % prettyTable(value, cssClass))
            elif isinstance(value, list):
                s.append("<td><table>")
                if key == 'audio':
                    for i in value:
                        link = "<a href=https:" + i + ">Listen</a>"
                        s.append('<tr><td valign="top">%s</td></tr>\n' % link)
                else:
                    for i in value:
                        s.append('<tr><td valign="top">%s</td></tr>\n' % prettyTable(i, cssClass))
                s.append('</table>')
            else:
                if key == 'picture' or key == 'icon':
                    s.append('  <td valign="top"><img src="%s"></td>\n' % value)
                else:
                    s.append('  <td valign="top">%s</td>\n' % value)
            s.append('</tr>\n')
    s.append('</table>')

    return '\n'.join(s).replace('partOfSpeech', 'type')

def generate_html_from_dictionary(dictionary, output_html_path):
    with open(output_html_path, 'w', encoding='utf-8') as filehandle:
        for listitem in prettyTable(dictionary, cssClass=''):
            filehandle.write(listitem)  
    return ntpath.basename(output_html_path)


if __name__ == '__main__':

    dictionary = {'hi':{"boyo":{"definitions":["boyo (plural boyos)","(Ireland) A boy or lad.","(sometimes derogatory) A stereotypically Welsh form of address for a man, usually younger than the speaker."],"examples":[],"partOfSpeech":"noun"},"doorframe":{"definitions":["doorframe (plural doorframes)","The frame into which a door is fitted."],"examples":[],"partOfSpeech":"noun"},"fascinate":{"definitions":["fascinate (third-person singular simple present fascinates, present participle fascinating, simple past and past participle fascinated)","To evoke an intense interest or attraction in someone.","To make someone hold motionless; to spellbind.","To be irresistibly charming or attractive to."],"examples":[],"partOfSpeech":"verb"},"forthe":{"definitions":["forthe (not comparable)","Obsolete spelling of forth"],"examples":[],"partOfSpeech":"adverb"},"gangway":{"definitions":["gangway (plural gangways)","A passageway through which to enter or leave, such as one between seating areas in an auditorium, or between two buildings.","An articulating bridge or ramp, such as from land to a dock or a ship.","A temporary passageway, such as one made of planks.","(rare, obsolete outside dialects) A clear path through a crowd or a passageway with people.","(Britain) An aisle.","(nautical) A passage along either side of a ship's upper deck.","(nautical) A passage through the side of a ship or an opening in the railing through which the ship may be boarded.","(agricultural) An earthen and plank ramp leading from the stable yard into the upper storey or mow of a dairy barn.","(Chicago) The narrow space between two buildings or houses, used to access the backyard/alleyway from the front.","A passageway through a passenger car"],"examples":[],"partOfSpeech":"noun"},"goddamned":{"definitions":["goddamned (not comparable)","(derogatory) Damned by God.","(often offensive) Used as an intensifier expressing anger."],"examples":[],"partOfSpeech":"adjective"},"halfa":{"definitions":["halfa (uncountable)","Synonym of esparto (\u201cNorth African grass\u201d)"],"examples":[],"partOfSpeech":"noun"},"impugn":{"definitions":["impugn (third-person singular simple present impugns, present participle impugning, simple past and past participle impugned)","(transitive, obsolete) To assault, attack.","(transitive) To verbally assault, especially to argue against an opinion, motive, or action; to question the truth or validity of."],"examples":[],"partOfSpeech":"verb"},"ofan":{"definitions":["ofan (plural ofanim)","Alternative form of ophan"],"examples":[],"partOfSpeech":"noun"},"presumptuous":{"definitions":["presumptuous (comparative more presumptuous, superlative most presumptuous)","Going beyond what is right, proper, or appropriate because of an excess of self-confidence or arrogance."],"examples":[],"partOfSpeech":"adjective"},"purser":{"definitions":["purser (plural pursers)","The person responsible for handling the accounts on a ship, or for dealing with the passengers on a ship or aircraft."],"examples":[],"partOfSpeech":"noun"},"regale":{"definitions":["regale (plural regales)","A feast, meal."],"examples":[],"partOfSpeech":"noun"},"rootless":{"definitions":["rootless (comparative more rootless, superlative most rootless)","Of a plant or another thing, having no roots.","Being a wanderer; having no ties to a particular locale.","(computing) Without (the use of) a root user account."],"examples":[],"partOfSpeech":"adjective"},"shipbuilder":{"definitions":["shipbuilder (plural shipbuilders)","A person who builds vessels such as ships and boats.","A firm that specializes in building ships."],"examples":[],"partOfSpeech":"noun"},"sidesaddle":{"definitions":["sidesaddle (plural sidesaddles)","A saddle, usually for a woman, in which the rider sits with both legs on the same side of the horse."],"examples":[],"partOfSpeech":"noun"},"sping":{"definitions":["sping (plural spings)","(Internet) The use of blogs' trackback functionality to generate link spam."],"examples":[],"partOfSpeech":"noun"},"stairwell":{"definitions":["stairwell (plural stairwells)","A shaft in a multi-story building enclosing a stairway or staircase."],"examples":[],"partOfSpeech":"noun"},"steerage":{"definitions":["steerage (countable and uncountable, plural steerages)","(uncountable) The art of steering.","(countable) The section of a passenger ship that provided inexpensive accommodation with no individual cabins.","(countable) The effect of the helm on a ship."],"examples":[],"partOfSpeech":"noun"},"uncouth":{"definitions":["uncouth (comparative uncouther or more uncouth, superlative uncouthest or most uncouth)","(archaic) Unfamiliar, strange, foreign.","Clumsy, awkward.","Unrefined, crude."],"examples":[],"partOfSpeech":"adjective"},"unsinkable":{"definitions":["unsinkable (comparative more unsinkable, superlative most unsinkable)","Of a ship: that cannot be sunk.","(figuratively) That cannot be overcome or defeated."],"examples":[],"partOfSpeech":"adjective"}}}
    out_html = 'file.html'

    sample_wiktionary_entry = {
        "ab off": {
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
            "pronunciations": {"text": [], "audio": []}},
        "boyo":{"definitions":["boyo (plural boyos)","(Ireland) A boy or lad.","(sometimes derogatory) A stereotypically Welsh form of address for a man, usually younger than the speaker."],"examples":[],"partOfSpeech":"noun"},"doorframe":{"definitions":["doorframe (plural doorframes)","The frame into which a door is fitted."],"examples":[],"partOfSpeech":"noun"},"fascinate":{"definitions":["fascinate (third-person singular simple present fascinates, present participle fascinating, simple past and past participle fascinated)","To evoke an intense interest or attraction in someone.","To make someone hold motionless; to spellbind.","To be irresistibly charming or attractive to."],"examples":[],"partOfSpeech":"verb"},"forthe":{"definitions":["forthe (not comparable)","Obsolete spelling of forth"],"examples":[],"partOfSpeech":"adverb"},"gangway":{"definitions":["gangway (plural gangways)","A passageway through which to enter or leave, such as one between seating areas in an auditorium, or between two buildings.","An articulating bridge or ramp, such as from land to a dock or a ship.","A temporary passageway, such as one made of planks.","(rare, obsolete outside dialects) A clear path through a crowd or a passageway with people.","(Britain) An aisle.","(nautical) A passage along either side of a ship's upper deck.","(nautical) A passage through the side of a ship or an opening in the railing through which the ship may be boarded.","(agricultural) An earthen and plank ramp leading from the stable yard into the upper storey or mow of a dairy barn.","(Chicago) The narrow space between two buildings or houses, used to access the backyard/alleyway from the front.","A passageway through a passenger car"],"examples":[],"partOfSpeech":"noun"},"goddamned":{"definitions":["goddamned (not comparable)","(derogatory) Damned by God.","(often offensive) Used as an intensifier expressing anger."],"examples":[],"partOfSpeech":"adjective"},"halfa":{"definitions":["halfa (uncountable)","Synonym of esparto (\u201cNorth African grass\u201d)"],"examples":[],"partOfSpeech":"noun"},"impugn":{"definitions":["impugn (third-person singular simple present impugns, present participle impugning, simple past and past participle impugned)","(transitive, obsolete) To assault, attack.","(transitive) To verbally assault, especially to argue against an opinion, motive, or action; to question the truth or validity of."],"examples":[],"partOfSpeech":"verb"},"ofan":{"definitions":["ofan (plural ofanim)","Alternative form of ophan"],"examples":[],"partOfSpeech":"noun"},"presumptuous":{"definitions":["presumptuous (comparative more presumptuous, superlative most presumptuous)","Going beyond what is right, proper, or appropriate because of an excess of self-confidence or arrogance."],"examples":[],"partOfSpeech":"adjective"},"purser":{"definitions":["purser (plural pursers)","The person responsible for handling the accounts on a ship, or for dealing with the passengers on a ship or aircraft."],"examples":[],"partOfSpeech":"noun"},"regale":{"definitions":["regale (plural regales)","A feast, meal."],"examples":[],"partOfSpeech":"noun"},"rootless":{"definitions":["rootless (comparative more rootless, superlative most rootless)","Of a plant or another thing, having no roots.","Being a wanderer; having no ties to a particular locale.","(computing) Without (the use of) a root user account."],"examples":[],"partOfSpeech":"adjective"},"shipbuilder":{"definitions":["shipbuilder (plural shipbuilders)","A person who builds vessels such as ships and boats.","A firm that specializes in building ships."],"examples":[],"partOfSpeech":"noun"},"sidesaddle":{"definitions":["sidesaddle (plural sidesaddles)","A saddle, usually for a woman, in which the rider sits with both legs on the same side of the horse."],"examples":[],"partOfSpeech":"noun"},"sping":{"definitions":["sping (plural spings)","(Internet) The use of blogs' trackback functionality to generate link spam."],"examples":[],"partOfSpeech":"noun"},"stairwell":{"definitions":["stairwell (plural stairwells)","A shaft in a multi-story building enclosing a stairway or staircase."],"examples":[],"partOfSpeech":"noun"},"steerage":{"definitions":["steerage (countable and uncountable, plural steerages)","(uncountable) The art of steering.","(countable) The section of a passenger ship that provided inexpensive accommodation with no individual cabins.","(countable) The effect of the helm on a ship."],"examples":[],"partOfSpeech":"noun"},"uncouth":{"definitions":["uncouth (comparative uncouther or more uncouth, superlative uncouthest or most uncouth)","(archaic) Unfamiliar, strange, foreign.","Clumsy, awkward.","Unrefined, crude."],"examples":[],"partOfSpeech":"adjective"},"unsinkable":{"definitions":["unsinkable (comparative more unsinkable, superlative most unsinkable)","Of a ship: that cannot be sunk.","(figuratively) That cannot be overcome or defeated."],"examples":[],"partOfSpeech":"adjective"}
    }

    #with open('file.html', 'w') as filehandle:
    #    for listitem in prettyTable(sample_wiktionary_entry, cssClass=''):
    #        filehandle.write(listitem)  

    generate_html_from_dictionary(sample_wiktionary_entry, 'file.html')