# from winbase.h
STDOUT = -11
STDERR = -12

try:
    import ctypes
    from ctypes import LibraryLoader

    windll = LibraryLoader(ctypes.WinDLL)
    from ctypes import wintypes
except (AttributeError, ImportError):
    windll = None
    setConsoleTextAttribute = lambda *_: None
    winapi_test = lambda *_: None
else:
    from ctypes import byref, Structure, c_char, POINTER

    COORD = wintypes._COORD


    class CONSOLE_SCREEN_BUFFER_INFO(Structure):
        """struct in wincon.h"""
        _fields_ = [
            ("dwSize", COORD)
        ]
