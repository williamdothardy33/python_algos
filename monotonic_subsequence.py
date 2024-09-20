#I will try to implement the idea starting with the end of the sequence
# generate a subsequence by either including the entry or not including the entry and do this for every branch
# of the recursive call tree generated by either of those 2 choices
# we will need to elimite the ones that are not monotonic


def longest_monotonic_subsequence_size(sequence, i, j):
    if i == 0: # index of last element in subsequence
        return 1
    if j == -1: # index of current element in subsequence
        return 0
    else:
        current = 0
        if j < i and j >= 0:
            if sequence[j] < sequence[i]:
                current = 1 + longest_monotonic_subsequence_size(sequence, j, j - 1)
            else:
                current = longest_monotonic_subsequence_size(sequence, i, j - 1)
        else:
            current = longest_monotonic_subsequence_size(sequence, i, j - 1)
        previous = longest_monotonic_subsequence_size(sequence, i - 1, j - 1)

        if current > previous:
            return current
        return previous
    

def longest_monotonic_subsequence_size_cached(sequence, i, j, cache):
    if cache[i][j + 1] is None:
        current = 0
        if j < i and j >= 0:
            if sequence[j] < sequence[i]:
                current = 1 + longest_monotonic_subsequence_size_cached(sequence, j, j - 1, cache)
            else:
                current = longest_monotonic_subsequence_size_cached(sequence, i, j - 1, cache)
        else:
            current = longest_monotonic_subsequence_size_cached(sequence, i, j - 1, cache)
        previous = longest_monotonic_subsequence_size_cached(sequence, i - 1, j - 1, cache)
        if current > previous:
            cache[i][j + 1] = current
        else:
            cache[i][j + 1] = previous
        
    return cache[i][j + 1]

def setup_cache(cache, sequence):
    for i in range(len(sequence)):
        row = [None] * (len(sequence) + 1)
        cache.append(row)

    for j in range(len(sequence) + 1):
        cache[0][j] = 1

    for i in range(1, len(sequence)):
        cache[i][0] = 0



def test_longest_monotonic_subsequence_size():
    prefix_default = 0
    sequence = [2,4,3,5,1,7,6,9,8]
    result = longest_monotonic_subsequence_size(sequence, len(sequence) - 1, len(sequence) - 1)
    print(f"the longest subsequence of {sequence} is of length {result}\n")

#test_longest_monotonic_subsequence_size()

def test_longest_monotonic_subsequence_size_cached():
    sequence = [2,4,3,5,1,7,6,9,8]
    cache = []
    setup_cache(cache, sequence)
    result = longest_monotonic_subsequence_size_cached(sequence, len(sequence) - 1, len(sequence) - 1, cache)
    
    print(f"the longest subsequence of {sequence} is of length {result}\n")
    print(f"the cache after running is {cache}\n")

test_longest_monotonic_subsequence_size_cached()
    