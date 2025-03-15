def count_words(words):
    words_list = words.split()
    word_count = len(words_list)
    return word_count

def count_characters(words):
    character_list = list(words)
    character_count = {}
    for character in character_list:
        if character_count[character] == None:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

print(count_characters("Hello there friendo!"))