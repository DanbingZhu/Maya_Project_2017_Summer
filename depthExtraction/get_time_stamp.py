import rosbag
import sys
import os
bag = rosbag.Bag('kinectv1_2017-06-08-15-35-13.bag')

timestamps = []

for topic, msg, t in bag.read_messages(topics=['/camera/depth_registered/image_raw']):
    timestamps.append("%f\n"%t.to_sec())

file = open("timestamp.txt", "w")
file.write("".join(timestamps))
file.close()
bag.close()
