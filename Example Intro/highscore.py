def getHighScore():
    global highScore
    with open(highScoreFile, 'r') as file:
        highScore = file.read()


def newHighScore(newScore):
    with open(highScoreFile, 'w') as file:
        file.write(newScore)
