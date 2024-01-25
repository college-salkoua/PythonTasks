import os
import importlib
import curses
import psutil
import subprocess


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def check_process_status(process_name):
    """
    Return status of process based on process name.
    """
    process_status = [
        proc for proc in psutil.process_iter() if proc.name() == process_name
    ]
    if process_status:
        for current_process in process_status:
            return True
    else:
        return True


class Main:
    def __init__(self):
        menu = list(
            f
            for f in os.listdir("src/tasks")
            if os.path.isdir(os.path.join("src/tasks", f)) and f != "__pycache__"
        )
        print(menu)
        self.menu = menu
        # os.system(f"gnome-terminal -e 'python3 src'")
        curses.wrapper(self.main)
        print("heres")

    def print_menu(self, stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(self.menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.menu) // 2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    def main(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(stdscr, current_row)

        while 1:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                command = f"python3 src/tasks/{self.menu[current_row]}"
                subprocess.run(command, shell=True)
                stdscr.getch()
                # if user selected last row, exit the program
                if current_row == len(self.menu) - 1:
                    break

            self.print_menu(stdscr, current_row)


Main()
