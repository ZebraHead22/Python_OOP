import statistics
# def celsius_to_fahrenheit(celsius: float = 36.6) -> float:
#     """
#     Convert Celsius temperature to fahrenheit temperature

#     :param celsius: Convert Celsius 
#     :type celsius: float
#     :return: Fahrenheit temperature
#     :rtype: float
#     """
#     return (celsius*9/5)+32 if isinstance(celsius, (float, int)) else print('FLOAT or INT type is needed!')


# def convert_temperature(value : float, from_unit : str, to_unit : str) -> float:
#     result = (value*9/5)+32 # конвертация из Цельсия в Фаренгейт
#     result = (value-32)*(5/9) # конвертация из Фаренгейта в Цельсий
#     result = value+273.15 # конвертация из Цельсия в Кельвины
#     return result

# convert_temperature(40, 'K', 'C')


def analyze_text(text : str) -> dict:
    
    # my_dict = dict()
    # words = text.split()
    # word_count = len(words)
    # my_dict['word_count'] = word_count
    # a = 0
    # longest_word = ''
    # for i in words: 
    #     if len(i) > a:
    #         a = len(i)
    #         longest_word = i
    # my_dict['longest_word'] = longest_word
    # b = 0
    # for i in words: 
    #     b += len(i)
    # average_word_length = b/word_count 
    # my_dict['average_word_length'] = average_word_length
    # return my_dict

    return {
        'word_count' : len(text.split()),
        'longest_word' : max(text.split(), key=len),
        'average_word_length' : sum([len(i) for i in text.split()])/len(text.split())
    }


result = analyze_text('Для создания заявки на конкурс в качестве руководителя следует')
print(result)