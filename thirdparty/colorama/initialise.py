orig_stdout = None
orig_stderr = None

wrapped_stdout = None
wrapped_stderr = None

atexit_done = False


def init(autoreset=False, convert=None, strip=None, wrap=True):
    if not wrap and any([autoreset, convert, strip]):
        raise ValueError('wrap=False conflicts with any other arg=True')

    global wrapped_stdout, wrapped_stderr
    global orig_stdout, orig_stderr
