import utime

__default_callback_group = None


def get_default_callback_group():
    global __default_callback_group
    if not __default_callback_group:
        __default_callback_group = CallbackGroup()
    return __default_callback_group


class CallbackGroup(object):
    """A CallbackGroup manages an event loop"""

    def __init__(self):
        self.timer_queue = []
        print("Global context initialized")

    def add_callback(self, callback_usecs, callback):
        self.timer_queue.append((callback_usecs, callback))
        self.timer_queue.sort()

    def wait_and_step(self):
        if not self.timer_queue:
            return
        usecs, callback = self.timer_queue.pop(0)
        utime.sleep_us(usecs - self.clock_us())
        callback()

    def clock_us(self):
        return utime.ticks_us()
