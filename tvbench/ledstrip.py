try:
    from rpi_ws281x import *
except ImportError:
    print('Failed to import rpi_ws281x')
    class Color:
        def __init__(self, r, g, b):
            self.r = r
            self.g = g
            self.b = b

    class Adafruit_NeoPixel:
        def __init__(self, *args):
            pass

        def begin(self, *args):
            pass

        def setPixelColor(self, *args):
            pass

        def show(self, *args):
            pass

class Ledstrip:

    _instance = None

    def __init__(self):
        if self._instance is not None:
            raise Exception('Singleton class!')

        self.LED_COUNT = 24
        self.LED_PIN = 18
        self.LED_FREQ_HZ = 800000
        self.LED_DMA = 10
        self.LED_INVERT = False
        self.LED_CHANNEL = 0

        self.color = Color(255, 0, 0)
        self.brightness = 255

        self.strip = Adafruit_NeoPixel(
            self.LED_COUNT,
            self.LED_PIN,
            self.LED_FREQ_HZ,
            self.LED_DMA,
            self.LED_INVERT,
            self.brightness,
            self.LED_CHANNEL
        )
        self.strip.begin()

    def set_color(self, color):
        self.color = color

    def show(self, color):
        for pixel in range(self.LED_COUNT):
            self.strip.setPixelColor(pixel, color)
        self.strip.show()

    def on(self):
        self.show(self.color)

    def off(self):
        self.show(Color(0, 0, 0))

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = self.Ledstrip()
        return cls._instance

