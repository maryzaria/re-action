import re


def find_sentence_with_key_word(text):
    # words = ('сопроводительное', 'письмо', 'слово', 'кодовое слово', 'фраза', 'начни', 'напиши', 'отклик', 'внимательно', 'до конца', 'полностью')
    pattern = re.compile(r'(?:сопровод[а-я]+\s+пис[а-я]+|отклик[а-я]*|вним[а-я]+|(кодов[а-я]+)?слов[а-я]*).*?(?:[\"«“]'
                         r'(?P<quotes>[^«“»”\"]+)(?:[\"»”]|\.\.\.)|\s*(?P<non_quotes>[A-ZФ-Я][a-zа-я]+))')
    result = re.findall(pattern, text)
    search = pattern.search(text)
    if search is not None:
        key_word = search.group('quotes') if search.group('quotes') is not None else search.group('non_quotes')
        if len(result) > 1:
            for res in result:
                key_word = res[1] if res[1] else key_word
        return key_word.strip()
    return None


if __name__ == '__main__':
    txt = ''
    print(find_sentence_with_key_word(txt))
