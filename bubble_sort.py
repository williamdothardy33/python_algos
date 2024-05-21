def bubble_sort_recur(vs, end_pointer, pointer_1, pointer_2, swap_count):
    if end_pointer < 2:
        return None
    elif pointer_2 == end_pointer:
        if swap_count == 0:
            return None
        else:
            bubble_sort_recur(vs, end_pointer -1, 0, 1, 0)
    else:
        swapped = swap_or_leave(vs, pointer_1, pointer_2)
        bubble_sort_recur(vs, end_pointer, pointer_1 + 1, pointer_2 + 1, swap_count + swapped)

def bubble_sort_iter(vs):
    end_pointer = len(vs)
    pointer_1 = 0
    pointer_2 = 1
    swap_count = 0
    while end_pointer > 1:
        if pointer_2 == end_pointer:
            if swap_count == 0:
                break
            else:
                pointer_1 = 0
                pointer_2 = 1
                swap_count = 0
                end_pointer -= 1
        else:
            swapped = swap_or_leave(vs, pointer_1, pointer_2)
            pointer_1 += 1
            pointer_2 += 1
            swap_count += swapped

def swap_or_leave(vs, pointer_1, pointer_2):
    swap_count = 0
    v_1 = vs[pointer_1]
    v_2 = vs[pointer_2]
    if v_2 < v_1:
        vs[pointer_1] = v_2
        vs[pointer_2] = v_1
        swap_count += 1
    return swap_count



vs = [10,9,8,7,6,5,4,3, 11, 1]
bubble_sort_iter(vs)

print(vs)