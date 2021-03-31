from code import InteractiveInterpreter
from sys import stderr


class Console:
    def __init__(self, loc):
        self._buffer = []
        self._interpreter = InteractiveInterpreter(locals=loc)

    def get_buffer(self):
        return self._buffer

    def set_locals(self, loc):
        self._interpreter.locals = loc

    @staticmethod
    def multiline_input(string=""):
        """
        Работает как input но в многострочном режиме
        """
        print(string, end="")
        var = "\n".join(iter(input, ""))
        return var

    def run_code(self, code: str):
        """
        Запуск кода и вывод исключений при их возникновении
        """
        self._buffer.append(code)
        try:
            self._interpreter.runcode(code)
        except:
            self._interpreter.showsyntaxerror()
            self._interpreter.showtraceback()
            stderr.flush()
