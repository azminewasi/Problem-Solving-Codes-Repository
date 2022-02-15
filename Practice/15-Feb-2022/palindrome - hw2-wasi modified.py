"""একটা স্ট্রিং ইনপুট দেয়া হবে, ইনপুট স্ট্রিং এর শেষে সর্বনিম্ন কয়টা ক্যারেক্টার যোগ করলে এটা পলিনড্রোম হবে ও পলিনড্রোমটা কি?"""

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
