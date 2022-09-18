class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 1. Get integer part of the result
        int_part = ""
        num, denom = numerator, denominator
        
        #   a. Add minus sign if needed
        if num * denom < 0: int_part += '-'
        num, denom = abs(num), abs(denom)
        
        #   b. Add integer part
        int_part += str(num // denom)
        if num % denom == 0: return int_part
        
        # 2. Get decimal part of the result
        dec_part = ""
        # d is a dictionary where d[num] records the position of character num in dec_part
        d = dict()
        i = 0
        while True:
            num %= denom
            # Two exit conditions:
            #   1. there is no numerator left for dividing
            if num == 0: return int_part + '.' + dec_part
            #   2. we've met this numerator before (indicating a repeating decimal)
            elif num in d: return "{}.{}({})".format(int_part, dec_part[:d[num]], dec_part[d[num]:])
            d[num] = i
            i += 1
            num *= 10
            dec_part += str(num // denom)