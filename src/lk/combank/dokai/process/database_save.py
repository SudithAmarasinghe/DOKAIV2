# import json
# import os
# import cv2
# from model.yolo.yolo_call import load_yolo_model
# from model.ocr.ocr_call import perform_ocr
# from model.deepseek.deepseekCall import get_description, get_title, get_text, get_summ

# class ReportProcessor:
#     def __init__(self, yolo_model_path, image_folder, output_folder, json_file):
#         self.yolo = load_yolo_model(yolo_model_path)
#         self.image_folder = image_folder
#         self.output_folder = output_folder
#         self.json_file = json_file
#         self.data = []
        
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#     def load_images(self):
#         images = []
#         for filename in os.listdir(self.image_folder):
#             if filename.endswith(".jpg") or filename.endswith(".png"):
#                 images.append(os.path.join(self.image_folder, filename))
#         return images

#     def detect_objects(self, image_path):
#         results = self.yolo(image_path)  # Run inference on the image
#         return results

#     def save_detected_objects(self, image, results, image_id, image_path):
#         objects = []
#         last_object_id = None  # Initialize the last object ID

#         # Extract the page number from the image_id (assuming image_id is the filename without extension)
#         page_number = image_id
        
#         # Create a list to hold all the objects with their coordinates
#         object_data = []

#         for i, result in enumerate(results[0].boxes):
#             x1, y1, x2, y2 = map(int, result.xyxy[0])  # Extracting the bounding box coordinates
#             label_index = result.cls[0].item()  # Get the class index
#             label = self.yolo.names[label_index]  # Map the class index to the label
#             cropped_image = image[y1:y2, x1:x2]
#             object_filename = f"{page_number}_{i}_{label}.jpg"  # Ensure the filename has an extension
#             object_path = os.path.join(self.output_folder, object_filename)
#             print(f"Saving object: {object_path}")

#             success = cv2.imwrite(object_path, cropped_image)
#             if not success:
#                 print(f"Failed to save {object_path}")

#             if label == 'text':
#                 text = get_text(object_path)
#                 # Store the object data with its coordinates
#                 object_data.append({
#                     "id": object_filename,
#                     "label": label,
#                     "description": text,
#                     "image_path": os.path.abspath(object_path),
#                     "before_object": last_object_id,
#                     "x1": x1,
#                     "y1": y1
#                 })
#                 try:
#                     os.remove(object_path)
#                 except:
#                     print(f"Can not remove {object_path}")
#             elif label == 'table':
#                 summ= get_summ(object_path)
#                 # Store the object data with its coordinates
#                 object_data.append({
#                     "id": object_filename,
#                     "label": label,
#                     "description": summ,
#                     "image_path": os.path.abspath(object_path),
#                     "before_object": last_object_id,
#                     "x1": x1,
#                     "y1": y1
#                 })
#                 try:
#                     os.remove(object_path)
#                 except:
#                     print(f"Can not remove {object_path}")
#             else:
#                 title= get_title(object_path)
#                 desc = get_description(object_path)
#                 # Store the object data with its coordinates
#                 object_data.append({
#                     "id": object_filename,
#                     "label": label,
#                     "title": title,
#                     "description": desc,
#                     "image_path": os.path.abspath(object_path),
#                     "before_object": last_object_id,
#                     "x1": x1,
#                     "y1": y1
#                 })
            
#             last_object_id = object_filename  # Update the last object ID

#         # Sort the objects by their y1 and x1 coordinates
#         sorted_objects = sorted(object_data, key=lambda obj: (obj['y1'], obj['x1']))

#         # Update the objects list with the sorted objects
#         objects = [obj for obj in sorted_objects]

#         return objects

#     def process_reports(self):
#         images = self.load_images()
#         for image_path in images:
#             image_id = os.path.splitext(os.path.basename(image_path))[0]
#             image = cv2.imread(image_path)
#             if image is None:
#                 print(f"Failed to load image {image_path}")
#                 continue
#             results = self.detect_objects(image_path)
#             objects = self.save_detected_objects(image, results, image_id, image_path)
#             self.data.append({
#                 "image_id": image_id,
#                 "objects": objects
#             })

