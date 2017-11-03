import yaml
settings = yaml.load(open('setting.yml'))

mocap_bodies = {}
mocap_pc_ip = settings['mocap_pc_ip']
serial_name = settings['serial_name']
white_list = settings['white_list']

import serial
from xbee import XBee, ZigBee

serial_port = serial.Serial(serial_name, 57600, timeout=0.02)
xbee_device = ZigBee(serial_port)

from pymavlink.mavutil import mavserial
mav = mavserial(serial_name, 57600)
