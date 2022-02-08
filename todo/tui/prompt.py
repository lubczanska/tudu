import curses

import todo.exception as exception
import todo.tui.ui as ui

RED = 2


def commandline(screen: ui.Screen, prompt=':', startbuf='') -> str:
    """
    Collect and display text entered by the user.
    Input mode be escaped with ESC and confirmed with ENTER
    :param prompt: prompt to be displayed at the beginning of the line
    :param startbuf: starting contents of the buffer
    :return: text entered by the user
    """
    # the default curses textbox uses some weird emacs keybindings,
    # so I wrote a custom one
    curses.curs_set(True)
    buffer = startbuf
    history = screen.prompt_history
    prompt_len = len(prompt)

    pos = len(buffer)
    window = screen.w - prompt_len - 1

    screen.clear_prompt()
    screen.prompt(0, prompt)
    end_idx = window - prompt_len
    start_idx = 0
    if pos > end_idx:
        start_idx, end_idx = pos - end_idx, pos
    screen.prompt(prompt_len, buffer[start_idx:end_idx])
    screen.stdscr.move(screen.h - 1, pos - start_idx + prompt_len + 1)
    screen.stdscr.refresh()
    key = screen.stdscr.get_wch()
    # provide basic editing options
    while key != curses.KEY_ENTER and key not in [10, 13] and key != '\n':
        if key == curses.KEY_RESIZE:
            screen.resize()
            window = screen.w - prompt_len - 1
        elif key == curses.KEY_LEFT and pos > 0:
            pos -= 1
        elif key == curses.KEY_RIGHT and pos < len(buffer):
            pos += 1
        elif key == curses.KEY_UP or key == curses.KEY_DOWN:
            history, buffer = buffer, history
            pos = len(buffer)
        elif key == curses.KEY_BACKSPACE and pos > 0:
            buffer = buffer[:pos - 1] + buffer[pos:]
            pos -= 1
        elif key == (curses.KEY_DC or key == 127) and pos < len(buffer):
            buffer = buffer[:pos] + buffer[pos + 1:]
        elif key == curses.KEY_EXIT or key == chr(27):
            curses.curs_set(False)
            screen.clear_prompt()
            raise exception.EscapeKey
        elif type(key) == int:  # special keys, get_wch() returns them as ints
            key = screen.stdscr.get_wch()
            continue
        else:
            buffer = buffer[:pos] + key + buffer[pos:]
            pos += 1

        # draw prompt and buffer contents, then move cursor to correct position
        screen.clear_prompt()
        screen.prompt(0, prompt)
        end_idx = window - prompt_len
        start_idx = 0
        if pos > end_idx:
            start_idx, end_idx = pos - end_idx, pos
        screen.prompt(prompt_len, buffer[start_idx:end_idx])
        screen.stdscr.move(screen.h - 1, pos - start_idx + prompt_len + 1)
        screen.stdscr.refresh()
        key = screen.stdscr.get_wch()

    screen.prompt_history = buffer
    screen.clear_prompt()
    curses.curs_set(False)
    return buffer


def error_prompt(screen, message):
    """ Display a red text message in the prompt area """
    screen.clear_prompt()
    screen.prompt(0, message[:screen.w - 3], curses.color_pair(RED) | curses.A_BOLD)


def regular_prompt(screen, message):
    """ Display a white text message in the prompt are """
    screen.clear_prompt()
    screen.prompt(0, message[:screen.w - 3])

