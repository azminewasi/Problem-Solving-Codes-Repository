def replacer(a,b):
    ans=""
    v="aeiou"
    c="qwrtypsdfghjklzxcvbnm"
    for letter in a:
        if b=="vowels":
            if letter.lower() in v:
                ans=ans+"V"
            else:
                ans=ans+letter
        elif b=="consonants":
            if letter.lower() in c:
                ans=ans+"C"
            else:
                ans=ans+letter
        
    return ans


print(replacer("It is MAT110 final", "vowels"))
print(replacer("It is CSE110 final", "consonants"))