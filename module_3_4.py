
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.upper().count(word.upper()) or word.upper().count(root_word.upper()):
            same_words.append(word)
            continue
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
