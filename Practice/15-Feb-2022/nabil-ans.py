def checkEvenPalindrome(s, i):
    for j in range(i, len(s)):
        if s[j] != s[2 * i - j - 1]:
            return False
    return True


def checkOddPalindrome(s, i):
    for j in range(i + 1, len(s)):
        if s[j] != s[2 * i - j]:
            return False
    return True


def shortestPalindrome(s):
    l = len(s)
    i = l // 2
    if l % 2 == 1:
        if checkOddPalindrome(s, i):
            return (0, s)
        i = i + 1
    for i in range(i, l):
        if checkEvenPalindrome(s, i):
            s = s[:i]
            return (2 * i - l, s + s[::-1])
        if checkOddPalindrome(s, i):
            s = s[: i + 1]
            return (2 * i - l + 1, s + s[-2::-1])


print(shortestPalindrome(input()))