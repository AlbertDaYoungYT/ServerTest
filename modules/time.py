from datetime import datetime
from time import *

def utime():
    import time
    return datetime.fromtimestamp(time.time())

def time():
    import time
    return time.time()

def todate(t):
    return datetime.fromtimestamp(t)