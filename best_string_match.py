# notes: for the next algorithm, given a pattern string p and a text string t
# we would like to find the minimum number of operations needed to transform p into t.
# the intuition behind this algorithm is that if we have the minimum number of operations for
# transforming init(p) = p_0p_1...p_(n - 1) to the text string t then to find the minimum number of operations for transforming
# entire string can be computed. there are 3 transformations that is considered when trying to transform a pattern
# string into text string that will contribute to the cost (number of operations). 
# we can either insert, delete, or match/substitute a character. translated into
# code at each point in the pattern string we can move the cursor over a character in the pattern string while holding the cursor
# for the text in the same position and pay the cost. this is equivalent to deleting the skipped over character into the pattern
#  string we could move the cursor over a character in the text string while holding the cursor for the pattern string in the same 
# position and pay the cost. this is equivalent to inserting the character in the pattern string. or we could move both cursors 
# over a character in both the pattern and text string. this is equivalent to a matching/substitution and paying the cost. at each 
# point in the pattern string every possible arrangement of these choices (with replacement) up until the cursor will be made 
# (via recursion) given one of the three choices at the cursor point and a minimum cost will be chosen. I believe a match is the
#  same as an insert followed by a delete or a delete followed by an insert in terms argument parameters so there will be overlap. 
# it is important to note that while skipping over a character is interpreted as either an insert or delete this is just an 
# interpretation and the algorithm can be modified and a different interpretation is possible. The algorithm essentially 
# matches/substitutes whatever character it can skipping over characters in either pattern or text string if it is worth it 
# to do so it terms of the penalty function used while preferring (less cost) to match characters at the beginning of the text 
# string. for example if t = 'spatula' and p = 'ate' you probably end up with something like __ate__ where the first 2 characters
# of t are skipped over the next 2 are matched the next one is substituted and the final two are skipped over for a total of 5 
# operations



def insert_penalty(c) -> int:
    return 1

def delete_penalty(c) -> int:
    return 1

def match_penalty(c1, c2) -> int:
    if c1 == c2:
        return 0
    return 1

def monotone_match_penalty(c1, c2):
    if c1 == c2:
        return 0
    else:
        return insert_penalty(c2) + delete_penalty(c1) + 1
    
def min_operations_recur(pattern: str, text: str, i: int, j: int, op, p_op, t_op) -> int:
    MATCH = 0
    INSERT = 1
    DELETE = 2
    operations_count = [0] * 3
    # case where pattern string is empty
    if i == 0:
        return j * t_op(' ') #cost to insert characters into pattern string
    
    # case where text string is empty
    if j == 0:
        return i * p_op(' ') #cost to delete characters from pattern string
    
    operations_count[MATCH] = min_operations_recur(pattern, text, i - 1, j - 1, op, p_op, t_op) + op(pattern[i], text[j])
    operations_count[INSERT] = min_operations_recur(pattern, text, i, j - 1, op, p_op, t_op) + t_op(text[j])
    operations_count[DELETE] = min_operations_recur(pattern, text, i - 1, j, op, p_op, t_op) + p_op(pattern[i])

    min_operations = operations_count[MATCH]

    for operation in [INSERT, DELETE]:
        if operations_count[operation] < min_operations:
            min_operations = operations_count[operation]
    return min_operations




def min_operations_cached(pattern: str, text: str, i: int, j: int, op, p_op, t_op, cache) -> int:
    MATCH = 0
    INSERT = 1
    DELETE = 2
    operations_count = [0] * 3
    if cache[i][j] is None:
        operations_count[MATCH] = min_operations_cached(pattern, text, i - 1, j - 1, op, p_op, t_op, cache) + op(pattern[i], text[j])
        operations_count[INSERT] = min_operations_cached(pattern, text, i, j - 1, op, p_op, t_op, cache) + t_op(text[j])
        operations_count[DELETE] = min_operations_cached(pattern, text, i - 1, j, op, p_op, t_op, cache) + p_op(pattern[i])

        min_operations = operations_count[MATCH]

        for operation in [INSERT, DELETE]:
            if operations_count[operation] < min_operations:
                min_operations = operations_count[operation]

        cache[i][j] = min_operations

    return cache[i][j]

