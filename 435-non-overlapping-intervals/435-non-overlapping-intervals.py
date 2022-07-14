class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start
        intervals.sort(key=lambda i:i[0])
        prev_interval_end = intervals[0][1]
        
        removals = 0
        
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            curr_interval_start = curr_interval[0]
            curr_interval_end = curr_interval[1]
            
            # check for overlap and increment count
            # set end to min of prev/current. We want to get rid of longer/larger end interval
            if curr_interval_start < prev_interval_end:
                removals += 1
                prev_interval_end = min(curr_interval_end, prev_interval_end)
            else:
                prev_interval_end = curr_interval_end
            
        return removals