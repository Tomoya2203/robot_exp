import labelme2coco
# How to use https://github.com/fcakyon/labelme2coco

labelme_folder = "./all_file"
export_dir = "coco_json"
category_id_start = 1
train_split_rate = 0.8

labelme2coco.convert(labelme_folder, export_dir,train_split_rate=train_split_rate, category_id_start=category_id_start)

