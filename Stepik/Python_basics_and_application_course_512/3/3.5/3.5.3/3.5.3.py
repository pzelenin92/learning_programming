import json
student1 = {
    "first_name": "Oleg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Good job, Greg"
}
student2 = {
    "first_name": "Wirl",
    "last_name": "Wood",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Nicely Done"
}
data = [student1, student2]

data_json=json.dumps(data,indent=4)

print(data_json)

# with open("jsonfile.json","w") as jsonfile:
#     json.dump(data,jsonfile,indent=4)

data_again=json.loads(data_json)
# print(data_again[1]["last_name"])
with open("jsonfile.json", "r") as f:
    data_again_1=json.load(f)
    print(data_again_1)
