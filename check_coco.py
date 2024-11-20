from icecream import ic
import json

file_path = "coco_json/train.json"

with open(file_path, "r") as f:
    dataset = json.load(f)

# print(dataset)
ic(dataset)  # データ多くて見切れるので対策したい
