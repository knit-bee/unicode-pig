import os
import platform
import sys
import time
from collections import deque

if platform.system() == "Windows":
    import WConio2 as wcon


class Pig:
    def run(self, reversed=False):
        print("\n")
        terminal_size = os.get_terminal_size().columns - 10
        if platform.system() == "Windows":
            self._print_for_windows(reversed=reversed, terminal_size=terminal_size)
        else:
            self._print_for_linux(reversed=reversed, terminal_size=terminal_size)

    def _print_for_windows(self, reversed=False, terminal_size=50):
        queue1, queue2 = self._generate_pig_queue(reversed=reversed)
        if reversed:
            space_range = range(0, terminal_size)
        else:
            space_range = range(terminal_size, 0, -1)
        cursor_x, cursor_y = wcon.wherex(), wcon.wherey()
        for space in space_range:
            pad_space = " " * space
            time.sleep(4 / terminal_size)
            for i in range(len(queue1)):
                if space % 2:
                    print(pad_space + queue1[i])
                else:
                    print(pad_space + queue2[i])
            wcon.gotoxy(cursor_x, cursor_y)
            for _ in range(len(queue1)):
                print(" " * 20)

    def _print_for_linux(self, reversed=False, terminal_size=50):
        queue1, queue2 = self._generate_pig_queue(reversed=reversed)
        if reversed:
            space_range = range(0, terminal_size)
        else:
            space_range = range(terminal_size, 0, -1)
        for space in space_range:
            pad_space = " " * space
            time.sleep(4 / terminal_size)
            for _ in range(len(queue1)):
                sys.stdout.write("\x1b[1A\x1b[2K")
            for i in range(len(queue1)):
                if space % 2:
                    sys.stdout.write(pad_space + queue1[i] + "\n")
                else:
                    sys.stdout.write(pad_space + queue2[i] + "\n")
        for _ in range(len(queue1)):
            sys.stdout.write("\x1b[1A\x1b[2K")

    def _generate_pig_queue(self, reversed=False):
        pig = [" ^^___  ", "@''   )ð", "  '`'`  "]
        queue1 = deque([], 3)
        queue2 = deque([], 3)
        for line in pig[:2]:
            if reversed:
                line = line[::-1].replace(")", "(")
            queue1.append(line)
            queue2.append(line)
        if reversed:
            queue1.append(pig[2][::-1])
            queue2.append("  ´'´'  "[::-1])
        else:
            queue1.append(pig[2])
            queue2.append("  ´'´'  ")
        return queue1, queue2


def main():
    piglet = Pig()
    print("\n")
    piglet.run()


if __name__ == "__main__":
    main()
