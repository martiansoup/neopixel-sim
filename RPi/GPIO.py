import simulator

BCM = 0
IN = 0
OUT = 1
PUD_DOWN = 0
RISING = 0

def setmode(mode):
    pass

def setup(pin, direction, pull_up_down=PUD_DOWN):
    if direction == IN:
        print("New button @pin{}".format(pin))

def add_event_detect(pin, on, callback):
    print("Callback @pin{}".format(pin))
    simulator.buttons.append((pin, callback))
