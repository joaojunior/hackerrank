from longest_word_in_dictionary_through_deleting import Solution


def test_example_1():
    s = 'abpcplea'
    dictionary = ['ale', 'apple', 'monkey', 'plea']

    expected = 'apple'
    assert expected == Solution().find_longest_word(s, dictionary)


def test_example_2():
    s = 'abpcplea'
    dictionary = ['a', 'b', 'c']

    expected = 'a'
    assert expected == Solution().find_longest_word(s, dictionary)


def test_empty_solution():
    s = 'zx'
    dictionary = ['ale', 'apple', 'monkey', 'plea']

    expected = ''
    assert expected == Solution().find_longest_word(s, dictionary)
