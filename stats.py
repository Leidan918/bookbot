def count_words(words):
    words_list = words.split()
    word_count = len(words_list)
    return word_count

def count_characters(words):
    character_list = list(words)
    character_count = {}
    for character in character_list:
        if character.lower() not in character_count:
            character_count[character.lower()] = 1
        else:
            character_count[character.lower()] += 1
    return character_count

def sort_char(char_list):
    sorted_char_list = {key: val for key, val in sorted(char_list.items(), key = lambda ele: ele[1], reverse = True)}

    return sorted_char_list