def swap_case(s):
    string = []
    for i in s:
        if i.isalpha():
            if i.islower():
                string.append(i.upper())

            else:
                string.append(i.lower())

        else:
            string.append(i)
    return "".join(string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)