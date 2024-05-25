import random


def swap(ns, pivot_1, pivot_2):
    temp = ns[pivot_1]
    ns[pivot_1] = ns[pivot_2]
    ns[pivot_2] = temp

def partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer = 0):
    if ns[left_pointer] < ns[pivot_index] and left_pointer < last_idx:
        return partition_recur(ns, last_idx, pivot_index, right_pointer, left_pointer + 1)
    elif ns[right_pointer] > ns[pivot_index] and right_pointer > 0:
        return partition_recur(ns, last_idx, pivot_index, right_pointer - 1, left_pointer)
    elif left_pointer >= right_pointer:        
        print()
        print('final swap')
        print(f'swapped (i, n): ({left_pointer}, {ns[left_pointer]}) with: ({pivot_index}, {ns[pivot_index]})')
        swap(ns, left_pointer, pivot_index)
        print(f'result: {ns}')
        print()
        return left_pointer
    else:
        print()
        print(f'swapped (i, n): ({left_pointer},{ns[left_pointer]}) with: ({right_pointer}, {ns[right_pointer]})')
        swap(ns, left_pointer, right_pointer)
        
        print(f'result: {ns}')
        print()
        return partition_recur(ns, last_idx, last_idx, right_pointer - 1, left_pointer + 1)
    




def partition_iter(ns):
    left_pointer = 0
    end_idx = len(ns) - 1
    right_pointer = end_idx - 1
    pivot_index = end_idx
    while left_pointer <= end_idx and right_pointer >= 0:
        if ns[left_pointer] < ns[pivot_index] and left_pointer < end_idx:
            left_pointer += 1
        elif ns[right_pointer] > ns[pivot_index] and right_pointer > 0:
            right_pointer -= 1
        elif left_pointer >= right_pointer:
            print()
            print('final swap')
            print(f'left pointer is: {left_pointer}, and right pointer is {right_pointer}')
            print(f'swapped (i, n): ({left_pointer}, {ns[left_pointer]}) with: ({pivot_index}, {ns[pivot_index]})')
            print(f'ns before: {ns}')
            swap(ns, left_pointer, pivot_index)
            print(f'result: {ns}')
            print()
            return left_pointer
        else:
            print()
            print(f'left point is: {left_pointer}, and right pointer is {right_pointer}')
            print(f'swapped (i, n): ({left_pointer},{ns[left_pointer]}) with: ({right_pointer}, {ns[right_pointer]})')
            print(f'ns before: {ns}')
            swap(ns, left_pointer, right_pointer)
            print(f'result: {ns}')
            print()
            left_pointer += 1
            right_pointer -= 1



    
        

def test_partition_recur():
    ns = [81,1,23,72,4,5,23]
    #pivot_index = random.choice(range(0, len(ns)))
    last_idx = len(ns) - 1

    print(f'ns: {ns}')
    print(f'(pivot index, pivot value): ({last_idx}, {ns[last_idx]})')

    print()
    partition_recur(ns, last_idx, last_idx, last_idx - 1)
    
    print(f'partitioned ns: {ns}')

#test_partition_recur()

def test_partition_iter():
    #ns = [9,21, 33, 1,3,7,45,81]
    ns = [81,1,23,72,4,5,23]
    #pivot_index = random.choice(range(0, len(ns)))
    last_idx = len(ns) - 1

    print(f'ns: {ns}')
    print(f'(pivot index, pivot value): ({last_idx}, {ns[last_idx]})')
    print()
    partition_iter(ns)
    print(f'partitioned ns: {ns}')

test_partition_iter()


