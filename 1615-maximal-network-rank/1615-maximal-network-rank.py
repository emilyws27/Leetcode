class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(set)
        #print(d)
        for a, b in roads:
            d[a].add(b)
            d[b].add(a)
        print(d)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, len(d[i]) + len(d[j]) - 1 * (i in d[j]))
        return res