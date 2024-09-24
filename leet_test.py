class Solution:
    def gcd(self, n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        if n1 % n2 == 0:
            return n2
        else:
            return self.gcd(n2, n1 % n2)

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotation_angle = k % len(nums)
        num_cycles = 0
        max_cycles = self.gcd(len(nums), rotation_angle)
        num_rotations = 0
        max_rotations = len(nums) / max_cycles if max_cycles != 0 else 0
        rotation_origin = 0
        current_angle = rotation_origin
        current_position = nums[current_angle]
        while num_cycles < max_cycles:
            while num_rotations < max_rotations:
                next_angle = (current_angle + rotation_angle) % len(nums)
                next_position = nums[next_angle]
                nums[next_angle] = current_position
                current_angle = next_angle
                current_position = next_position
                num_rotations += 1
            num_cycles += 1
            num_rotations = 0
            rotation_origin += 1
            current_angle = rotation_origin
            current_position = nums[current_angle]

def test_rotate():
    nums = [-1,-100,3,99]
    print(f"before rotating nums is {nums}\n")
    Solution().rotate(nums, 2)
    print(f"after rotating nums is {nums}\n")

#test_rotate()

class Solution_1:
    def maxProfit(self, prices: list[int]) -> int:
        total_profits = 0
        current_buy = prices[0]
        for i in range(len(prices)):
            if i + 1 < len(prices):
                #can I make more money by waiting one more day
                #if not dump stock and make buy the next day
                if prices[i] - current_buy >= prices[i + 1] - current_buy:
                    total_profits += (prices[i] - current_buy)
                    current_buy = prices[i + 1]
                #swap out current_buy if there is a future with more profit to be made
                #and prices are better right now than before
                elif prices[i] < current_buy:
                    current_buy = prices[i]
                #otherwise hold the current stock
                else:
                    continue
            else:
                #if the market is about to close and your still holding a position and its
                #profitable to dump it do so
                if prices[i] > current_buy:
                    total_profits += (prices[i] - current_buy)
                        

        return total_profits

        



class Solution_2:
    def canJump(self, nums: list[int]) -> bool:
        reached_end = False
        end = len(nums) - 1
        position = 0

        while reached_end != True:
            if position >= end:
                reached_end = True
                break
            jump_length = nums[position]
            print(f"position + jump_length is {position + jump_length}\n")
            if jump_length == 0:
                break
            elif position + jump_length < end:
                if nums[position + jump_length] == 0 and jump_length > 1:
                    position = position + (jump_length - 1)
                else:
                    position = position + jump_length
            else:
                reached_end = True
                break
        return reached_end
    
#the greedy assumption is jump the furthest you can at
#any given point in the algorithm and only jump a smaller distance
#if the current jump leaves you in a hole you can't get out of
#this doesn't work because earlier maxed out jumps lock you out
#of the sequence of jumps required in some scenarios where
#the only way to get to the end is to make smaller jumps in the beginning
#you can only backpedal up until your current position in this algo
class Solution_3:
    def canJump(self, nums: list[int]) -> bool:
        reached_end = False
        end = len(nums) - 1
        position = 0
        jump_length = nums[position]

        while reached_end != True:
            next_position = position + jump_length
            if next_position >= end:
                reached_end = True
                break    
            else:
                if nums[next_position] == 0:
                    if jump_length > 1:
                        jump_length -= 1
                    else:
                        reached_end = False
                        break
                else:
                    position = next_position
                    jump_length = nums[next_position]

        return reached_end
            




class Solution_4:
    def canJump(self, nums: list[int]) -> bool:
        reached_end = False
        end = len(nums) - 1
        position = 0
        jump_length = nums[position]

        while reached_end != True:
            next_position = position + jump_length
            if next_position >= end:
                reached_end = True
                break
            else:
                if jump_length != 0:
                    next_choice = position + 1
                    for i in range(position + 1, position + jump_length + 1):
                        if nums[i] >= nums[next_choice]:
                            next_choice = i
                    position = next_choice
                    jump_length = nums[position]
                else:
                    reached_end = False
                    break 

        return reached_end
            



class Solution_5:
    def canJump(self, nums: list[int]) -> bool:
        start = 0
        end = len(nums) - 1
        position = end
        delta_position = 0

        while position >= start:
            if position == start and delta_position == 0:
                return True
            else:
                previous_position = position - 1
                delta_position += 1
                if previous_position > -1:
                    jump_length = nums[previous_position]
                    if jump_length >= delta_position:
                        position = previous_position
                        delta_position = 0
                    else:
                        position = previous_position
                else:
                    return False

def test_canJump():
    nums = [2,3,1,1,4]
    print(f"nums is {nums}\n")
    result = Solution_5().canJump(nums)

    print(f"can jump to end is {result}\n")

#test_canJump()
        

    

        
class Solution_6:
    def canJump(self, nums: list[int]) -> bool:
        reached_end = False
        end = len(nums) - 1
        position = 0
        jump_length = nums[position]
        while reached_end != True:
            next_position = position + jump_length
            if next_position >= end:
                reached_end = True
                break
            else:
                if jump_length != 0:
                    next_choice = position + 1
                    for i in range(position + 1, position + jump_length + 1):
                        if nums[i] >= nums[next_choice]:
                            next_choice = i
                    position = next_choice
                    jump_length = nums[position]
                    can_move = True if (position + jump_length) >= end else False
                    for i in range(position + 1, min(len(nums), position + jump_length + 1)):
                        if nums[i] != 0:
                            can_move = True
                    if can_move == False:
                        position = next_position
                        jump_length = nums[next_position]
                else:
                    reached_end = False
                    break 
        return reached_end





class Solution_7:
    def candy(self, ratings: list[int]) -> int:
        candy_count = 0
        previous_amount = 1
        min_amount = 1

        start_idx = 0
        for i in range(len(ratings)):
            if ratings[i] < ratings[start_idx]:
                start_idx = i

        end_idx = start_idx - 1 if start_idx != 0 else len(ratings) - 1
        
        print(f"the start_idx is {start_idx}\n")
        while start_idx != end_idx:
            print(f"starting another repetition\n\n")
            print(f"the start_idx is {start_idx}\n")
            print(f"the previous count is {previous_amount}\n")
            print(f"the candy_count is {candy_count}\n")
            if start_idx == 0:
                if ratings[start_idx] > ratings[start_idx + 1]:
                    previous_amount += 1
                    candy_count += (previous_amount)
                else:
                    previous_amount = min_amount
                    candy_count += min_amount
                start_idx += 1 
            elif start_idx == len(ratings) - 1:
                if ratings[start_idx] > ratings[start_idx - 1]:
                    previous_amount += 1
                    candy_count += (previous_amount)
                else:
                    previous_amount = min_amount
                    candy_count += min_amount
                start_idx = 0
                previous_amount = 1
            else:
                if ratings[start_idx] <= ratings[start_idx - 1] and ratings[start_idx] <= ratings[start_idx + 1]:
                    previous_amount = min_amount
                    candy_count += min_amount
                else:
                    previous_amount += 1
                    candy_count += (previous_amount)
                    
                start_idx += 1
            
            print(f"after updating current repetition\n\n")
            print(f"the start_idx is {start_idx}\n")
            print(f"the previous count is {previous_amount}\n")
            print(f"the candy_count is {candy_count}\n")

            if start_idx == end_idx:
                print(f"final candy count update start\n")
                print(f"the start_idx is {start_idx}\n")
                print(f"the previous count is {previous_amount}\n")
                print(f"candy count before is {candy_count}\n")
                if end_idx == len(ratings) - 1:
                    if ratings[start_idx] <= ratings[start_idx - 1]:
                        candy_count += min_amount
                    else:
                        candy_count += (previous_amount + 1)
                elif end_idx == 0:
                    if ratings[start_idx] <= ratings[start_idx + 1]:
                        candy_count += min_amount
                    else:
                        candy_count += (previous_amount + 1)
                else:
                    if ratings[start_idx] <= ratings[start_idx + 1] and ratings[start_idx] <= ratings[start_idx - 1]:
                        candy_count += min_amount
                    else:
                        candy_count += (previous_amount + 1)

                print(f"final candy count update end\n")
                print(f"the start_idx is {start_idx}\n")
                print(f"the previous count is {previous_amount}\n")
                print(f"candy count after is {candy_count}\n")
            

                    

                

        return candy_count



def test_candy():
    ratings = [1,2,2]
    print(f"ratings is {ratings}")
    result = Solution_7().candy(ratings)
    print(f"the result is {result}")

#test_candy()

class Solution_8:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_offset = 0
        next_offset = 1
        while next_offset < len(nums):
            if next_offset == current_offset + 1:
                next_offset += 1
            elif nums[current_offset] == nums[next_offset]:
                nums[next_offset] = -1
                next_offset += 1
            else:
                current_offset = next_offset - 1

        start_offset = 0
        search_offset = 1

        print(f"nums before pullback is {nums}\n")


        while start_offset < len(nums):
            if search_offset >= len(nums):
                return start_offset + 1
            elif nums[search_offset] == nums[start_offset] and search_offset == start_offset + 1:
                start_offset += 1
                search_offset += 1
            elif  nums[search_offset] == - 1:
                search_offset += 1
            
            else:
                nums[start_offset + 1] = nums[search_offset]
                nums[search_offset] = -1
                start_offset += 1
                search_offset = start_offset + 1

        return start_offset;

def test_remove_duplicates():
    nums = [0,0,1,1,1,1,2,3,3]
    count = Solution_8().removeDuplicates(nums)
    print(f"the result is {nums}\n")
    print(f"the count is {count}\n")



#test_remove_duplicates()

class MinStack:

    def __init__(self):
        self.underlying = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
            self.underlying.append(val)
        elif val >= self.min:
            self.underlying.append(val)
        else:
            previous_min_rep = val - self.min if val - self.min < val else val + self.min
            self.min = val
            self.underlying.append(previous_min_rep)        

    def pop(self) -> None:
        result = self.underlying[-1]
        if len(self.underlying) == 1:
            self.min = None
        elif result < self.min:
            self.min = self.min - result if self.min > 0 else result - self.min
        self.underlying.pop()

    def top(self) -> int:
        result = self.underlying[-1]
        if result < self.min:
            return self.min
        return result

    def getMin(self) -> int:
        result = self.min
        return result
    
def test_MinStack():
    minStack = MinStack()
    print(f"newly created minStack is {minStack.underlying}\n")
    minStack.push(-2);
    print(f"after push -2 minStack is {minStack.underlying}\n")
    minStack.push(0);
    print(f"after push 0 minStack is {minStack.underlying}\n")
    minStack.push(-3);
    print(f"after push -3 minStack is {minStack.underlying}\n")
    min1 = minStack.getMin();
    print(f"getMin returned {min1}\n")
    minStack.pop();
    print(f"after poping minStack is {minStack.underlying}\n")
    top1 = minStack.top();
    print(f"the top of the stack is now {top1}\n")
    min2 = minStack.getMin();
    print(f"the min is now {min2}\n")

#test_MinStack()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_9:
    def rightSideView(self, root: TreeNode) -> list[int]:
        queue = deque()
        queue.append(root)
        result =  []

        while len(queue) != 0:
            current = queue.popleft()
            if current is not None:
                result.append(current.val)
                left = current.left
                right = current.right
                if right is not None:
                    queue.append(right)
                else:
                    queue.append(left)

        return result

def test_rightSideView():
    root = [1,2,3,4]
    root_tree = TreeNode(val = 1, left = TreeNode(val = 2, left = TreeNode(val = 4)), right = TreeNode(val = 3))
    
    result = Solution_9().rightSideView(root_tree)
    print(f"the result is {result}")

#test_rightSideView()

class Solution_10:
    def rotate_image(self, image: list[list[int]]):
        diameter = len(image)
        rotation_angle = len(image) - 1
        num_rotations = 0
        row_start = 0
        column_start = 0
        top = row_start
        right = column_start + rotation_angle
        bottom = row_start + rotation_angle
        left = column_start
        row = row_start
        column = column_start
        max_shifts = 4
        current = image[row][column]

        
        while diameter > 1:
            print(f"(row, next) is ({row}, {column})\n")

            for i in range(max_shifts):
                next_row = None
                next_column = None

                if row == top:
                    next_row = top + (column + rotation_angle) - right
                    next_column = right
                elif column == right:
                    next_row = bottom
                    next_column = right - ((row + rotation_angle) - bottom)
                elif row == bottom:
                    next_row = bottom - (left -(column - rotation_angle))
                    next_column = left
                else:
                    next_row = top
                    next_column = left + (top -(row - rotation_angle))

                print(f"(next_row, next_column) is ({next_row}, {next_column})\n")

                next = image[next_row][next_column]
                image[next_row][next_column] = current
                current = next
                row = next_row
                column = next_column
            
            if num_rotations == rotation_angle - 1:
                diameter -= 2
                num_rotations = 0
                row_start += 1
                column_start = row_start
                row = row_start
                column = column_start
                current = image[row][column]
                rotation_angle -= 2
                top = row_start
                right = column_start + rotation_angle
                bottom = row_start + rotation_angle
                left = column_start
            else:
                column_start += 1
                row = row_start
                column = column_start
                current = image[row][column]
                num_rotations += 1


def test_rotate_image():
    matrix = [[5,1,9,11], [2,4,8,10], [13,3,6,7], [15,14,12,16]]
    print(f"before rotating matrix is {matrix}\n")
    Solution_10().rotate_image(matrix)
    print(f"after rotating matrix is {matrix}\n")

#test_rotate_image()





class Solution_11:
    def max_water(self, heights: list[int]) -> int:
        left_offset = 0
        right_offset = 0
        volume = 0  
        while right_offset < len(heights):
            next_volume = 0
            marginally_increased_volume = volume
            if right_offset + 1 < len(heights):
                left_height = heights[left_offset]
                right_height = heights[right_offset]
                next_height = heights[right_offset + 1]
                next_volume = next_height if next_height < right_height else right_height
                marginally_increased_volume = ((right_offset + 1) - left_offset) * left_height if left_height < next_height else ((right_offset + 1) - left_offset) * next_height

            if next_volume > marginally_increased_volume:
                left_offset = right_offset
                right_offset += 1
                volume = next_volume
            else:
                volume = marginally_increased_volume
                right_offset += 1

        return volume
            
        

def test_max_water():
    #heights = [1,1]
    #heights = [1,8,6,2,5,4,8,3,7]
    #heights = [1,1]
    heights = [1,1,1,6,5,1]


    print(f"heights is {heights}\n")
    result = Solution_11().max_water(heights)
    print(f"max volume is {result}\n")

#test_max_water()

class Solution_12:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        range_start = None
        current_value = None
        result = []
        current_offset = 0
        while current_offset < len(nums):
            if current_offset == 0:
                current_offset += 1
            else:
                if range_start is None:
                    if nums[current_offset] == nums[current_offset - 1] + 1:
                        range_start = nums[current_offset - 1]
                        current_value = nums[current_offset]
                    else:
                        result.append(str(nums[current_offset - 1]))

                    
                else:
                    if nums[current_offset] == nums[current_offset - 1] + 1:
                        current_value = nums[current_offset]
                    else:
                        result.append(f"{range_start}->{current_value}")
                        range_start = None
                        current_value = None

                if current_offset == len(nums) - 1:
                    if range_start is None:
                        result.append(str(nums[current_offset]))
                    else:
                        result.append(f"{range_start}->{current_value}")
                    break


                current_offset += 1


        return result
    

class Solution_13:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        result = []
        if len(nums) > 0:
            current_offset = len(nums) - 1 
            end = nums[current_offset]
            previous = end
            while current_offset >= 0:
                next_offset = current_offset - 1
                if next_offset >= 0:

                    if nums[next_offset] == nums[current_offset] - 1:
                        current_offset = next_offset
                        previous = nums[current_offset]
                    else:
                        if previous == end:
                            result.append(str(end))
                        else:
                            result.append(f"{previous}->{end}")

                        current_offset = next_offset
                        end = nums[current_offset]
                        previous = end

                if current_offset == 0:
                    if previous == end:
                        result.append(str(nums[current_offset]))
                    else:
                        result.append(f"{previous}->{end}")
                    break

        result.reverse()
        return result






def test_summary_ranges():
    nums = [0,1,2,4,5,7]
    #nums = [0,2,3,4,6,8,9]
    #nums = [-1]

    print(f"nums is {nums}\n")
    result = Solution_13().summary_ranges(nums)
    print(f"ranges are {result}\n")

#test_summary_ranges()

#              1
#          1       1
#      1       2       1
#   1      3       3       1
#1      4       6       4       1

#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1
class Solution_14:
    cache = None
    def setup_binomial_cache(self):
        self.cache = []
        self.cache.append(None)
        for i in range(1, 11):
            temp = []
            for i in range(0, 11):
                temp.append(None)
            self.cache.append(temp) #looks like a longer version of [None, [None, None]] 2x2 with first row None



        for r in range (1, 11):
            self.cache[r][1] = 1
            self.cache[r][r] = 1

    def binomial_coefficient_recur(self, row: int, column: int) -> int:
        if row > 0 and column > 0:
            if column == 1 or column == row:
                return 1
            else:
                return self.binomial_coefficient_recur(row - 1, column - 1) + self.binomial_coefficient_recur(row - 1, column)
            
    def binomial_coefficient_cached(self, row: int, column: int) -> int:
        if self.cache[row][column] is None:
            self.cache[row][column] = self.binomial_coefficient_cached(row - 1, column - 1) + self.binomial_coefficient_cached(row - 1, column)
            
        return self.cache[row][column]
            
    def binomial_coefficient_driver(self, row: int, column: int) -> int:
        self.setup_binomial_cache()
        return self.binomial_coefficient_cached(row, column)
        


    def binomial_coefficients(self, n: int) -> list[int]:
        result = []
        for i in range(1, n + 1):
            result.append(self.binomial_coefficient_recur(n, i))

        return result
    
    def binomial_coefficients_dp(self, n: int) -> list[int]:
        self.setup_binomial_cache()
        for i in range(3, n + 1):
            for j in range(2, i):
                self.cache[i][j] = self.cache[i - 1][j - 1] + self.cache[i - 1][j]


        return self.cache[n]
    
def is_subsequence_recur(s, t, i, j):
    if i == -1:
        return True
    if j == -1 and i > -1:
        return False
    if s[i] == s[j]:
        return is_subsequence_recur(s, t, i - 1, j - 1)
    else:
        return is_subsequence_recur(s, t, i, j - 1)
    
def is_subsequence(s, t):
    i = len(s) - 1
    j = len(t) - 1
    result = False
    while j >= - 1:
        if i == -1:
            result = True
            break
        if s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            j -= 1
    return result
    
def has_subsequence_recur(s, t, i, j):
    if i == 0: #empty s string
        return True
    if j == 0: #empty t string
        return False
    return (s[i] == t[j] and has_subsequence_recur(s, t, i - 1, j - 1)) or has_subsequence_recur(s, t, i, j - 1)

def has_subsequence_dp(s, t, table):
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            table[i][j] = s[i] == t[j] and table[i - 1][j - 1] or table[i][j - 1]

    return table[i][j]

def setup_subsequence_table(table, n, m):
    for i in range(n):
        row = [None] * m
        table.append(row)

    for j in range(m):
        table[0][j] = True

    for i in range(1, n):
        table[i][0] = False

def longest_substring_size(s):
    start = 0
    delta_start = 0
    max_window_size = 0
    in_view = {}
    if len(s) != 0:
        in_view[s[start]] = True
        
        while start + delta_start + 1 < len(s):
            next = s[start + delta_start + 1]
            if in_view.get(next) is not None:
                if delta_start + 1 > max_window_size:
                    max_window_size = delta_start + 1
                start = start + delta_start + 1
                delta_start = 0
                in_view = {}
                in_view[s[start]] = True                
            else:
                in_view[next] = True
                delta_start += 1


    if delta_start + 1 > max_window_size:
                return delta_start + 1
    return max_window_size

def setup_grid_dfs(table, n, m):
    for i in range(n):
        row = [False] * m
        table.append(row)

def adjacent_lands(grid, i, j):
    lands = []
    map_bottom = len(grid)
    map_right = len(grid[0]) if map_bottom != 0 else 0
    for delta in range(-1, 2, 2):
        longitude = i + delta
        latitude = j + delta

        if longitude > -1 and longitude < map_bottom:
            if grid[longitude][j] == "1":
                lands.append([longitude, j])

        if latitude > -1 and latitude < map_right:
            if grid[i][latitude] == "1":
                lands.append([i, latitude])

    return lands

    
#a union find was suggested in the leet problem "topics" but in order to use the union find you need the edges for the graph
# (I think) I can't think of a cheaper way to get these "tree edges" besides using dfs and since I'm already using it to find which
#cells are connected I figure there isn't any point. 
# I could use adjacent_lands on each "land" cell but it would give me back edges (which union find set will ignore assuming
# the tree edges containing the vertices that make up the back edge are checked first)
# and It doesn't seem like it's worth the cost. will think on this further.

def grid_dfs(grid, i, j, discovered):
    discovered[i][j] = True
    nearby_lands = adjacent_lands(grid, i, j)
    for longitude, latitude in nearby_lands:
        if discovered[longitude][latitude] == False:
            grid_dfs(grid, longitude, latitude, discovered)

def number_of_islands(grid, discovered):
    island_count = 0
    map_bottom = len(grid)
    map_right = len(grid[0]) if map_bottom != 0 else 0

    for i in range(map_bottom):
        for j in range(map_right):
            if grid[i][j] != "0":
                if discovered[i][j] == False:
                    island_count += 1
                    grid_dfs(grid, i, j, discovered)

    return island_count

def climbing_stairs_by_search(n, count):
    if n < 0:
        return count
    if n == 0:
        return count + 1
    left_count = climbing_stairs_by_search(n - 1, count)
    right_count = climbing_stairs_by_search(n - 2, left_count)
    return right_count

def climbing_stairs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return climbing_stairs(n - 1) + climbing_stairs(n - 2)

def climbing_stairs_dp(n):
    row = [0] * (n + 1)
    row[0] = 1
    row[1] = 1
    for i in range(2, n + 1):
        row[i] = row[i - 1] + row[i - 2]

    return row[n]

def ransom_note(note, magazine):
    letter_store = {}
    for c in magazine:
        if letter_store.get(c) is not None:
            letter_store[c] += 1
        else:
            letter_store[c] = 1

    for l in note:
        count = letter_store.get(l)
        if count is not None:
            if count != 0:
                letter_store[l] = count - 1
            else:
                return False
        else:
            return False
    return True


def house_robber(nums, i):
    if i == 0:
        return nums[i]
    if i == 1:
        current = nums[i]
        previous = nums[i - 1]
        if current > previous:
            return current
        return previous
    
    rob_and_skip = nums[i] + house_robber(nums, i - 2)
    skip = house_robber(nums, i - 1)
    if rob_and_skip > skip:
        return rob_and_skip
    return skip

def house_robber_dp(nums):
    row = [0] * len(nums)

    if len(nums) > 0:
        row[0] = nums[0]
        if len(nums) > 1:
            row[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                row[i] = max((nums[i] + row[i - 2]), row[i - 1])

    print(f"row is {row}\n")

    return row[len(nums) - 1]

            

def test_house_robber():
    #nums = [1,2,3,1]
    nums = [2,7,9,3,1]
    i = len(nums) - 1
    result = house_robber(nums, i)
    print(f"maximum money made from robbing {nums} is {result}\n")

test_house_robber()

def test_house_robber_dp():
    nums = [1,2,3,1]
    #nums = [2,7,9,3,1]
    i = len(nums) - 1
    result = house_robber_dp(nums)
    print(f"maximum money made from robbing {nums} (using dp) is {result}\n")

test_house_robber_dp()


def test_ransom_note():
    #note = "a"
    #magazine = "b"
    note = "aa"
    #magazine = "ab"
    magazine = "aab"

    result = ransom_note(note, magazine)

    print(f"the ransom note '{note}' can be made with the magazine '{magazine}': {result}\n")

#test_ransom_note()
    

def test_climbing_stairs_by_search():
    #n = 2
    #n = 3
    n = 4
    result = climbing_stairs_by_search(n, 0)
    print(f"the number of ways of climbing {n} steps (using search) is {result}\n")

#test_climbing_stairs_by_search()

def test_climbing_stairs_dp():
    #n = 2
    #n = 3
    n = 4
    result = climbing_stairs_dp(n)
    print(f"the number of ways of climbing {n} steps (using dp) is {result}\n")

#test_climbing_stairs_dp()

def test_climbing_stairs():
    #n = 2
    #n = 3
    n = 4
    result = climbing_stairs(n)
    print(f"the number of ways of climbing {n} steps is {result}\n")

#test_climbing_stairs()

def test_number_of_islands():
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    discovered = []
    length = len(grid)
    width = len(grid[0]) if length != 0 else 0
    setup_grid_dfs(discovered, length, width)
    result = number_of_islands(grid, discovered)
    print(f"the map has {result} island(s)\n")

#test_number_of_islands()








def test_longest_substring_size():
    s = "abcabcbb"
    #s = "bbbbb"
    #s = "pwwkew"
    result = longest_substring_size(s)
    print(f"the string: {s} has longest substring of length: {result}\n")

#test_longest_substring_size()

    

def test_binomial_coefficient_recur():
    row = 5
    column = 3
    result = Solution_14().binomial_coefficient_recur(row, column)
    print(f"the ({row}, {column}) binomial coefficient is {result}\n")

#test_binomial_coefficient_recur()

def test_binomial_coefficients():
    order = 5
    result = Solution_14().binomial_coefficients(order)
    print(f"the binomial coefficients for order {order} polynomial is {result}\n")

#test_binomial_coefficients()

def test_binomial_coefficient_cached():
    row = 5
    column = 3
    result = Solution_14().binomial_coefficient_driver(row, column)
    print(f"the ({row}, {column}) binomial coefficient is {result}\n")
    

#test_binomial_coefficient_cached()

def test_binomial_coefficients_dp():
    n = 5
    result = Solution_14().binomial_coefficients_dp(n)
    print(f"the binomial coefficients for n = {n}  is {result}\n")

#test_binomial_coefficients_dp()

def test_has_subsequence_recur():
    s = " adc"
    t = " ahbgdc"
    result = has_subsequence_recur(s, t, len(s) - 1, len(t) - 1)
    print(f"{s} is a subsequence of {t}: {result}")

#test_has_subsequence_recur()

def test_has_subsequence_dp():
    s = " afc"
    t = " ahbgdc"
    table = []
    setup_subsequence_table(table, len(s), len(t))
    result = has_subsequence_dp(s, t, table)
    print(f"{s} is a subsequence of {t}: {result}")

#test_has_subsequence_dp()
