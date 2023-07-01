next_pin = 0


def new_pin():
    global next_pin
    next_pin += 1
    return next_pin


def pin_print(s, a_pin):
    print(f'{a_pin}: {s}')