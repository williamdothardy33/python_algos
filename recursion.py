def countdown(n):
    if n < 0:
        return None
    else:
        print(n)
        countdown(n - 1)

def test_countdown():
    countdown(10)

def print_nested(ns, ns_length):
    pointer = 0
    while pointer < ns_length:
        current = ns[pointer]
        if isinstance(current, int):
            print(current)
        else:
            print_nested(current, len(current))
        pointer += 1
    
def test_print_nested():
    ns = [1,2,3,
        [4,5,6], 7,
        [8, [9,10,11, [12,13,14]]],
        [15,16,17,18,19, [20,21,22, [23,24,25, [26,27,29]], 30,31], 32], 33]
    
    print_nested(ns, len(ns))

# top down sum
def sum(ns, ns_length, start = 0):
    if start >= ns_length:
        return 0
    else:
        return ns[start] + sum(ns, ns_length, start + 1)

def test_sum():
    ns = [1,2,3,4,5,6,7,8,9,10]
    print(sum(ns, len(ns)))

def count_paths(num_steps):
    # not enough steps for the jump 
    if num_steps < 0:
        return 0
    # reached the bottom
    elif num_steps == 0:
        return 1
    else:
        # the way this works is if we cannot 'jump' 1, 2, or 3 steps then we are already at the bottom (that counts as one way to reach the bottom)
        # the first recursive call gets executed and returns the number of ways to reach the bottom if my first "jump" is one step and my other
        # 'jumps' are some combination of1, 2, and 3 steps. when I reach the top of the call tree the second recursive call gets executed and
        # similarly my first 'jump' is 2 steps and the my next step is some combination of 1, 2, or 3 steps etc.
        return count_paths(num_steps - 1) + count_paths(num_steps - 2) + count_paths(num_steps - 3)


def test_count_paths():
    print(f'0 steps: {count_paths(0)}')
    print(f'1 steps: {count_paths(1)}')
    print(f'2 steps: {count_paths(2)}')
    print(f'3 steps: {count_paths(3)}')
    print(f'4 steps: {count_paths(4)}')
    print(f'5 steps: {count_paths(5)}')

def remove_letter(ls, index):
    result = ''
    ls_pointer = 0
    while ls_pointer < len(ls):
        if ls_pointer != index:
            result += ls[ls_pointer]
        
        ls_pointer += 1
    return result

def anagram(ls, exclude_pointer = None):
    start = ls
    # creates substring with letter excluded at excluded_pointer if it isn't the default None
    # and reassign start
    if exclude_pointer is not None:
        substring = remove_letter(ls, exclude_pointer)
        start = substring
        

    # base case anagram of one letter is itself
    if len(start) == 1:
        return [start]
    else:
        result = []
        letter_pointer = 0
        while letter_pointer < len(start):
            current_letter = start[letter_pointer]
            # for every recursive call made an option for a letter is eliminated until we get to 1 letter
            # and then we append the entrie(s) from the array return from next stack frame to the letter that we excluded in the previous stack frame and then do the same with
            # the left over letters so that for every 'slot' in the original string we have 'cycled' through all possible letters
            sub_anagrams = anagram(start, letter_pointer)
            sub_pointer = 0
            while sub_pointer < len(sub_anagrams):
                sub_anagram = sub_anagrams[sub_pointer]
                result.append(current_letter + sub_anagram)
                sub_pointer += 1
            letter_pointer += 1
        return result
    
def anagram_v2(ls: str):
    if len(ls) == 1:
        return [ls]
    else:
        result = []
        for idx, l in enumerate(ls):
            sub_anagrams = anagram_v2(ls[:idx] + ls[idx + 1:])
            for sub_anagram in sub_anagrams:
                result.append(l + sub_anagram)
        return result
    





def test_anagram():
    ls = 'abcd'
    print(anagram_v2(ls))


def array_strlen_sum(ss, pointer = 0):
    if pointer >= len(ss):
        return 0
    else:
        return len(ss[pointer]) + array_strlen_sum(ss, pointer + 1)

def test_array_strlen_sum():
    ss = ['ab', 'c', 'def', 'ghij']
    print(array_strlen_sum(ss))


def evens(ns, result: list = [], pointer = 0):
    if pointer >= len(ns):
        return result
    else:
        current = ns[pointer]
        if current % 2 == 0:
            result.append(current)
            return evens(ns, result, pointer + 1)
        else:
            return evens(ns, result, pointer + 1)

def test_evens():
    ns = [1,2,8,9, 11, 14, 22, 35]
    print(evens(ns))


def triangular(n):
    if n <= 1:
        return 1
    else:
        return n + triangular(n - 1)

def test_triangular():
    n = 7
    print(triangular(7))



def index_of_x(s, pointer = 0):
    if pointer >= len(s):
        return -1
    else:
        if s[pointer] == 'x':
            return pointer
        else: 
            return index_of_x(s, pointer + 1)
        
def test_index_of_x():
    s = 'abcdefghijklmnopqrstuvwxyz'
    print(index_of_x(s))

test_index_of_x()


    






