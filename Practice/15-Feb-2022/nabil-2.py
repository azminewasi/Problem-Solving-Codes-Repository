# def is_palindrome(s):
#     return s == s[::-1]
# from https://stackoverflow.com/a/39829879
def is_palindrome(word):
    if len(word) <= 1: return True
    if word[0] != word[-1]: return False
    return is_palindrome(word[1:-1])

def shortest_palindrome(s):
    if is_palindrome(s): return (0, s)
    for i in range(1, len(s)):
        if is_palindrome(s[i:]):
            return (i, s + s[i - 1 :: -1])

def shortest_palindrome_pro_max(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            n, m = shortest_palindrome(s[i:-i] if i > 0 else s)
            s = s[:i]
            return (n, s + m + s[::-1])
    return (0, s)

while True:
    print(shortest_palindrome_pro_max(input()))