test_case = int(input("Number of Tests: "))

for i in range(test_case):
    print("Test no", i+1, ": ")
    input_string = input("Input string: ")

    temp_string = input_string[::-1]
    ans_polindrome = ""
    ans_minCharAdded = len(input_string)

    for p in range(len(input_string)+1):
        tempCheckPalindrome = input_string+temp_string
        if tempCheckPalindrome == tempCheckPalindrome[::-1]:
            if ans_minCharAdded >= len(temp_string):
                ans_polindrome = tempCheckPalindrome
                ans_minCharAdded = len(temp_string)
        temp_string = temp_string[1:]

    print("Minimum number:", ans_minCharAdded,
          "\nPalindrome:", ans_polindrome, "\n\n")
