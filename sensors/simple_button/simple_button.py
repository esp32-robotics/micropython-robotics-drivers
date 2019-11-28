
class SimpleButton(object):
    """Represents a single button that is connected to the ESP32"""

    def __init__(self, pin):
        self.pin = pin

    def read_pressed(self):
        print("Reading button on pin {}".format(self.pin))
        # TODO: Actually call MicroPython code to get the value

        return False
