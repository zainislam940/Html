def game():
    return 446
    score = game()
    with open("Hi score.txt,") as f:
        Hiscore = int(f.read())

if hiscore<score:
    with open("Hi score.txt," "w")  as f:
        f.write(str(score))