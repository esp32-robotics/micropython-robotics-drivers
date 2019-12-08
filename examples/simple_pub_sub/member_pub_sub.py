import urclpy
import utime


def main(args=None):
    urclpy.init(args=args)

    n = urclpy.Node("chatter_node")

    print(n.get_name())

    # n.create_subscription(int, "/chatter")

    i = 1

    def print_time():
        nonlocal i
        print(i)
        i += 1

    n.create_timer(0.2, print_time)

    for _ in range(10):
        n._default_callback_group.wait_and_step()


if __name__ == "__main__":
    main()
