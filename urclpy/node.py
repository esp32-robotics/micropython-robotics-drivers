"""
urclpy equivalent of https://github.com/ros2/rclpy/blob/master/rclpy/rclpy/node.py
"""

from .callback_groups import get_default_callback_group


class Publisher(object):
    def __init__(self, callback_group, topic: str):
        self.callback_group = callback_group
        self.topic = topic

    def publish(self, msg):
        self.callback_group._publish(self.topic, msg)


class Node(object):
    def __init__(self, node_name: str):
        self.__name = node_name

        self._default_callback_group = get_default_callback_group()

    def get_name(self):
        return self.__name

    def create_subscription(
        self, msg_type, topic: str, callback, qos_profile: int, *, callback_group=None
    ):
        # NOTE(eric): msg_type and qos_profile aren't handled yet
        callback_group = callback_group or self._default_callback_group

        callback_group._add_subscription(topic, callback)

    def create_publisher(
        self, msg_type, topic: str, qos_profile: int, *, callback_group=None
    ):
        callback_group = callback_group or self._default_callback_group

        return Publisher(callback_group, topic)

    def create_timer(self, timer_period_sec: float, callback, callback_group=None):
        if callback_group is None:
            callback_group = self._default_callback_group

        timer_period_usec = int(timer_period_sec * 1e6)

        def looped_timer(*args, **kwargs):
            callback(*args, **kwargs)
            callback_group._add_callback(
                callback_group._clock_us() + timer_period_usec, looped_timer
            )

        callback_group._add_callback(
            callback_group._clock_us() + timer_period_usec, looped_timer
        )
