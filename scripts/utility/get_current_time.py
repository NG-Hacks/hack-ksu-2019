import time

def get_current_time():
    date_str = time.strftime("%Y-%m-%dT%H:%M:%S.", time.localtime())
    msec = int((time.time()-int(time.time()))*1000)
    date_str = date_str + str(msec)+"Z"
    return date_str