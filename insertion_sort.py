def insertion_sort_recur(vs, start, prev_pointer, vs_length, current_value):
    if start >= vs_length:
        return None
    if vs[prev_pointer] <= current_value and prev_pointer >= 0:
        insert(vs, current_value, prev_pointer + 1)
        if start + 1 == vs_length:
            return None
        else:
            insertion_sort_recur(vs, start + 1, start, vs_length, vs[start + 1])
    else:
        if prev_pointer == 0:
            shift_right(vs, prev_pointer)
            insert(vs, current_value, prev_pointer)
            if start + 1 == vs_length:
                return None
            else:
                insertion_sort_recur(vs, start + 1, start, vs_length, vs[start + 1])
        else:
            shift_right(vs, prev_pointer)
            insertion_sort_recur(vs, start, prev_pointer - 1, vs_length, current_value)

def insertion_sort_iter(vs):
    start = 1
    prev_pointer = 0
    current_value = vs[1]
    vs_length = len(vs)
    while start < vs_length:
        if vs[prev_pointer] <= current_value:
            insert(vs, current_value, prev_pointer + 1)
            prev_pointer = start
            start += 1
            if start < vs_length:
                current_value = vs[start]
        else:
            if prev_pointer == 0:
                shift_right(vs, prev_pointer)
                insert(vs, current_value, prev_pointer)
                prev_pointer = start
                start += 1
                if start < vs_length:
                    current_value = vs[start]
            else:
                shift_right(vs, prev_pointer)
                prev_pointer -= 1

        



def shift_right(vs, current_pointer):
    vs[current_pointer + 1] = vs[current_pointer]

def insert(vs, value, pointer):
    vs[pointer] = value


t = [10,9,31,22,3,25,3,2,11]
insertion_sort_iter(t)
print(t)
    

    