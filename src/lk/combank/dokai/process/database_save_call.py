from process.database_save import ReportProcessor
from process.json_sorter import JsonSorter

def save(company, year):
    processor = ReportProcessor(
        yolo_model_path="model/yolo/best_yolo.pt",
        image_folder="images",  # change the path to the input image folder
        output_folder=f"database/{company}_{year}/figures",
        json_file="database/database.json"
    )
    processor.process_reports()

    sorter = JsonSorter('database/database.json')
    sorter.sort_objects()
    sorter.save_sorted_json('database/{company}_{year}/{company}_{year}.json')
    sorter.delete_input_file()






# if __name__ == "__main__":
#     processor = ReportProcessor(
#         yolo_model_path="model/yolo/best_yolo.pt",
#         image_folder="images",  # change the path to the input image folder
#         output_folder="database/2022_CommercialBank/images",
#         json_file="database/database.json"
#     )
#     processor.process_reports()

#     sorter = JsonSorter('database/database.json')
#     sorter.sort_objects()
#     sorter.save_sorted_json('database/2022_CommercialBank/database_sorted.json')
#     sorter.delete_input_file()