# Notes because it was only a few days and I almost forgot how it works
# the idea behind insertion sort is that you select a value starting at the second value in the array
# you shift all the previous values forward if they are bigger than the current selected value
# the first previous value that you find that is smaller than the current selected value will yield an insertion
# you advance forward after this insertion
# there is an edge case at 0 because there aren't any more previous values to check after that
# You need to check that there is more values to select before you do it

# in reference to quick select it takes logN recursive steps to reach the base case and each recursive
# step partition function is partitioning roughly half the number of elements in the previous step
# another way to think of it is that starting at the bottom of the call tree partition will need to double the amount
# of work it did at the previous step and it will need to do this for a total log(N) steps to reach the root of the call tree
# this is the same as 2^(log(N)) = N. 
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
    

    