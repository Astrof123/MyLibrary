def circleShift(word, orig):
    total = 0
    temple = orig
    sp = []
    for i in range(len(orig)):
        if temple not in sp:
            for j in range(len(word) - len(orig) + 1):
                if word[j:j+len(orig)] == temple:
                    total += 1
            sp.append(temple)
            temple = temple[-1] + temple[:-1]
        else:
            temple = temple[-1] + temple[:-1]

    return total