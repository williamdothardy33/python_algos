from collections import deque
class backtrack():
    discovered = []
    def setup_word_search(self, n, m):
        for i in range(n):
            row = [False] * m
            self.discovered.append(row)

    def next_candidates(self, table, row, column):
        candidates = []
        row_end = len(table)
        column_end = len(table[0])

        for i in range(-1, 2, 2):
            next_row = row + i
            next_column = column + i

            if next_row > - 1 and next_row < row_end and self.discovered[next_row][column] != True:
                candidates.append([next_row, column])
            if next_column > - 1 and next_column < column_end and self.discovered[row][next_column] != True:
                candidates.append([row, next_column])

        return candidates
        
    def word_search_recur(self, table, word, word_offset, row, column):
        if word_offset == len(word):
            return True
        
        found = False
        for next_row, next_column in self.next_candidates(table, row, column):
            self.discovered[next_row][next_column] = True
            if table[next_row][next_column] == word[word_offset]:
                found = found or self.word_search_recur(table, word, word_offset + 1, next_row, next_column)
                if found:
                    break
        return found
    
    def word_search(self, table, word):
        n = len(table)
        m = len(table[0])
        is_found = False
        if n != 0 and m != 0 and len(word) != 0:
            self.setup_word_search(n, m)
            for i in range(n):
                if is_found:
                    break
                for j in range(m):
                    if table[i][j] == word[0]:
                        is_found = is_found or self.word_search_recur(table, word, 1, i, j)
                        if is_found:
                            break
        return is_found
    
def test_word_search():
    table = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    #word = "ABFCEE"
    word = "SEE"
    result = backtrack().word_search(table, word)
    print(f"the word {word} was found in the table: {result}\n")

test_word_search()
                
            

