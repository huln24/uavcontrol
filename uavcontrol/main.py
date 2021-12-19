import argparse
import auvsi_suas.client

import uavcontrol.receive_mission


parser = argparse.ArgumentParser()
parser.add_argument('--username')
parser.add_argument('--password')
args = parser.parse_args()

print(args.username, args.password)