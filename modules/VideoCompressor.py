import os
import subprocess

class VideoCompressor:
    def compress(self, path_to_file, path_to_output, filename):
        filename_ext = os.path.splitext(filename)
        filename_new = filename_ext[0] + '.mp4'
        filename_new = filename_new.replace(" ", "_")
        file_path = os.path.join(path_to_output, filename_new)

        cmd = f'ffmpeg -nostats -loglevel 0 -i "{path_to_file}" -vcodec libx265 -x265-params log-level=none -crf 28 "{file_path}"'
        subprocess.run(cmd, shell=True)