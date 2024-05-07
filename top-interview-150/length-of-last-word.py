def lengthOfLastWord(s: str) -> int:
    """Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal 
    substring
    consisting of non-space characters only.

    Example 1:

    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.
    
    Examples
    -------
    >>> lengthOfLastWord("Hello World")
    5
    >>> lengthOfLastWord("   fly me   to   the moon  ")
    4
    >>> lengthOfLastWord("luffy is still joyboy")
    6
    """
    words = [string for string in s.split(' ') if string != '']
    return len(words[-1])


if __name__ == '__main__':
    inp = "Hello World"
    assert lengthOfLastWord(inp) == 5

    inp = "   fly me   to   the moon  "
    assert lengthOfLastWord(inp) == 4

    inp = "luffy is still joyboy"
    assert lengthOfLastWord(inp) == 6