import json
import pprint
import nicePrinter

with open("classic_dump.json") as json_data:
    x = json.load(json_data)

for pub in x:
    print("\n")
    print("Title: ", pub["bibliography"]["title"])
    print("Author: ", pub["bibliography"]["author"]["name"])
    print("Published: ", pub["bibliography"]["publication"]["full"])
    print("Themes: \n" + nicePrinter.nicePrinter(pub["bibliography"]["subjects"][0:3]))
