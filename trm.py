import regex as re


def trm_print(s):
    import inspect
    # https://stackoverflow.com/questions/13699283/how-to-get-the-callers-filename-method-name-in-python
    filename = inspect.stack()[1].filename
    filename_match = re.findall(r'(?:Integration/)(.*)', filename)
    filename_joined = ''.join(filename_match)
    name = filename_joined
    print(f'[{name}]: {s}')