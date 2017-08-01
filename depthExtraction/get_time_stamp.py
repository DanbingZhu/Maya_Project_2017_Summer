import argparse
import rosbag
import sys
import os

def get_time_stamp(bag_file, timestamp_file):
	bag = rosbag.Bag(bag_file)
	timestamps = []

	for topic, msg, t in bag.read_messages(topics=['/camera/depth_registered/image_raw']):
		timestamps.append("%f\n"%t.to_sec())

	file = open(timestamp_file, "w")
	file.write("".join(timestamps))
	file.close()
	bag.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    This script extracts timestamps from a ros bag file.
    ''')

    parser.add_argument('bag_file', help='input bag file (format: bag)')
    parser.add_argument('timestamp_file', help='output timestamp file (format: txt)')
    args = parser.parse_args()

    get_time_stamp(args.bag_file,args.timestamp_file)
