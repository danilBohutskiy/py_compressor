from components.FileHelper import FileHelper

import uuid
import os
import subprocess

class VideoCompressor:

    FORMAT_MP4 = '.mp4'

    def compress(self, path_to_file):
        path_new = self.get_new_path(path_to_file)
        cmd = f'ffmpeg -nostats -loglevel 0 -i "{path_to_file}" -vcodec libx265 -x265-params log-level=none -crf 28 "{path_new}" && rm "{path_to_file}"'
        subprocess.run(cmd, shell=True)
        FileHelper.rename_path(path_new, path_to_file)
    
    def get_new_path(self, path_to_file):
        filename = FileHelper.get_filename_from_path(path_to_file)
        filename_ext = os.path.splitext(filename)
        filename_base = filename_ext[0]
        filename_new = self.generate_unique_filename(filename_base) + self.FORMAT_MP4
        filename_new = filename_new.replace(" ", "_")
        path_new = FileHelper.change_path_filename(path_to_file, filename_new)

        return path_new
    
    def generate_unique_filename(self, base_filename):
        unique_id = uuid.uuid4().hex[:6] 
        unique_filename = f"{base_filename}_{unique_id}"
        return unique_filename