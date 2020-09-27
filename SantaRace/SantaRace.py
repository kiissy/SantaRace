
from bangtal import *

scene = Scene('산타레이스', 'images/background.png')

santa = Object('images/santa.png')
santa.x = 0
santa.y = 500
santa.locate(scene, santa.x, santa.y)
santa.show()

playButton = Object('images/play.png')
playButton.locate(scene, 610, 30)
playButton.show()

timer = Timer(10.)
showTimer(timer)

def playButton_onMouse(x, y, action):
    santa.x = santa.x + 30
    santa.locate(scene, santa.x, santa.y)

    if santa.x > 1280:
        showMessage('선물 배달 성공!')
playButton.onMouseAction = playButton_onMouse

def timer_onTimeout():
    showMessage('선물 배달 실패!')
timer.onTimeout = timer_onTimeout

timer.start()

startGame(scene)