class cell:
    def __init__(self, cost, parent) -> None:
        self.cost = cost
        self.parent = parent

def setup_table(table, num_rows, num_columns, init_row, init_column):
    for i in range(0, num_rows):
        row = []
        for j in range(0, num_columns):
            row.append(cell(None, -1))
        table.append(row)

    for i in range(0, num_rows):
        table[i][0].cost = init_column(i)
        table[i][0].parent = 2

    for j in range(0, num_columns):
        table[0][j].cost = init_row(j)
        table[0][j].parent = 1

def print_table(table, num_rows, num_columns):
    print("[\n")
    for i in range(0, num_rows):
        print(" [", end="")
        for j in range(0, num_columns):
            if j != num_columns - 1:
                # parent: {table[i][j].parent}
                # parent: {table[i][j].parent}
                print(f"cost: {table[i][j].cost}, ", end="")
            else:
                print(f"cost: {table[i][j].cost}", end="")
        print("]\n")
    print("]\n")


def min_operations_dp(pattern: str, text: str, op, p_op, t_op, table) -> int:
    MATCH = 0
    INSERT = 1
    DELETE = 2
    operations_count = [0] * 3
    
    for i in range(1, len(pattern)):
        for j in range(1, len(text)):
            operations_count[MATCH] = table[i - 1][j - 1].cost + op(pattern[i], text[j])
            operations_count[INSERT] = table[i][j - 1].cost + t_op(text[j])
            operations_count[DELETE] = table[i - 1][j].cost + p_op(pattern[i])
            
            table[i][j].cost = operations_count[MATCH]
            table[i][j].parent = MATCH

            for operation in [INSERT, DELETE]:
                if operations_count[operation] < table[i][j].cost:
                    table[i][j].cost = operations_count[operation]
                    table[i][j].parent = operation

    return table[i][j].cost


        
def setup_cache(cache, num_rows, num_columns, init_row, init_column):
    for i in range(0, num_rows):
        temp = []
        for j in range(0, num_columns):
            temp.append(None)
        cache.append(temp)

    for i in range(0, num_rows):
        cache[i][0] = init_column(i)

    for j in range(0, num_columns):
        cache[0][j] = init_row(j)


def increasing_insert_penalty(t_idx):
    return t_idx * insert_penalty(' ')

def zero_insert_penalty(t_idx):
    return 0

def increasing_delete_penalty(p_idx):
    return p_idx * delete_penalty(' ')

def constant_insert_penalty(t_idx):
    return 1

def constant_delete_penalty(p_dx):
    return 1


    
def default_goal_cell_column(table, pattern, text):
    return len(text) - 1

# for the text 'template' the pattern 'ate' is perfectly matched at the end
# we need to make it cost the same (and less than match or delete) to start the match from any point in the text
# when 'ate' is matched the row value will be at the end and the column value will be minimized where matches
# are made for the pattern text instead of skipping over the pattern which will have increasing penalty cost
# I think also substring matches where the least skips over the text and the least substitutions will also have the lowest cost
# for example if 'a_t_e', are, and 'ate' all occurred in the text the latter match will have lower cost  

def substring_goal_cell_column(table, pattern, text):
    i = len(pattern) - 1
    j = 0
    current_offset = j
    next_offset = current_offset + 1 
    current_min_cost = table[i][current_offset].cost

    while next_offset < len(text):
        next_cost = table[i][next_offset].cost
        if next_cost < current_min_cost:
            current_min_cost = next_cost
            j = next_offset
            
        current_offset = next_offset
        next_offset = current_offset + 1
    
    return j

    



def match_type(c1, c2):
    if c1 == c2:
        return "M"
    else:
        return "S"
    
