from datetime import datetime


def get_datetime():
    now = datetime.now()
    now = now.strftime("%Y%m%d%H%M%S")
    return int(now)
