import json

with open("classics.json") as json_data:
    d = json.load(json_data)

usefullist = d[0:3]

with open("classic_dump.json", "w") as outfile:
    json.dump(usefullist, outfile)
    print(usefullist)

