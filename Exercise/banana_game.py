from Exercise.container import *
import io


def solve_puzzle(step_list: list, word: str, shuffled_word: str, container,
                 word_pointer: int=0, shuffled_pointer: int=0,
                 char: str=None, words='') -> bool:

    needed_char = shuffled_word[shuffled_pointer]
    if char is not None:
        if char != needed_char:
            return False
        else:
            shuffled_pointer += 1
    if shuffled_pointer == len(shuffled_word):
        step_list.append(words[:-1].split(' '))
        return True
    copy_container = container.copy()
    copy_container_2 = container.copy()
    (flag_1, flag_2, flag_3) = (False, False, False)

    if not container.is_empty():
        derived_char = container.extract()
        flag_1 = solve_puzzle(step_list, word, shuffled_word, container,
                              word_pointer, shuffled_pointer, derived_char,
                              words + 'get() ')

    if word_pointer < len(word):
        current_char = word[word_pointer]
        word_pointer += 1
        try:
            copy_container.insert(current_char)
        except ContainerFullError:
            pass
        else:
            flag_2 = solve_puzzle(step_list, word, shuffled_word,
                                  copy_container, word_pointer,
                                  shuffled_pointer, None,
                                  words + 'put('+current_char+') ')
        finally:
            flag_3 = solve_puzzle(step_list, word, shuffled_word,
                                  copy_container_2, word_pointer,
                                  shuffled_pointer, current_char,
                                  words + 'move('+current_char+') ')

    return flag_1 or flag_2 or flag_3


def solve_by_container(word, shuffled_word, container):
    steps = []
    solvable = (solve_puzzle(steps, word, shuffled_word, container))
    if solvable:
        step = min(steps, key=len)
        step = str(step)
        msg = 'It can be solved, and the shortest step is ' + step[:-1] + '.'
    else:
        msg = 'It can not be solved.'
    print(msg)


def read_puzzles(file: io.TextIOWrapper) -> list:
    db = []
    for line in file:
        word = ''
        for letter in line:
            if letter.isalpha():
                word += letter
        db.append(word)
    return db


def solve_puzzle_file(path: str, word: str) -> str:
    file_handler = open(path, 'r')
    puzzle_list = read_puzzles(file_handler)
    file_handler.close()
    containers = [Bucket, Stack, Queue]
    result = ''
    index = 1
    for puzzle in puzzle_list:
        result += str(index) + '\n'
        result += solve_formatted_puzzle(containers, puzzle, word)
        index += 1
    return result[:-1]


def solve_formatted_puzzle(containers: list, scrabbled_word: str, word: str)\
        -> str:
    result = ['']
    for sample in containers:
        container = sample()
        steps = []
        is_solvable = solve_puzzle(steps, word, scrabbled_word, container)
        if is_solvable:
            result[0] += sample.NAME + ' '
            answer = min(steps, key=lambda coll: len(coll))
            answer = sample.NAME + format_output(answer)
            result.append(answer)
    if len(result[0]) == 0:
        msg = 'impossible\n'
    else:
        msg = result[0][:-1] + '\n'
        for x in range(1, len(result)):
            msg += result[x] + '\n'

    return msg


def format_output(output: list) -> str:
    msg = ''
    for step in output:
        msg += ' ' + step
    return msg


output = solve_puzzle_file('banana_game_puzzles.csv', 'BANANA')
out = open('ex1.txt', 'w')
out.write(output)

