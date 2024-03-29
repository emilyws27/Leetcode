class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i, output = 0, []
        
        # Append first non-overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals (if no overlapping then just append newInterval)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        output.append(newInterval)
        
        # Append remaining non-overlapping intervals
        while i < n:
            output.append(intervals[i])
            i += 1
            
        return output