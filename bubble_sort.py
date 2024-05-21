def bubble_sort_recur(vs, swap_size, pointer_1, pointer_2, swap_count):
    if swap_size < 2:
        return None
    elif pointer_2 == swap_size:
        if swap_count == 0:
            return None
        else:
            bubble_sort_recur(vs, swap_size -1, 0, 1, 0)
    else:
        swapped = swap_or_leave(vs, pointer_1, pointer_2)
        bubble_sort_recur(vs, swap_size, pointer_1 + 1, pointer_2 + 1, swap_count + swapped)

def bubble_sort_iter(vs):
    swap_size = len(vs)
    pointer_1 = 0
    pointer_2 = 1
    swap_count = 0
    while swap_size > 1:
        if pointer_2 == swap_size:
            if swap_count == 0:
                break
            else:
                pointer_1 = 0
                pointer_2 = 1
                swap_count = 0
                swap_size -= 1
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