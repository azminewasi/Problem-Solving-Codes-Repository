def function_2(line):
    letters=list()
    
    positions=list()
    
    for i in range (len(line)):
        letter=line[i]

        if letter==" ":
             continue
        if letter not in letters:
            letters.append(letter)
            positions.append([i])

        else:
            positions[letters.index(letter)].append(i)

    ans = dict(zip(letters, positions))
    return ans


inp=input()
print(function_2(inp))