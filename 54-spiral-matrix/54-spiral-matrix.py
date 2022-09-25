class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spire = []
        while matrix:
            top = matrix.pop(0)
            spire += top
            
            if not matrix or not matrix[0]:
                break
                
            for i in range(len(matrix)):
                right = matrix[i].pop()
                spire += [right]
                
            if not matrix or not matrix[0]:
                break
            
            bottom = matrix.pop()
            spire += bottom[::-1]
            
            if not matrix or not matrix[0]:
                break
            
            for i in range(len(matrix)-1, -1, -1):
                left = matrix[i].pop(0)
                spire += [left]
                
        return spire