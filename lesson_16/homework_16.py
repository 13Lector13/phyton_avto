from pathlib import Path
import json
import logging
import xml.etree.ElementTree as ET


def remove_csv_duplicates(csv_folder, result_file):
    csv_folder = Path(csv_folder)
    result_file = Path(result_file)

# csv_folder = Path(r"C:\Users\Lector\Desktop\Phyton_homework\files")

    print(csv_folder.exists())
    print(csv_folder.is_dir())

    unique_lines = set()

    for csv_file in csv_folder.iterdir():
        if csv_file.suffix == ".csv":
            with open(csv_file, "r", encoding="utf-8") as f:
                for line in f:
                    unique_lines.add(line.strip())


    with open(result_file, "w", encoding="utf-8") as f:
        for line in unique_lines:
            f.write(line + "\n")



remove_csv_duplicates(
    r"C:\Users\Lector\Desktop\Phyton_homework\files",
    r"C:\Users\Lector\Desktop\Phyton_homework\lesson_16\result_zakovorotnyi.csv"
)

json_logger = logging.getLogger("json_logger")
json_logger.setLevel(logging.ERROR)

json_handler = logging.FileHandler("json_zakovorotnyi.log", encoding="utf-8")
json_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

json_handler.setFormatter(json_formatter)
json_logger.addHandler(json_handler)


def validate_json_files(json_folder):
    json_folder = Path(json_folder)

    print(json_folder.exists())
    print(json_folder.is_dir())

    for json_file in json_folder.iterdir():
        if json_file.suffix == ".json":
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                json_logger.error(f"Invalid JSON in file {json_file.name}: {e}")



validate_json_files(
    r"C:\Users\Lector\Desktop\Phyton_homework\files"
)


xml_logger = logging.getLogger("xml_logger")
xml_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
xml_logger.addHandler(console_handler)


def log_all_incoming(xml_file):
    xml_file = Path(xml_file)
    if not xml_file.exists():
        xml_logger.error(f"File {xml_file} does not exist")
        return

    tree = ET.parse(xml_file)
    root = tree.getroot()

    found_any = False

    for incoming in root.findall(".//timingExbytes/incoming"):
        xml_logger.info(f"Found incoming: {incoming.text}")
        found_any = True

    if not found_any:
        xml_logger.info("No incoming values found in the file.")


log_all_incoming(
    r"C:\Users\Lector\Desktop\Phyton_homework\files\groups.xml"
)

