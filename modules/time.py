from datetime import datetime
import modules.time as time

def utime():
    import time
    return datetime.fromtimestamp(time.time())

def time():
    import time
    return time.time()

def todate(t):
    return datetime.fromtimestamp(t)