import time
from sensors.simple_button import SimpleButton

# Usage: python3 -m sensors.simple_button.examples.read


def main():
    led = SimpleButton(10)
    while True:
        time.sleep(1)
        print("Button is{} pressed".format(
            '' if led.read_pressed() else ' not'))

if __name__ == "__main__":
    main()
