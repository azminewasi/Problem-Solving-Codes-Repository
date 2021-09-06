def function_1 (line):
    if len(line)==1:
        return line
    elif line[len(line)-1] in "aeiou":
        return "yay"+line
    else:
        letters=list(line)
        last_letter=letters[len(line)-1]
        letters[len(line)-1]=""
        ans_list=[]
        ans_list.append(last_letter)
        for letter in letters:
            ans_list.append(letter)
        ans_list.append("a")
        ans_list.append("y")
        ans=""
        for letter in ans_list:
            ans=ans+letter
        return ans

data=input()
print(function_1(data))
