import json
import os

class JsonSorter:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.data = self.load_json()

    def load_json(self):
        with open(self.json_file_path, 'r') as file:
            return json.load(file)

    def sort_objects(self):
        last_object_id = None
        for page in self.data:
            # Sort the objects based on y1 within a range of ±100 and then x1
            page['objects'] = sorted(page['objects'], key=lambda obj: (obj['y1'] // 100, obj['x1']))
            # Assign new ids to each object based on their order and type
            for i, obj in enumerate(page['objects'], start=1):
                obj_id = f"{i}_{obj['id']}"
                obj['id'] = obj_id
                obj["before_object"] = last_object_id
                previous_id = obj['id']
                # Remove x1 and y1 keys
                del obj['x1']
                del obj['y1']
                last_object_id = obj_id

    def save_sorted_json(self, output_file_path):
        with open(output_file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def delete_input_file(self):
        os.remove(self.json_file_path)
