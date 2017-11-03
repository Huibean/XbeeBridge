from Estimate.AttitudeEstimate import AttitudeEstimate
from Estimate.PositionEstimate import PositionEstimate

from system_args import mocap_bodies, white_list

from MocapBody import MocapBody
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
    global first_body_id
    if id in mocap_bodies:
        mocap_bodies[id].update(position, rotation)
    else:
        if id in white_list:
            mocap_bodies[id] = MocapBody(id, white_list[id])
            mocap_bodies[id].update(position, rotation)
            print("init new mocap body {0}".format(id))
        else:
            pass
            #  print("body id {0} not matching".format(id))
