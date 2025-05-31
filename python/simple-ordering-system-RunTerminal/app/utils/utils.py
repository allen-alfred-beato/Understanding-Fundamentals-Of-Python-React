import time


class Utilities:
    
    def delayFunction(callback, seconds):
        time.sleep(seconds)
        return callback()
        