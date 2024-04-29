class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [string for string in s.split(' ') if string != '']
        return len(words[len(words) -1 :][0])

if __name__ == '__main__':
    sol = Solution()
    inp = "Hello World"
    assert sol.lengthOfLastWord(inp) == 5

    inp = "   fly me   to   the moon  "
    assert sol.lengthOfLastWord(inp) == 4

    inp = "luffy is still joyboy"
    assert sol.lengthOfLastWord(inp) == 6