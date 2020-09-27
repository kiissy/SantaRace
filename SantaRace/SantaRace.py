
from bangtal import *

scene = Scene('산타레이스', 'images/background.png')

santa = Object('images/santa.png')
santa.x = 0
santa.y = 500
santa.locate(scene, santa.x, santa.y)
santa.show()

playButton = Object('images/play.png')
playButton.locate(scene, 610, 30)
# playButton.show()

startButton = Object('images/start.png')
startButton.locate(scene, 590, 70)
startButton.show()

endButton = Object('images/end.png')
endButton.locate(scene, 590, 20)
endButton.show()

timer = Timer(10.)
showTimer(timer)

def playButton_onMouse(x, y, action):
    santa.x = santa.x + 30
    santa.locate(scene, santa.x, santa.y)

    if santa.x > 1280:
        showMessage('선물 배달 성공!')

        startButton.show()
        endButton.show()
        playButton.hide()

        timer.stop()
playButton.onMouseAction = playButton_onMouse

def endButton_onMouse(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouse

def startButton_onMouse(x, y, action):
    startButton.hide()
    endButton.hide()
    playButton.show()

    timer.set(10.)
    timer.start()

    santa.x = 0
    santa.locate(scene, santa.x, santa.y)
startButton.onMouseAction = startButton_onMouse

def timer_onTimeout():
    showMessage('선물 배달 실패!')

    startButton.show()
    endButton.show()
    playButton.hide()
timer.onTimeout = timer_onTimeout

startGame(scene)