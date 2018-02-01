from Exercise.container_2 import *


def banana_verify(source, goal, container, moves):
    (cursor, move_index) = (0, 0)
    (len_of_move, len_of_source) = (len(moves), len(source))
    construct_word = ''
    is_match = True
    while move_index < len_of_move and is_match:
        move = moves[move_index]
        if move == 'P' and cursor < len_of_source:
            try:
                container.put(source[cursor])
            except ContainerFullException:
                is_match = False
        elif move == 'M' and cursor < len_of_source:
            construct_word += source[cursor]
        elif move == 'G' and not container.is_empty():
            construct_word += container.get()
            cursor -= 1
        else:
            is_match = False
        cursor += 1
        move_index += 1
    print(construct_word)
    return is_match and construct_word == goal


flag = banana_verify('BANANA', 'AAANNB', Stack(),
                     ['P', 'M', 'P', 'M', 'P', 'M', 'G', 'G', 'G', 'G'])
print(flag)
