import urclpy


def main(args=None):
    urclpy.init(args=args)

    n = urclpy.Node("chatter_node")

    print(n.get_name())

    i = 1

    pub = n.create_publisher(int, "/chatter", 0)

    def print_time():
        nonlocal i
        print("Sending:", i)
        pub.publish(i)
        i += 1

    def on_msg(msg):
        print("Got message:", msg)

    n.create_subscription(int, "/chatter", on_msg, 0)

    n.create_timer(0.2, print_time)

    for _ in range(10):
        n._default_callback_group._wait_and_step()


if __name__ == "__main__":
    main()
