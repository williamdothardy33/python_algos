#time complexity O(N) where N is length of xs, and ys
def intersection(xs, ys):
    index = {}
    result = []
    # build an index for xs 
    for x in xs:
        index[x] = True
    
    # populate result with entries in ys that have been indexed
    for y in ys:
        if index.get(y) is not None:
            result.append(y)

    return result

def test_intersection():
    xs = [3,4,5,6,7]
    ys = [10,9,8,7,6,5]
    print(intersection(xs, ys))

def char_duplicate(xs):
    tracked = {}
    for x in xs:
        if tracked.get(x) is None:
            tracked[x] = True
        else:
            return x

def test_char_duplicate():
    xs = ['a', 'b', 'c', 'd', 'c', 'e']
    print(char_duplicate(xs))

def missing_letter(ls):
    index = {}
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']
    
    #build an index for ls
    for l in ls:
        index[l] = True

    # check alphabet against index
    for letter in alphabet:
        if index.get(letter) is None:
            return letter

def test_missing_letter():
    ls = 'the quick brown box umps over a lazy dog'
    print(missing_letter(ls))

def first_non_duplicate(ls):
    index = {}
    for l in ls:
        if index.get(l) is None:
            index[l] = True
        else:
            index[l] = False
    
    for l in ls:
        if index.get(l) is True:
            return l

def test_first_non_duplicate():
    ls = 'minimum'
    print(first_non_duplicate(ls))

test_first_non_duplicate()
    
