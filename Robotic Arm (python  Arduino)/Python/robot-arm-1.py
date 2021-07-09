from pyfirmata import Arduino, SERVO
from time import sleep
from threading import Thread

port = 'COM7'
pin1 = 11  # hand/Gripper         --red
pin2 = 10  # rotation/base        --black
pin3 = 9   # up down/sholder      --orange
pin4 = 8   # middle/waist         --yellow

board = Arduino(port)

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO


# ROTATION
def rotation(pin2, angle):
    board.digital[pin2].write(angle)
    sleep(0.015)


def re_rotation():
    for i in range(0):
        rotation(pin2, i)


def x1rotation():
    for i in range(0, 160):
        rotation(pin2, i)


def x2rotation():
    for i in range(160, 1, -1):
        rotation(pin2, i)


# HAND
def hand(pin1, angle):
    board.digital[pin1].write(angle)
    sleep(0.015)


def re_hand():
    for i in range(0):
        hand(pin1, i)


def x1hand():
    for i in range(0, 90):
        hand(pin1, i)


def x2hand():
    for i in range(90, 1, -1):
        hand(pin1, i)


# UP-DOWN
def updown(pin3, angle):
    board.digital[pin3].write(angle)
    sleep(0.015)


def reupdown():
    for i in range(0, 90):
        updown(pin3, i)
    for i in range(90, 1, -1):
        updown(pin3, i)


def x1updown():
    for i in range(0, 180):
        updown(pin3, i)


def x2updown():
    for i in range(180, 1, -1):
        updown(pin3, i)


def x3updown():
    for i in range(90, 1, -1):
        updown(pin3, i)


# MIDDLE
def middle(pin4, angle):
    board.digital[pin4].write(angle)
    sleep(0.015)


def remiddle():
    for i in range(60):
        middle(pin4, i)


def x1middle():
    for i in range(100):
        middle(pin4, i)


def x2middle():
    for i in range(100, 50, -1):
        middle(pin4, i)


def x3middle():
    for i in range(30, 1, -1):
        middle(pin4, i)


def x4middle():
    for i in range(60, 180):
        middle(pin4, i)


def x5middle():
    for i in range(180, 60, -1):
        middle(pin4, i)


# DEFAULT
if __name__ == '__main__':
    Thread(target=remiddle()).start()
    Thread(target=reupdown()).start()
    Thread(target=re_rotation()).start()
    Thread(target=re_hand()).start()
sleep(2)

# STAGE1
x1rotation()
if __name__ == '__main__':
    Thread(target=x3middle()).start()
    Thread(target=x1updown()).start()
    Thread(target=x1hand()).start()

x1middle()
x2hand()
if __name__ == '__main__':
    Thread(target=x2middle()).start()
    Thread(target=x2updown()).start()
    Thread(target=remiddle()).start()
    Thread(target=x2rotation()).start()
    Thread(target=x1updown()).start()
    Thread(target=x4middle()).start()

x1hand()
if __name__ == '__main__':
    Thread(target=x2hand()).start()
    Thread(target=x5middle()).start()
    Thread(target=x2updown()).start()

# DEFAULT2

if __name__ == '__main__':
    Thread(target=remiddle()).start()
    Thread(target=reupdown()).start()
    Thread(target=re_rotation()).start()
    Thread(target=re_hand()).start()

print("done")
