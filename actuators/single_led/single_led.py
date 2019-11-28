
class SingleLed(object):
    """Represents a single LED that is connected to the ESP32"""

    def __init__(self, pin):
        self.pin = pin

    def write_on(self, is_on):
        print("Setting LED on pin {} to {}".format(self.pin, is_on))
        # TODO: Actually call MicroPython code to set the output