def edit_sequence(pattern, text, start_cell, target_cell, table, i, j, match_op):
    current_cell = target_cell
    if current_cell == start_cell:
        return []
    else:
        if current_cell.parent == 0:
            operation = match_op(pattern[i], text[j])
            prefix = edit_sequence(pattern, text, start_cell, table[i - 1][j - 1], table, i - 1, j - 1, match_op)
            prefix.append(operation)
            return prefix
        elif current_cell.parent == 1:
            operation = "I"
            prefix = edit_sequence(pattern, text, start_cell, table[i][j - 1], table, i, j - 1, match_op)
            prefix.append(operation)
            return prefix
        else:
            operation = "D"
            prefix = edit_sequence(pattern, text, start_cell, table[i - 1][j], table, i - 1, j, match_op)
            prefix.append(operation)
            return prefix
    

    




def test_min_operations_recur():
    p = " ate"
    t = " spatula"
    i = len(p) - 1
    j = len(t) - 1

    result = min_operations_recur(p, t, i, j, match_penalty, delete_penalty, insert_penalty)

    print(f"the min operations for transforming p into t is: {result}\n")

#test_min_operations_recur()

def test_min_operations_cached():
    p = " ate"
    t = " spatula"
    i = len(p) - 1
    j = len(t) - 1
    cache = []
    setup_cache(cache, i + 1, j + 1, increasing_insert_penalty, increasing_delete_penalty)

    result = min_operations_cached(p, t, i, j, match_penalty, delete_penalty, insert_penalty, cache)

    print(f"the min operations for transforming p into t is: {result}\n")
    print(f"the cache is {cache}\n")

#test_min_operations_cached()

def test_min_operations_dp():
    p = " ate"
    t = " spatula"
    i = len(p) - 1
    j = len(t) - 1
    table = []
    setup_table(table, i + 1, j + 1, increasing_insert_penalty, increasing_delete_penalty)

    result = min_operations_dp(p, t, match_penalty, delete_penalty, insert_penalty, table)

    print(f"the min operations for transforming p into t is: {result}\n")
    print_table(table, i + 1, j + 1)
    target_cell_column = default_goal_cell_column(table, p, t)
    target_cell = [len(p) - 1][target_cell_column]
    start_cell = table[0][0]
    sequence = edit_sequence(p, t, start_cell, target_cell, table, i, target_cell_column, match_type)
    print(f"the edit sequence is {sequence}\n")

#test_min_operations_dp()


def test_min_substring_operations_dp():
    p = " ate"
    t = " altitude are ate"
    #t = " speculate"
    i = len(p) - 1
    j = len(t) - 1
    table = []
    setup_table(table, i + 1, j + 1, zero_insert_penalty, increasing_delete_penalty)

    result = min_operations_dp(p, t, match_penalty, delete_penalty, insert_penalty, table)

    print(f"the min operations for transforming p into t is: {result}\n")
    print_table(table, i + 1, j + 1)
    target_cell_column = substring_goal_cell_column(table, p, t)
    target_cell = table[len(p) - 1][target_cell_column]
    start_cell = table[0][0]
    sequence = edit_sequence(p, t, start_cell, target_cell, table, i, target_cell_column, match_type)
    print(f"the edit sequence is {sequence}\n")

#test_min_substring_operations_dp()

def test_min_subsequence_operations_dp():
    ns = [1,2,9,8,5,6,7]
    t = " " + "".join([str(n) for n in ns])

    ns.sort()
    p = " " + "".join([str(n) for n in ns])
    
    i = len(p) - 1
    j = len(t) - 1
    table = []
    setup_table(table, i + 1, j + 1, increasing_insert_penalty, increasing_delete_penalty)

    result = min_operations_dp(p, t, monotone_match_penalty, delete_penalty, insert_penalty, table)



    print(f"the min operations for transforming p into t is: {result}\n")
    print_table(table, i + 1, j + 1)
    target_cell_column = default_goal_cell_column(table, p, t)
    target_cell = table[len(p) - 1][target_cell_column]
    start_cell = table[0][0]
    sequence = edit_sequence(p, t, start_cell, target_cell, table, i, target_cell_column, match_type)

    print(f"t is {t}\n")
    print(f"p is {p}\n")


    print(f"the edit sequence is {sequence}\n")

test_min_subsequence_operations_dp()
