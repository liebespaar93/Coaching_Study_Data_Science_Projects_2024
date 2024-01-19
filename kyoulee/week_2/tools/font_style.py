#!/usr/bin/env python
# coding: utf-8

class style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UDLINE = "\033[4m"
    BLINK = "\033[5m"
    INVERT = "\033[7m"
    HIDDEN = "\033[8m"


class bg(style):
    RED = "\033[41m"
    YELLOW = "\033[43m"
    LRED = "\033[101m"
    LYELLOW = "\033[103m"


class fg(style):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    LRED = "\033[91m"
    LGREEN = "\033[92m"
    LYELLOW = "\033[93m"
    LBLUE = "\033[94m"
    LMAGENTA = "\033[95m"
    LCYAN = "\033[96m"
    WHITE = "\033[97m"