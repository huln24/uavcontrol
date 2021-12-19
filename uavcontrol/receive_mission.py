import argparse

from auvsi_suas.client import client

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True)
parser.add_argument("-u", "--username", required=True)
parser.add_argument("-p", "--password", required=True)
parser.add_argument("--mission_id", required=True)
args = parser.parse_args()

url = args.url
username = args.username
password = args.password
mission_id = args.mission_id

client = client.Client(url, username, password)

mission = client.get_mission(mission_id)

