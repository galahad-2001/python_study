# -*- coding: utf-8 -*-


def gm(rawlist):
    s = []
    lens = len(rawlist)
    for i in range(lens - 1):
        s.append(float(rawlist[i + 1] / float(rawlist[i])))
    s.reverse()

    outputlist = []
    for i in range(lens * 2 - 1):
        outputlist.append([])
        for j in range(lens * 2 - 1):
            v = rawlist[lens - 1]
            for m in range(abs(lens - 1 - i)):
                v /= s[m]
            for n in range(abs(lens - 1 - j)):
                v /= s[n]
            outputlist[i].append(v)

    for i in range(len(outputlist)):
        for k in range(len(outputlist[i])):
            print outputlist[k][i],
        print ''

    return outputlist


def aa(gmlist):
    s = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    lens = len(gmlist)
    


def bb(gmlist):
    pass


if __name__ == '__main__':
    rawlist = [0.006, 0.061, 0.242, 0.383]
    gm(rawlist)
