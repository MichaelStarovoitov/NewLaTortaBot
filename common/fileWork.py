import os
import json

def append_to_json_file(file_path, new_element):
    if os.path.exists(file_path):
        with open(file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_element)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([new_element], file, indent=4, ensure_ascii=False)

def load_data(file_path):
    if os.path.exists(file_path):
        if os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4, ensure_ascii=False)
                data = []
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)
            data = []
    return data

def write_file(file_path, data):
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        data = ''
    return data