import math as m


def Insert(D, E):
    tempArray = []
    tempArray.append(E)
    for i, k in D.items():
        if D[i] is not None:
            tempArray = Merge(tempArray, D[i])
            D[i] = None
        else:
            break
    newArrayIndex = m.floor(m.log(len(tempArray), 2))
    D[newArrayIndex] = tempArray[:]
    return True


def Merge(L, R):
    tempArray = []
    L.append(m.inf)
    R.append(m.inf)
    i = 0
    j = 0
    for k in range(len(L)+len(R)-2):
        if L[i] <= R[j]:
            tempArray.append(L[i])
            i += 1
        else:
            tempArray.append(R[j])
            j += 1
    return tempArray


def printD(D):
    for k, v in D.items():
        print(v, end=' ')
    print()


def main():
    D = {}
    D[0] = [0]
    for j in range(1, 20):
        Insert(D, j)
        printD(D)


if __name__ == '__main__':
    main()
