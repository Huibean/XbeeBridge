from Estimate.AttitudeEstimate import AttitudeEstimate
from Estimate.PositionEstimate import PositionEstimate

from system_args import mocap_body_team, white_list

from xbee.python2to3 import intToByte, stringToBytes

import time, datetime

def receiveNewFrame( frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount, labeledMarkerCount, latency, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    #  print( "Received frame", frameNumber )
    #  print("latency", latency)
    pass

def receiveRigidBodyFrame(id, position, rotation ):
    #  print( "Received frame for rigid body", id )
    #  print( "position: ", position )
    #  print( "rotation: ", rotation )
    if not mocap_body_team.is_exist(id):
        mocap_body_team.create_new_body(id)

    mocap_body_team.body(id).update(position, rotation)
