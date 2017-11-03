from threading import Thread
from system_args import xbee_device

class WatchMan(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print(xbee_device.wait_read_frame()) 
