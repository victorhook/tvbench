from ledstrip import Ledstrip
import time

global led
led = Ledstrip()

i = 0

def slide(color, step=2, delay=.1):
    global led
    i = 0

    while i < 255:
            
        if color == 'r':
            r = i
        elif color == 'g':
            r = i
        elif color == 'b':
            r = i
    
        g = 100
        b = 100
            
        print('Color: %s %s %s' % (r, g, b))
        i += step
        time.sleep(delay)


if __name__ == '__main__':
    slide('r')