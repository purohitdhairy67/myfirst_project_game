def finalScoring():
    filename = "scoring.txt"

    with open(filename) as fh:
        score = fh.read()
        score = eval(score)
        fh.close()

    # insertion sort
    for i in range(1, len(score)):
        key = score[i]
        j = i-1
        while j >= 0 and score[j][1] < key[1]:
            score[j+1] = score[j]
            j = j-1
        score[j+1] = key

    with open(filename, 'w') as file:
        file.write(str(score))
        file.close()
    n = 1
    for i in score:
        print(str(n) + ". " +i[0], end="" )
        for j in range(8-len(i[0])+10): print(" ",end="")
        print(str(i[1]))
        n += 1
    print("\n\n\n")