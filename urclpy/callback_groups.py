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
        self.pending_callbacks = []  # Tuples of (usecs, function)
        self.subscriptions = {}  # Map of channels to list of functions
        print("Global context initialized")

    def _add_callback(self, callback_usecs, callback):
        self.pending_callbacks.append((callback_usecs, callback))
        self.pending_callbacks.sort()

    def _add_subscription(self, topic, func):
        if topic not in self.subscriptions:
            self.subscriptions[topic] = []

        self.subscriptions[topic].append(func)

    def _publish(self, topic, msg):
        if topic not in self.subscriptions:
            return

        for callback in self.subscriptions[topic]:
            self.pending_callbacks.append((0, lambda: callback(msg)))
        self.pending_callbacks.sort()

    def _wait_and_step(self):
        if not self.pending_callbacks:
            return
        usecs, callback = self.pending_callbacks.pop(0)
        utime.sleep_us(usecs - self._clock_us())
        callback()

    def _clock_us(self):
        return utime.ticks_us()
