"""
urclpy equivalent of https://github.com/ros2/rclpy/blob/master/rclpy/rclpy/node.py
"""

from .callback_groups import get_default_callback_group


class Node(object):
    def __init__(self, node_name: str):
        self.__name = node_name

        self._default_callback_group = get_default_callback_group()

    def get_name(self):
        return self.__name

    def create_subscription(self, msg_type, topic: str):
        raise NotImplementedError()

    def create_timer(self, timer_period_sec: float, callback, callback_group=None):
        if callback_group is None:
            callback_group = self._default_callback_group

        timer_period_usec = int(timer_period_sec * 1e6)

        def looped_timer(*args, **kwargs):
            callback(*args, **kwargs)
            callback_group.add_callback(
                callback_group.clock_us() + timer_period_usec, looped_timer
            )

        callback_group.add_callback(
            callback_group.clock_us() + timer_period_usec, looped_timer
        )
