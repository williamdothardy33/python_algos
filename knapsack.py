def knapsack(s, target, i):
    if target == 0: #target reached
        return True
    if target < 0: #target overshot
        return False
    if i < 0 and target > 0: #exhausted all elements and the sequence and couldn't get target to zero
        return False
    
    # search 2^n subsets. I think the base case functions as a sort of pruning 
    si_included = knapsack(s, target - s[i], i - 1)
    si_excluded = knapsack(s, target, i - 1)
    return si_included or si_excluded

def test_knapsack():
    s = [1, 5, 8, 2]
    result = knapsack(s, 3, len(s) - 1)
    print(f"target 3 can be reached is {result}\n")

    # for j in range(18):
    #     result = knapsack(s, j, len(s) - 1)
    #     print(f"target {j} can be reached is {result}\n")

test_knapsack()    