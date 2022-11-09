def reverse_lookup(d, v):
    k = []
    if v in d.values():
        for k1 in d:
            if d.get(k1) == v:
                k.append(k1)
    return k

if __name__ == '__main__':
    ben = {'name':'James', 'age':26, 'best friend':'James', 'shoe size':26, 24:'James', 23:26}
    print(reverse_lookup(ben, 'James'))