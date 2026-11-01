class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Store existing digits
        for i in range(9):
            for j in range(9):

                num = board[i][j]

                if num == ".":
                    empty.append((i, j))
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(pos):

            if pos == len(empty):
                return True

            # Find cell with minimum candidates
            best = pos
            min_count = 10

            for p in range(pos, len(empty)):

                r, c = empty[p]
                b = (r // 3) * 3 + c // 3

                candidates = []

                for num in "123456789":
                    if (num not in rows[r] and
                        num not in cols[c] and
                        num not in boxes[b]):
                        candidates.append(num)

                if len(candidates) < min_count:
                    min_count = len(candidates)
                    best = p

                if min_count == 0:
                    break

            if min_count == 0:
                return False

            # Swap best cell into current position
            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            b = (r // 3) * 3 + c // 3

            for num in "123456789":

                if (num not in rows[r] and
                    num not in cols[c] and
                    num not in boxes[b]):

                    board[r][c] = num

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(pos + 1):
                        return True

                    # Undo
                    board[r][c] = "."

                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        backtrack(0)