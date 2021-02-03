import numpy

word_matrix = [['a', 'r', 'r', 'a', 'y', 'i', 'p', 'o', 'u', 't'],
['r', 'l', 'm', 'p', 'y', 'u', 'o', 'b', 'u', 'n'],
['s', 't', 'r', 'i', 'n', 'g', 'i', 'l', 'w', 'l'],
['x', 'o', 'x', 'n', 't', 'o', 'n', 'a', 'h', 's'],
['u', 'v', 'w', 't', 'o', 'l', 't', 's', 'i', 't'],
['r', 'e', 't', 'u', 'r', 'n', 'e', 'u', 'l', 'w'],
['b', 'z', 'a', 'z', 'y', 'e', 'r', 'm', 'e', 's'],
['f', 'u', 'l', 'c', 'z', 'i', 'o', 'r', 't', 'u'],
['o', 'a', 'm', 'k', 'd', 'o', 'u', 'b', 'l', 'e'],
['r', 'f', 'u', 'w', 'z', 'x', 'd', 'd', 'x', 'y']]


def search_ten(ten_str):            # takes vector containing 10 1-letter strings, checks for usual suspects,
    # returns list of [word, position]
    candidates = ["string", "pointer", "array", "for", "while", "double", "return"]
    result_list = []
    for word in candidates:
        test = []
        test.extend(word)
        test_length = len(test)
        search_length = 11 - test_length
        flags = [True]*search_length
        for offset in range(0, search_length):
            offset_flag = True
            for pointer in range(0, test_length):
                if ten_str[pointer + offset] != test[pointer]:
                    offset_flag = False
            flags[offset] = offset_flag
        if numpy.sum(flags):
            for position in range(0, search_length):
                if flags[position]:
                    result_list.append([word, position])
        print(result_list)


search_ten(['a', 'f', 'o', 'r', 'y', 'w', 'h', 'i', 'l', 'e'])


def search(searched_term, word_matrix):
    directions = ["east", "south", "west", "north"]
    for dir in directions:
        if dir == "east":
            for running_index in range(0, 10):
                ten_string = ["A"] * 10
                for letters in range(0, 10):
                    ten_string[letters] = word_matrix[running_index][letters]





