#O(n^3)
def largest_subsection_sum(ns):
    ns_length = len(ns)
    last_idx = ns_length - 1
    sum = None
    window_sum = 0
    start_pointer = 0
    end_pointer = last_idx
    window_pointer = start_pointer
    while start_pointer < ns_length:
        if end_pointer == start_pointer:
            start_pointer += 1
            end_pointer = last_idx
        if window_pointer > end_pointer:
            if sum is not None:
                if window_sum > sum:
                    sum = window_sum
            else:
                sum = window_sum
            end_pointer -= 1
            window_pointer = start_pointer
            window_sum = 0
        else:
            window_sum += ns[window_pointer]
            window_pointer += 1

    return sum

#O(n^2)
def largest_subsection_sum_v2(ns):
    ns_length = len(ns)
    last_idx = ns_length - 1
    sum = None
    window_sum = 0
    total_window_sum = 0
    window_difference = 0
    window_difference_pointer = last_idx
    start_pointer = 0
    window_pointer = start_pointer
    while start_pointer < ns_length:
        if window_difference_pointer == start_pointer:
            if sum is not None:
                if window_sum > sum:
                    sum = window_sum
            else:
                sum = window_sum
            window_sum = 0
            total_window_sum = 0
            window_difference = 0
            window_difference_pointer = last_idx
            start_pointer += 1
            window_pointer = start_pointer
        if window_pointer <= last_idx:
            window_sum += ns[window_pointer]
            total_window_sum = window_sum
            window_pointer += 1
        else:
            window_difference += ns[window_difference_pointer]
            next_window_sum = total_window_sum - window_difference
            if next_window_sum > window_sum:
                window_sum = next_window_sum
            window_difference_pointer -= 1
    return sum

#O(n^2)
def largest_subsection_sum_v3(ns):
    ns_length = len(ns)
    last_idx = ns_length - 1
    max_window_sum = None
    current_window_sum = 0
    start_pointer = 0
    window_pointer = start_pointer
    while start_pointer < ns_length:
        if window_pointer > last_idx:
            start_pointer += 1
            current_window_sum = 0
            window_pointer = start_pointer
        else:
            current_window_sum += ns[window_pointer]
            if max_window_sum is not None:
                if current_window_sum > max_window_sum:
                    max_window_sum = current_window_sum
            else:
                max_window_sum = current_window_sum
            window_pointer += 1
    return max_window_sum
        
#in this implementation which uses the call stack, for a given index i we find the subsection ending at index i - 1 that has the largest sum. starting
#with the first element at the bottom of the call tree at index 0 and making the choice whether to extend the current subsection and possibly update the max
#or starting a new subsection and possibly updating the max. we do this for each successive index so that by the time we get to i - 1 index
# we will have the largest subsection sum ending at that index. for example at index 2 the subsection sum of either n2, sum(n2, n1), or sum(n2,sum(n1, n0)) will
#be returned depending on whether n1 or sum(n1, n0) was returned in the previous frame. and n0 will be returned at the bottom of the call tree. this will calculate
#the largest subsection sum ending at each index i: 0 <= i <= last_idx and pick the biggest one (which is cached in the max dictionary) we only start a new subsection if
#we gain nothing by extending the current subsection (I can't quite say for sure why this criteria makes sense)
def largest_subsection_sum_v4(ns):
    def max_subsection_upto(ns, ns_pointer, max):
        if ns_pointer == 0:
            max['max'] = ns[ns_pointer]
            return ns[ns_pointer]
        else:
            previous_max = max_subsection_upto(ns, ns_pointer - 1, max)
            current = ns[ns_pointer]
            next = current + previous_max
            if next > current:
                if next > max['max']:
                    max['max'] = next
                return next
            else:
                if current > max['max']:
                    max['max'] = current
                return current
    
    last_idx = len(ns) - 1
    max = {'max': None}
    max_subsection_upto(ns, last_idx, max)
    return max['max']

# from my understanding a greedy algorithm solves an overall problem by 'folding' a bunch of best possible choices over the 'partitioned' 
# problem space, and at each point making the best possible choice for a solution within the given partition. So I think in order to implement a greedy algorithm
# we first need to find a suitable partition (to my mind this partition needs to divide the problem in such a way that there is a 'folding' function that can
# un-partition the problem and a map from a given partition to the solution for the given the partition needs to compose with the folding function which is 
#pseudomathmatical but makes sense to me lol so basically fold(map(partition(problem space))) == map(fold(partition(problem space))))

def max_subsection(ns):
    ns_pointer = 0
    max = ns[0]
    subsection_sum = ns[0]
    ns_length = len(ns)
    while ns_pointer < ns_length:
        if ns_pointer + 1 < ns_length:
            next = ns[ns_pointer + 1]
            next_subsection_sum = subsection_sum + next
            if subsection_sum > 0:
                subsection_sum = next_subsection_sum
                
            else:
                subsection_sum = next
            if subsection_sum > max:
                    max = subsection_sum
        ns_pointer += 1
    return max

        

def test_fun():
    ns = [-3,1,-5,1,4,-2,6,-3]
    print(f'ns is: {ns}')
    result = max_subsection(ns)
    print(f'the largest subsection sum of {ns} is: {result}')
test_fun()
