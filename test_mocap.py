from NatNetClient import NatNetClient

def receiveNewFrame( frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount, labeledMarkerCount, latency, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    #  print('frameNumber: {0}, markerSetCount: {1}, unlabeledMarkersCount: {2}, rigidBodyCount: {3}, skeletonCount: {4}, labeledMarkerCount: {5}, latency: {6}, timecode: {7}, timecodeSub: {8}, timestamp: {9}, isRecording: {10}, trackedModelsChanged: {11}'.format(frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount, labeledMarkerCount, latency, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged))
    pass

import time
sys_counter = time.time()

def receiveRigidBodyFrame(id, position, rotation ):
    #  print( "Received frame for rigid body", id )
    #  print( "position: ", position )
    #  print( "rotation: ", rotation )

    global sys_counter

    if id == 1:
        now = time.time()
        print(now - sys_counter)
        sys_counter = now
    

nat_net_streaming_client = NatNetClient(serverIPAddress="10.0.0.150")

nat_net_streaming_client.newFrameListener = None
nat_net_streaming_client.rigidBodyListener = receiveRigidBodyFrame
nat_net_streaming_client.run()

import time
while True:
    time.sleep(1)
