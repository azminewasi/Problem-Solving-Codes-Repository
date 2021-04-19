import re
def count_substring(string, sub_string):
    
    astr, pattern = string, sub_string
    if pattern == '': return 0

    ind, count, start_flag = 0,0,0
    while True:
        try:
            if start_flag == 0:
                ind = astr.index(pattern)
                start_flag = 1
            else:
                ind += 1 + astr[ind+1:].index(pattern)
            count += 1
        except:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)