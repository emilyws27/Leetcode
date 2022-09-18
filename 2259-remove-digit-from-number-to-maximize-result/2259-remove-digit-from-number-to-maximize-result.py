class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        new_num = []
        for dig in range(len(number)):
            if number[dig] == digit:
                
                new_num.append(int(number[:dig]+number[dig+1:]))
        return str(max(new_num))