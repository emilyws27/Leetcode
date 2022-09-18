class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")

        lst.reverse()
        to_return = []
        for word in lst:
            if len(word) > 0:
                to_return.append(word)
        
        return " ".join(to_return)