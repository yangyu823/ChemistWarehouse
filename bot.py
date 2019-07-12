from datetime import datetime, timedelta
from threading import Timer
import time, threading

# x = datetime.today()
# y = x.replace(day=x.day, hour=12, minute=0, second=0, microsecond=0) + timedelta(days=1)
# delta_t = y - x
#
# secs = delta_t.total_seconds()
#
#
# def hello_world():
#     print(secs)
#     # ...
#
#
# t = Timer(1, hello_world)
# t.start()

WAIT_SECONDS = 1


def foo():
    print(time.ctime())
    threading.Timer(WAIT_SECONDS, foo).start()


foo()
