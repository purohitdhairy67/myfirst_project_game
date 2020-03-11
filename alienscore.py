
def scoring(score_value):
    filename = "scoring.txt"
    with open(filename) as fh:
        score = fh.read()
        score = eval(score)
        fh.close()
    score.append(["username",  score_value])
    filename = "scoring.txt"
    with open(filename, 'w') as file:
        file.write(str(score))
        file.close()


def update_username(username):
    filename = "scoring.txt"
    with open(filename) as fh:
        score = fh.read()
        score = eval(score)
        fh.close()
    score[-1][0] = username
    with open(filename, 'w') as file:
        file.write(str(score))
        file.close()
    temp = score[-1]
    poping = False
    for i in range(len(score) - 1):
        if score[i][0] == temp[0] and score[i][1] < temp[1]:  # compare username and remove if same
            score[i][1] = temp[1]
        if score[i][0] == temp[0]:
            poping = True
    if len(score) > 1 and poping:
        score.pop()
    with open(filename, 'w') as file:
        file.write(str(score))
        file.close()

