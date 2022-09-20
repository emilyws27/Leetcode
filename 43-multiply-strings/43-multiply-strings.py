class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':
            return '0'
        
        digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        int1, int2 = 0, 0
        
        for i, n in enumerate(num1[::-1]):
            int1 += 10 ** i * digits[n]
        
        for i, n in enumerate(num2[::-1]):
            int2 += 10 ** i * digits[n]
            
        return str(int1 * int2)
      
            