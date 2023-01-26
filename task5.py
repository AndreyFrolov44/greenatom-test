def version_comparison(a: str, b: str):
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))

    if len(a) != len(b):
        return -1 if len(a) < len(b) else 1

    i = 0
    while i < len(a) and len(b):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
        else:
            i += 1
    else:
        return 0


print(version_comparison('2.100.2', '2.100.2.5.3'))
