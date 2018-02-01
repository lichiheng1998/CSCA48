def greeting(name: str) -> str:
    """(str) -> str
    Given the name of the person, return the greeting message which
    involves the name provided.
    >>> greeting('Adam')
    'Hello Adam how are you today?'
    """
    return 'Hello ' + name + ' how are you today?'


def mutate_list(my_list: list) -> None:
    """(list) -> NoneType
    Given a list, mutate the list with the defined rule. The integer in
    the list will be multiplied by two, the boolean will be negated, the
    first and the last element will be removed, and the first element
    will be set to the string 'Hello'.
    REQ: there should at least have one elements in the given list.
    REQ: the str in the list should at least have two characters.
    >>> my_list = [3, True, 5, 'great']
    >>> mutate_list(my_list)
    >>> my_list
    ['Hello', False, 10, 'rea']
    """
    # Mutate the first element to be the str 'Hello'.
    my_list[0] = 'Hello'
    # Traverse the list from the second element.
    for index in range(1, len(my_list)):
        value = my_list[index]
        # If the current element is a boolean, reverse the boolean.
        if isinstance(value, bool):
            my_list[index] = not value
        # If the current element is a integer, multiply the integer by two.
        elif isinstance(value, int):
            my_list[index] = value * 2
        # If the current element is a str, remove the first and the last
        # character.
        elif isinstance(value, str):
            my_list[index] = value[1:-1]


def merge_dicts(dict_one: dict, dict_two: dict) -> dict:
    """({str: list of ints}, str: list of ints}) -> str: list of ints}
    Given two dictionaries, merge two dictionaries by adding all keys and
    value pairs to the new dictionary. If two dictionaries have the same
    key, append the value in the list of the second dictionary to the list
    of the first dictionary which corresponds to that key.
    >>> dict_one = {'a': [4, 1, 2], 'b': [1,3], 'c': [5]}
    >>> dict_two = {'d': [7], 'c': [5, 6, 7]}
    >>> new_dict = merge_dicts(dict_one, dict_two)
    >>> new_dict == {'a': [4, 1, 2], 'b': [1,3], 'c': [5, 5, 6, 7], 'd': [7]}
    True
    """
    # Construct a new dictionary
    new_dict = {}
    # Copy all values in the dictionary one to the new dictionary.
    new_dict.update(dict_one)
    # Traverse all keys in the dictionary two.
    for key in dict_two:
        # Get the corresponding value.
        value = dict_two[key]
        if key in new_dict:
            # If the key is already in the new dictionary, extend all integers
            # in the list of the second dictionary to the list of the the new
            # dictionary.
            new_dict[key].extend(value)
        else:
            # Otherwise insert the key value pair to the new dictionary.
            new_dict[key] = value
    # Return the new dictionary.
    return new_dict
