from ultralytics import YOLO

def load_yolo_model(yolo_model_path):
    return YOLO(yolo_model_path)