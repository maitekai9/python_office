
def find_str_index(sentence, count, start, sep=' '):
    if count == 0:
        return sentence.find(sep, start)
    index = sentence.find(sep, start)
    return find_str_index(sentence, count - 1, index + 1)