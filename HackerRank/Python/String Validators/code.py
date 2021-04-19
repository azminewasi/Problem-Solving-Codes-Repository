if __name__ == '__main__':
    s = input()
    number="0123456789"
    small="qwertyuioplkjhgfdsazcvbnm"
    cap="QWERTYUIOPLKJHGFDSAZXCVBNM"
    
    sr="False"
    for i in s:
        if i in number+small+cap:
            sr="True"
            break;
    print(sr)
    sr="False"

    for i in s:
        if i in small+cap:
            sr="True"
            break;
    print(sr)
    sr="False"

    for i in s:
        if i in number:
            sr="True"
            break;
    print(sr)
    sr="False"

    for i in s:
        if i in small:
            sr="True"
            break;
    print(sr)
    sr="False"

    for i in s:
        if i in cap:
            sr="True"
            break;
    print(sr)
    