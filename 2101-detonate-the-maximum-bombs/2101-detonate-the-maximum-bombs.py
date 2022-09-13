class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dict1 = defaultdict(list)
    
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                dist = abs(bombs[i][0] - bombs[j][0])**2 + abs(bombs[i][1] - bombs[j][1])**2
                if dist <= bombs[i][2]**2:
                    dict1[i].append(j)

        def dfs(node):
            visited.add(node)

            for child in dict1[node]:
                if child not in visited:
                    dfs(child)

        max_val = 0

        for i in range(len(bombs)):
            visited = set()
            dfs(i)
            max_val = max(max_val, len(visited))

        return max_val