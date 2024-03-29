"""Round A 2021 - Kick Start 2021

K-Goodness String (5pts, 7pts)

Practice Submissions
Test 1
RE
Feb 4 2022, 20:48
remove_red_eye
Last updated: Feb 4 2022, 20:31

PROBLEM
ANALYSIS
Problem
Charles defines the goodness score of a string as the number of indices i such that Si≠SN−i+1 where 1≤i≤N/2 (1-indexed). For example, the string CABABC has a goodness score of 2 since S2≠S5 and S3≠S4.

Charles gave Ada a string S of length N, consisting of uppercase letters and asked her to convert it into a string with a goodness score of K. In one operation, Ada can change any character in the string to any uppercase letter. Could you help Ada find the minimum number of operations required to transform the given string into a string with goodness score equal to K?

Input
The first line of the input gives the number of test cases, T. T test cases follow.

The first line of each test case contains two integers N and K. The second line of each test case contains a string S of length N, consisting of uppercase letters.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of operations required to transform the given string S into a string with goodness score equal to K.

Limits
Memory limit: 1 GB.
1≤T≤100.
0≤K≤N/2.
Test Set 1
Time limit: 20 seconds.
1≤N≤100.
Test Set 2
Time limit: 40 seconds.
1≤N≤2×105 for at most 10 test cases.
For the remaining cases, 1≤N≤100."""

from difflib import ndiff

def levenshtein_distance(str_1, str_2):
    distance = 0
    buffer_removed = buffer_added = 0
    for x in ndiff(str_1, str_2):
        code = x[0]
        if code == ' ':
            distance += max(buffer_removed, buffer_added)
            buffer_removed = buffer_added = 0
        elif code == '-':
            buffer_removed += 1
        elif code == '+':
            buffer_added += 1
    distance += max(buffer_removed, buffer_added)
    return distance


T=int(input())
for i in range(T):
    
    l,K=tuple(list(map(int, input().split())))
    data=input()
    
    if l%2==0:
        d1=data[0:int(l/2)]
        d2=data[-1:int((l/2)+1)*(-1):-1]
    else:
        d1=data[0:int((l-1)/2)]
        d2=data[-1:int((l+1)/2)*(-1):-1]
        
    ans=levenshtein_distance(d1,d2)
    if ans>=K:
        print("Case","#"+str(i+1)+":",0)
    else:
        print("Case","#"+str(i+1)+":",K-ans)