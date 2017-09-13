# import json
#
# with open("json_example.json", "r", encoding ="utf8") as f:
#     contents = f.read()
#     json_data = json.loads(contents)
#     print(type(json_data["employees"][0]))
#     print(json_data["employees"][0]["firstName"])
#
#

import json

dict_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

with open("data.json", "w") as f:
    json.dump(dict_data, f)
    