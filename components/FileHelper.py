import os
import uuid
import tkinter as tk

from pathlib import Path
from hurry.filesize import size
from tkinter.filedialog import askdirectory

class FileHelper:
    def ask_directory():
        root = tk.Tk()
        root.withdraw()
        path = askdirectory(title='Select Folder')
        return path
    
    def set_workdir(folder_path):
        os.chdir(folder_path)

    def get_list_directories(folder_path):
        directories = []
        for root, dirs, files in os.walk(folder_path):
            for dir_name in dirs:
                directories.append(os.path.join(root, dir_name))
        return directories
    
    def get_dir_size(folder_path):
        total = 0
        with os.scandir(folder_path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
        return size(total)  

    def get_filename_from_path(path):
        return os.path.basename(path)

    def change_path_filename(file_path, filename):
        path = Path(file_path)
        new_path = str(path.with_name(filename))
        return new_path

    def rename_path(file_path, file_path_new):
        path = Path(file_path)
        path.rename(file_path_new)

    def delete_file(file_path):
        os.remove(file_path)

    def rename_filename_with_format(file_path, format, filename_unique = False):
        filename = FileHelper.get_filename_from_path(file_path)
        filename_ext = os.path.splitext(filename)
        filename_base = filename_ext[0]
        if filename_unique:
            filename_new = FileHelper.generate_unique_filename(filename_base) + format
        else:
            filename_new = filename_base + format
        filename_new = filename_new.replace(" ", "_")
        path_new = FileHelper.change_path_filename(file_path, filename_new)
        return path_new

    def generate_unique_filename(base_filename):
        unique_id = uuid.uuid4().hex[:6] 
        unique_filename = f"{base_filename}_{unique_id}"
        return unique_filename

    def get_file_list(folder_path):
        file_list = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_list.append(file_path)
        return file_list
