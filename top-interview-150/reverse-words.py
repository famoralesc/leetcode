class Solution:
    def reverseWords(self, s: str) -> str:
        l = [st for st in s.split(" ") if st != ""]
        l.reverse()
        return " ".join(l)
    
if __name__ == '__main__':
    sol = Solution()
    inp = "the sky is blue"
    assert sol.reverseWords(inp) == "blue is sky the"
    sol = Solution()
    inp = "  hello world  "
    assert sol.reverseWords(inp) == "world hello"
    sol = Solution()
    inp = "a good   example"
    assert sol.reverseWords(inp) == "example good a"