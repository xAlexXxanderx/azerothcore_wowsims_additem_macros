import os
import sys
import argparse
import json
import collections
current_path = os.path.dirname(os.path.abspath(__file__))

def get_data(path_to_json_file):
    with open(path_to_json_file) as f:
        json_data = json.load(f)
    return(json_data)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", help="Path to exported JSON file", action='store')
args = parser.parse_args()

path_to_json_file = current_path+'/wowsims.json'
if args.filepath:
    path_to_json_file = args.filepath

gems_list = []
items = get_data(path_to_json_file)['player']['equipment']['items']
for item in items:
    print(".additem "+str(item['id']))
    if "gems" in item:
        for gem in item['gems']:
            gems_list.append(gem)

for gem, count in collections.Counter(gems_list).most_common():
    if gem != 0:
        print(".additem "+str(gem)+' '+str(count))

glyphs = get_data(path_to_json_file)['player']['glyphs']
for i in range(1,4):
    print(".additem "+str(glyphs['major'+str(i)]))
    print(".additem "+str(glyphs['minor'+str(i)]))
