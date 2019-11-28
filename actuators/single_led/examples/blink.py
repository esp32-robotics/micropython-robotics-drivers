import time
from actuators.single_led import SingleLed

# Usage: python3 -m actuators.single_led.examples.blink


def main():
    led = SingleLed(10)
    while True:
        led.write_on(True)
        time.sleep(1)
        led.write_on(False)
        time.sleep(1)

if __name__ == "__main__":
    main()
