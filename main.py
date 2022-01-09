def reverseWords(s):
    first = 0

    l = s.split(" ")
    last = len(l) - 1
    new_list = []

    while first <= last:

        li = []
        word = l[first]
        for x in word:
            li.append(x)

        li.reverse()
        s = ''.join(li)
        print(s)
        new_list.append(s)
        first += 1

    final_string = " ".join(new_list)
    print(final_string)
    print(l)

reverseWords("akshay arun more")