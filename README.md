# Micropython robotics drivers

This repository will contain a set of drivers intended to interface various common sensors and output devices with the ESP32 running micropython. 

Once microROS support for micropython is up and running, we anticipate migrating these drivers to function as ROS2 nodes.

## Process for developing a new driver

1. Pick a driver to work on. The [issues list](https://github.com/esp32-robotics/micropython-robotics-drivers/issues) contains several suggested components that are both commonly used sensors and tractable to develop a driver for.
2. Obtain and build the hardware needed for development. That will likely involve an ESP32 dev board, an actuator/sensor, and a breadboard with some minimal amount of wiring to connect things together.
3. Install Micropython on your ESP32: see instructions [here](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
4. Build a driver. Each driver lives in a subfolder of either `sensors/` or `actuators/`, and is a module containing a single class. See the examples in `actuators/led/` and `sensors/button/` as a template.
