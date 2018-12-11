def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    t = int(n / k)
    p = []
    for i in range(0, n, t):
        p.append(string[i:i + t])
    result = []

    for elm in p:
        for c in elm:
            if c not in result:
                result.append(c)
        output(result)
        result.clear()


def output(result):
    for i in result:
        print(i, end="")
    print()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)