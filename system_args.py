import yaml
settings = yaml.load(open('setting.yml'))

from MocapBodyTeam import MocapBodyTeam
mocap_body_team = MocapBodyTeam()

mocap_pc_ip = settings['mocap_pc_ip']
serial_name = settings['serial_name']
white_list = settings['white_list']

#  import serial
#  from xbee import ZigBee, DigiMesh

#  serial_port = serial.Serial(serial_name, 57600, write_timeout=0.01, timeout=0.005)
#  xbee_device = DigiMesh(serial_port)

#  from pymavlink.mavutil import mavserial
#  mav = mavserial(serial_name, 57600)
