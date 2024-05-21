
# Note this implementation will not work for an empty array one way to fix this would be to use an inner function to do the stack iteration and
# have a check for empty array. Don't know how, and if I can have inner function in python
def selection_sort_recur(vs, last_idx, start, min_index, min_value, pointer):
    if start >= last_idx:
        return None
    elif pointer > last_idx:
        if start == min_index:
            selection_sort_recur(vs, last_idx, start + 1, start + 1, vs[start + 1], start + 1)
        else:
            swap_or_leave(vs, start, min_index)
            selection_sort_recur(vs, last_idx, start + 1, start + 1, vs[start + 1], start + 1)
    else:
        current_value = vs[pointer]
        if current_value < min_value:
            selection_sort_recur(vs, last_idx, start, pointer, current_value, pointer + 1)
        else:
            selection_sort_recur(vs, last_idx, start, min_index, min_value, pointer + 1)

def selection_sort_iter(vs):
    start = 0
    pointer = 0
    last_idx = len(vs) - 1
    if len(vs) == 0:
        return None
    else:
        min_idx = 0
        min_value = vs[0]
        while start < last_idx:
            if pointer > last_idx:
                if start == min_idx:
                    start += 1
                    pointer = start
                    min_idx = pointer
                    min_value = vs[pointer]
                else:
                    swap_or_leave(vs, start, min_idx)
                    start += 1
                    pointer = start
                    min_idx = pointer
                    min_value = vs[pointer]
            else:
                current_value = vs[pointer]
                if current_value < min_value:
                    min_idx = pointer
                    min_value = current_value
                    pointer += 1
                else:
                    pointer += 1

        
    




def swap_or_leave(vs, pointer_1, pointer_2):
    swap_count = 0
    v_1 = vs[pointer_1]
    v_2 = vs[pointer_2]
    if v_2 < v_1:
        vs[pointer_1] = v_2
        vs[pointer_2] = v_1
        swap_count += 1
    return swap_count

vs = [32, 8, 11, 1, 3, 5, 25, 9, 11]
selection_sort_recur(vs, len(vs) - 1, 0, 0, vs[0], 0)

print(vs)