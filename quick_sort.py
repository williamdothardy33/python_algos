import random
def partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer = 0):
    if left_pointer == pivot_index and left_pointer < last_idx:
        return partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer + 1)
    elif right_pointer == pivot_index and right_pointer > 0:
        return partition_recur(ns, last_idx, pivot_index, right_pointer - 1, left_pointer)
    elif ns[left_pointer] < ns[pivot_index] and left_pointer < right_pointer:
        return partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer + 1)
    elif ns[right_pointer] >= ns[pivot_index] and right_pointer > left_pointer:
        return partition_recur(ns, last_idx, pivot_index, right_pointer - 1, left_pointer)
    elif left_pointer >= right_pointer:
        if right_pointer > pivot_index:
            print('final swap')
            print(f'swapped (i, n): ({right_pointer}, {ns[right_pointer]}) with: ({pivot_index}, {ns[pivot_index]})')
            swap(ns, right_pointer, pivot_index)
            print()
            print(f'result: {ns}')
            print()
            return ns
        else:
            print('final swap')
            print(f'swapped (i, n): ({left_pointer}, {ns[left_pointer]}) with: ({pivot_index}, {ns[pivot_index]})')
            swap(ns, left_pointer, pivot_index)
            print()
            print(f'result: {ns}')
            print()
            return ns
    else:
        print()
        print(f'swapped (i, n): ({left_pointer},{ns[left_pointer]}) with: ({right_pointer}, {ns[left_pointer]})')
        swap(ns, left_pointer, right_pointer)
        
        print(f'result: {ns}')
        print()
        return partition_recur(ns, last_idx, pivot_index, last_idx, 0)


def swap(ns, pivot_1, pivot_2):
    temp = ns[pivot_1]
    ns[pivot_1] = ns[pivot_2]
    ns[pivot_2] = temp

def test_partition_recur():
    ns = [1,3,19,81,25,33,4,5,7]
    pivot_index = random.choice(range(0, len(ns)))
    last_idx = len(ns) - 1

    print(f'ns: {ns}')
    print(f'(pivot index, pivot value): ({pivot_index}, {ns[pivot_index]})')

    print()
    partition_recur(ns, last_idx, pivot_index, last_idx)
    
    print(f'partitioned ns: {ns}')

test_partition_recur()
    

    


