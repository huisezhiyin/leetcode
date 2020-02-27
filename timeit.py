import signal
import time


class TestException(Exception):
    pass


def timeit(max_time: int):
    def wrape(func):
        def exception(signum, frame):
            raise TestException

        def warnning(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, exception)
                signal.alarm(max_time)
                response = func(*args, **kwargs)
                signal.alarm(0)
                return response
            except TestException:
                print("time out warnning")

        return warnning

    return wrape
