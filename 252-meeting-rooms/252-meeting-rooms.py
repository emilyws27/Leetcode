class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        inter = []
        for item in intervals:
            inter.append(item[0])
            inter.append(item[1])
        
        inter.sort()
        print(inter)
        
        for i in range(0, len(inter),2):
            print( [inter[i], inter[i+1]])
            if [inter[i], inter[i+1]] not in intervals:
                return False
        return True
        