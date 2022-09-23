class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for char in [(-a,'a'), (-b,'b'), (-c,'c')]:
            if char[0]:
                heapq.heappush(heap, char)
        
        result = []
        while heap:
            count, char = heapq.heappop(heap)
			#if previous 2 characters are same as current character, 
			#first get the second most frequent character and then push back curr character
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not heap:
                    break
                tmpCnt, tmpChar = count, char
                count, char = heapq.heappop(heap)
                heapq.heappush(heap, (tmpCnt, tmpChar))

            result.append(char)
            count += 1
            if count:
                heapq.heappush(heap, (count, char))

        return "".join(result)
        
        
        
        
        