#         with open(self.json_file, 'w') as f:
#             json.dump(self.data, f, indent=4)





import json
import os
import cv2
from model.yolo.yolo_call import load_yolo_model
from model.ocr.ocr_call import perform_ocr
from model.deepseek.deepseekCall import get_description, get_summ, get_text, get_title

class ReportProcessor:
    def __init__(self, yolo_model_path, image_folder, output_folder, json_file):
        self.yolo = load_yolo_model(yolo_model_path)
        self.image_folder = image_folder
        self.output_folder = output_folder
        self.json_file = json_file
        self.data = []
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def load_images(self):
        images = []
        for filename in os.listdir(self.image_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                images.append(os.path.join(self.image_folder, filename))
        return images

    def detect_objects(self, image_path):
        results = self.yolo(image_path)  # Run inference on the image
        return results

    def save_detected_objects(self, image, results, image_id, image_path):
        objects = []
        last_object_id = None  # Initialize the last object ID

        # Extract the page number from the image_id (assuming image_id is the filename without extension)
        page_number = image_id
        
        # Create a list to hold all the objects with their coordinates
        object_data = []

        for i, result in enumerate(results[0].boxes):
            x1, y1, x2, y2 = map(int, result.xyxy[0])  # Extracting the bounding box coordinates
            label_index = result.cls[0].item()  # Get the class index
            label = self.yolo.names[label_index]  # Map the class index to the label
            cropped_image = image[y1:y2, x1:x2]
            object_filename = f"{page_number}_{i}_{label}.jpg"  # Ensure the filename has an extension
            object_path = os.path.join(self.output_folder, object_filename)
            print(f"Saving object: {object_path}")

            success = cv2.imwrite(object_path, cropped_image)
            print(success)
            if not success:
                print(f"Failed to save {object_path}")

            if label == 'text':
                print(type(object_path))      ############################################ <-----------------
                text = get_text(object_path)
                # Store the object data with its coordinates
                object_data.append({
                    "id": object_filename,
                    "label": label,
                    "description": text,
                    "image_path": os.path.abspath(object_path),
                    "before_object": last_object_id,
                    "x1": x1,
                    "y1": y1
                })
                try:
                    os.remove(object_path)
                except:
                    print(f"Can not remove {object_path}")
            elif label == 'table':
                summ= get_summ(object_path)
                # Store the object data with its coordinates
                object_data.append({
                    "id": object_filename,
                    "label": label,
                    "description": summ,
                    "image_path": os.path.abspath(object_path),
                    "before_object": last_object_id,
                    "x1": x1,
                    "y1": y1
                })
                try:
                    os.remove(object_path)
                except:
                    print(f"Can not remove {object_path}")
            else:
                title= get_title(object_path)
                desc = get_description(object_path)
                # Store the object data with its coordinates
                object_data.append({
                    "id": object_filename,
                    "label": label,
                    "title": title,
                    "description": desc,
                    "image_path": os.path.abspath(object_path),
                    "before_object": last_object_id,
                    "x1": x1,
                    "y1": y1
                })
            
            last_object_id = object_filename  # Update the last object ID

        # Sort the objects by their y1 and x1 coordinates
        sorted_objects = sorted(object_data, key=lambda obj: (obj['y1'], obj['x1']))

        # Update the objects list with the sorted objects
        objects = [obj for obj in sorted_objects]

        return objects

    def process_reports(self):
        images = self.load_images()
        for image_path in images:
            image_id = os.path.splitext(os.path.basename(image_path))[0]
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to load image {image_path}")
                continue
            results = self.detect_objects(image_path)
            objects = self.save_detected_objects(image, results, image_id, image_path)
            self.data.append({
                "image_id": image_id,
                "objects": objects
            })

        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=4)

