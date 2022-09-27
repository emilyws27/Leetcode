class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        computers = [(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell]
        cols, rows = map(collections.Counter, zip(*computers))
        return sum(rows[y] > 1 or cols[x] > 1 for x, y in computers)